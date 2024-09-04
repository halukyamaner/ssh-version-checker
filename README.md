# SSH Version Checker

## Overview
SSH Version Checker is a Python script designed to determine the version of SSH running on a remote server by capturing the SSH banner. This utility is useful for network administrators and security professionals who need to audit or verify SSH configurations on servers.

## Features
- **SSH Banner Retrieval**: Connects to a specified IP and port to retrieve and display the SSH banner, which includes the version information.
- **Customizable Port Settings**: Allows users to specify the SSH port, defaulting to port 22.
- **Timeout and Error Handling**: Manages connections effectively with timeouts and clear error messages for common network issues.

## Requirements
- Python 3.x
- `socket` module from Python's standard library

## Usage
To check the SSH version on a server, run the script from the command line. You will be prompted to enter the IP address and the SSH port of the target server.

```bash
python ssh_version_checker.py
