# DroidSniper - Misconfigured Android Debug Bridge Scanner 🎯

This tool, DroidSniper, is designed to detect misconfigured Android Debug Bridge (ADB) protocols on Android devices. These devices are vulnerable to unauthorized access via ADB due to misconfiguration. By scanning for ADB instances lacking proper authentication, security teams can identify and mitigate potential vulnerabilities, safeguarding devices against unauthorized access. 🛡️

## Features 🌟

- **Scan Network**: Rapidly scans networks for devices with open ADB ports. 🔍
- **Misconfiguration Detection**: Identifies devices with ADB configured without authentication, highlighting potential security risks. ⚠️

## Connect to your target 🎯

Below are the steps to connect to your target when it doesn't have an Auth method for the ADB protocol.

### Initial Steps

1. **Install adb**: `sudo apt install adb` 💻

2. **Enable ADB listener TCP/IP**:
    - Switch ADB to TCP/IP mode: `adb tcpip 5555` 🔌

3. **Connect To Target**:
    - Obtain your IP address or target. 🎲
    - Connect to your device or target: `adb connect <device-ip-address>:5555` 🖇️
    - Confirm with `adb devices` ✅
    - Get shell: `adb shell` 🐚

### Security Tips 🔐

- **Secure Network**: Use a secure, trusted network for TCP/IP connections. 🌐
- **Disable ADB Over Network After Use**: Execute `adb usb` to revert to USB-only mode, closing the TCP/IP connection and enhancing security. 🔒

## Disclaimer 📝

The use of the DroidSniper tool should be limited to testing, research, and educational purposes only. I am not responsible for any misuse or damage caused by this tool. Ensure you have explicit permission to test devices and networks with DroidSniper. Unauthorized access to devices and networks is illegal and unethical. 🚫
