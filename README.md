# DroidSniper

# ADB Misconfiguration Scanner

## Overview

This tool is designed to detect Android devices vulnerable to unauthorized access via the Android Debug Bridge (ADB) due to misconfiguration. By scanning for ADB instances that lack proper authentication, security teams can identify and mitigate potential vulnerabilities, safeguarding devices from unauthorized access.

## Features

- **Scan Network**: Rapidly scans the local network for devices with open ADB ports.
- **Misconfiguration Detection**: Identifies devices with ADB configured without authentication, highlighting potential security risks.
- **Comprehensive Reporting**: Generates detailed reports on detected vulnerabilities, facilitating targeted security enhancements.

## Secure ADB Connection Guide

For users and security professionals, establishing a secure connection to Android devices via ADB is crucial. Below are steps to connect securely using ADB version 1.0.41, ensuring devices are configured to prevent unauthorized access.

### Initial Setup

1. **Install ADB**: Ensure ADB (version 1.0.41 or above) is installed on your system. It's typically part of the Android SDK Platform-Tools.

2. **USB Connection**: Initially connect your Android device to your computer via USB. This is necessary even for TCP/IP connections to set up the device for remote debugging.

### Enabling Developer Options and USB Debugging

3. **Activate Developer Options**: On the device, go to Settings > About phone and tap 'Build number' seven times.

4. **Enable USB Debugging**: In 'Developer options', toggle 'USB Debugging' to enabled.

### Establishing a Secure Connection

#### USB (Recommended for Security)

5. **Connect and Verify**: With the device connected via USB, use `adb devices` to list connected devices, ensuring yours is detected.

#### TCP/IP (Wireless)

6. **Enable ADB Over TCP/IP**:
    - Switch ADB to TCP/IP mode: `adb tcpip 5555`
    - Disconnect the USB cable.

7. **Connect Wirelessly**:
    - Obtain your device's IP address.
    - Connect to your device: `adb connect <device-ip-address>:5555`
    - Confirm with `adb devices`.

### Security Tips

- **Secure Network**: Use a secure, trusted network for TCP/IP connections.
- **Disable ADB Over Network After Use**: Execute `adb usb` to revert to USB-only mode, closing the TCP/IP connection and enhancing security.

## Installation

Clone the repository and navigate to the project directory. Follow the setup instructions specific to your system to install any dependencies and configure the tool.

```bash
git clone <repository-url>
cd adb-misconfiguration-scanner
# Follow setup instructions for your environment
# ADB Misconfiguration Scanner

## Overview

This tool is designed to detect Android devices vulnerable to unauthorized access via the Android Debug Bridge (ADB) due to misconfiguration. By scanning for ADB instances that lack proper authentication, security teams can identify and mitigate potential vulnerabilities, safeguarding devices from unauthorized access.

## Features

- **Scan Network**: Rapidly scans the local network for devices with open ADB ports.
- **Misconfiguration Detection**: Identifies devices with ADB configured without authentication, highlighting potential security risks.
- **Comprehensive Reporting**: Generates detailed reports on detected vulnerabilities, facilitating targeted security enhancements.

## Secure ADB Connection Guide

For users and security professionals, establishing a secure connection to Android devices via ADB is crucial. Below are steps to connect securely using ADB version 1.0.41, ensuring devices are configured to prevent unauthorized access.

### Initial Setup

1. **Install ADB**: Ensure ADB (version 1.0.41 or above) is installed on your system. It's typically part of the Android SDK Platform-Tools.

2. **USB Connection**: Initially connect your Android device to your computer via USB. This is necessary even for TCP/IP connections to set up the device for remote debugging.

### Enabling Developer Options and USB Debugging

3. **Activate Developer Options**: On the device, go to Settings > About phone and tap 'Build number' seven times.

4. **Enable USB Debugging**: In 'Developer options', toggle 'USB Debugging' to enabled.

### Establishing a Secure Connection

#### USB (Recommended for Security)

5. **Connect and Verify**: With the device connected via USB, use `adb devices` to list connected devices, ensuring yours is detected.

#### TCP/IP (Wireless)

6. **Enable ADB Over TCP/IP**:
    - Switch ADB to TCP/IP mode: `adb tcpip 5555`
    - Disconnect the USB cable.

7. **Connect Wirelessly**:
    - Obtain your device's IP address.
    - Connect to your device: `adb connect <device-ip-address>:5555`
    - Confirm with `adb devices`.

### Security Tips

- **Secure Network**: Use a secure, trusted network for TCP/IP connections.
- **Disable ADB Over Network After Use**: Execute `adb usb` to revert to USB-only mode, closing the TCP/IP connection and enhancing security.

## Installation

Clone the repository and navigate to the project directory. Follow the setup instructions specific to your system to install any dependencies and configure the tool.

```bash
git clone <repository-url>
cd adb-misconfiguration-scanner
# Follow setup instructions for your environment
# ADB Misconfiguration Scanner

## Overview

This tool is designed to detect Android devices vulnerable to unauthorized access via the Android Debug Bridge (ADB) due to misconfiguration. By scanning for ADB instances that lack proper authentication, security teams can identify and mitigate potential vulnerabilities, safeguarding devices from unauthorized access.

## Features

- **Scan Network**: Rapidly scans the local network for devices with open ADB ports.
- **Misconfiguration Detection**: Identifies devices with ADB configured without authentication, highlighting potential security risks.
- **Comprehensive Reporting**: Generates detailed reports on detected vulnerabilities, facilitating targeted security enhancements.

# Connect to your target

Below are the steps to connect to your target when it doesnt have an Auth method for the ADB protocol.

### Initial Steps

1. **Install adb: sudo apt install adb

1. **Enable ADB listener TCP/IP**:
    - Switch ADB to TCP/IP mode: `adb tcpip 5555

2. **Connect To Target**:
    - Obtain your IP address or target.
    - Connect to your device or target: `adb connect <device-ip-address>:5555`
    - Confirm with `adb devices`.
    - Get shell: `adb shell`

### Security Tips

- **Secure Network**: Use a secure, trusted network for TCP/IP connections.
- **Disable ADB Over Network After Use**: Execute `adb usb` to revert to USB-only mode, closing the TCP/IP connection and enhancing security.
