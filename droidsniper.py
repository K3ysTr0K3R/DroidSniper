#!/usr/bin/env python3

import re
import socket
import argparse
import ipaddress
from rich.console import Console
from alive_progress import alive_bar
from concurrent.futures import ThreadPoolExecutor, as_completed

class AndroidDebugBridgeScanner:
    def __init__(self):
        self.results = []
        self.console = Console()

    def ascii_art(self):
        self.console.print("[bold bright_green]______           _     _ _____       _[/bold bright_green]")
        self.console.print("[bold bright_green]|  _  \         (_)   | /  ___|     (_)[/bold bright_green]")
        self.console.print("[bold bright_green]| | | |_ __ ___  _  __| \ `--. _ __  _ _ __   ___ _ __[/bold bright_green]")
        self.console.print("[bold bright_green]| | | | '__/ _ \| |/ _` |`--. \ '_ \| | '_ \ / _ \ '__|[/bold bright_green]")
        self.console.print("[bold bright_green]| |/ /| | | (_) | | (_| /\__/ / | | | | |_) |  __/ |[/bold bright_green]")
        self.console.print("[bold bright_green]|___/ |_|  \___/|_|\__,_\____/|_| |_|_| .__/ \___|_|[/bold bright_green]")
        self.console.print("[bold bright_green]                                      | |[/bold bright_green]")
        self.console.print("Coded By: K3ysTr0K3R                  [bold bright_green]|_|[/bold bright_green]")
        print("")

    def retrieve(self, ip):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((str(ip), 5555))
            sock.send(b"\x43\x4e\x58\x4e\x00\x00\x00\x01\x00\x10\x00\x00\x07\x00\x00\x00\x32\x02\x00\x00\xbc\xb1\xa7\xb1\x68\x6f\x73\x74\x3a\x3a\x00")
            data = sock.recv(2048)
            sock.close()
            return data.decode('utf-8', 'ignore')
        except Exception:
            return None

    def scanner(self, ip, data, output_file=None):
        if data and 'product' in data:
            try:
                product_name = re.search("product.name=(.*?);", data)
                product_model = re.search("ro.product.model=(.*?);", data)
                product_device = re.search(";ro.product.device=(.*?);", data)
                if product_name and product_model and product_device:
                    result = f"[bold bright_green][+][/bold bright_green] Android Debug Bridge Detected | Target: [bold cyan]{ip.ljust(15)}[/bold cyan] | Product Name: [bold bright_magenta]{product_name.group(1).ljust(15)}[/bold bright_magenta] | Product Model: [bold bright_magenta]{product_model.group(1).ljust(15)}[/bold bright_magenta] | Product Device: [bold bright_magenta]{product_device.group(1).ljust(15)}[/bold bright_magenta]"
                    self.console.print(result)
                    self.results.append(result)
                    if output_file:
                        self.store_results(output_file, result + "\n")
            except Exception:
                None

    def store_results(self, file_path, data):
        with open(file_path, "a") as file:
            file.write(data)

    def scan_subnet_or_ip(self, subnet_or_ip, output_file=None, threads=1):
        try:
            network = ipaddress.ip_network(subnet_or_ip, strict=False)
            total_ips = len(list(network.hosts()))
            with alive_bar(total_ips, title="Scanning Targets", bar="smooth", enrich_print=False) as bar:
                with ThreadPoolExecutor(max_workers=threads) as executor:
                    futures = {executor.submit(self.retrieve, str(ip)): str(ip) for ip in network.hosts()}
                    for future in as_completed(futures):
                        ip = futures[future]
                        data = future.result()
                        if data:
                            self.scanner(ip, data, output_file)
                        bar()
        except ValueError:
            with alive_bar(1, title="Scanning Target", bar="smooth", enrich_print=False) as bar:
                data = self.retrieve(subnet_or_ip)
                if data:
                    self.scanner(subnet_or_ip, data, output_file)
                bar()

    def scan_from_file(self, target_file, threads=1, output_file=None):
        with open(target_file, "r") as ip_file:
            ip_hosts = [line.strip() for line in ip_file.readlines()]
            if not ip_hosts:
                return

            with alive_bar(len(ip_hosts), title="Scanning Targets", bar="smooth", enrich_print=False) as bar:
                with ThreadPoolExecutor(max_workers=threads) as executor:
                    futures = {executor.submit(self.retrieve, ip): ip for ip in ip_hosts}
                    for future in as_completed(futures):
                        ip = futures[future]
                        data = future.result()
                        if data:
                            self.scanner(ip, data, output_file)
                        bar()

    def main(self):
        self.ascii_art()
        parser = argparse.ArgumentParser(description="DroidSniper - Android Debug Bridge (ADB) Scanner")
        parser.add_argument('-ip', '--ipaddress', type=str, help="IP address to scan or subnet in CIDR notation.")
        parser.add_argument('-f', '--file', type=str, help="File containing IP addresses to scan.")
        parser.add_argument('-o', '--output', type=str, help="File to store results.")
        parser.add_argument('-t', '--threads', type=int, help="Number of threads you wish to use for the scan.")

        args = parser.parse_args()

        if args.ipaddress:
            self.scan_subnet_or_ip(args.ipaddress, output_file=args.output, threads=args.threads)
        elif args.file:
            self.scan_from_file(args.file, output_file=args.output, threads=args.threads)
        else:
            parser.print_help()

if __name__ == "__main__":
    scanner = AndroidDebugBridgeScanner()
    scanner.main()
