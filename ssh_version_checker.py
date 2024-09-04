"""
Library: SSH Version Checker
Author: Haluk YAMANER
Email: haluk@halukyamaner.com
Web: https://www.halukyamaner.com
Version: 1.0

Description:
    This script connects to a specified IP address and port (defaulting to 22 for SSH) and retrieves the SSH banner to identify the server's SSH version. It's a simple and efficient way to remotely determine the version of SSH running on a server, which can be useful for both security assessments and general server maintenance.

Usage:
    The script is executed from the command line. The user is prompted to input the IP address and optionally the port number of the target server. The script then attempts to establish a TCP connection, reads the SSH banner, and displays the server's SSH version information if available.

Requirements:
    Python 3.x
    Modules: socket

Features:
    - Connects to a user-specified IP and port to check for SSH service
    - Retrieves and displays the SSH version banner if present
    - Provides feedback on connection issues like timeouts or other network errors
    - Handles invalid user input for IP addresses and port numbers effectively
"""
import socket

def check_ssh_version(ip, port=22):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Set a timeout for the connection
        sock.connect((ip, port))  # Connect to the SSH port
        
        # Read the SSH banner which contains the version information
        banner = sock.recv(1024).decode().strip()
        
        if banner:
            print(f"SSH Banner:")
            print()
            print(f"{ip}:{port}")
            print(f"{banner}")
            print()
        else:
            print(f"No SSH banner detected on {ip}:{port}.")
        
        # Close the connection
        sock.close()
    except socket.timeout:
        print(f"Connection to {ip}:{port} timed out.")
    except socket.error as e:
        print(f"Failed to connect to {ip}:{port}: {str(e)}")

if __name__ == "__main__":
    # Prompt the user for an IP address
    ip_address = input("Please enter the IP address of the target server: ")

    # Validate if the user input is a valid IP address format
    try:
        socket.inet_aton(ip_address)  # Check if it's a valid IP address
    except socket.error:
        print("Invalid IP address format. Please enter a valid IP address.")
        exit(1)

    # Prompt the user for the SSH port, with a default of 22
    try:
        port_input = input("Please enter the SSH port (default is 22): ")
        ssh_port = int(port_input) if port_input else 22  # Default to 22 if no input
    except ValueError:
        print("Invalid port number. Please enter a valid integer.")
        exit(1)

    # Check the SSH version of the server
    check_ssh_version(ip_address, ssh_port)
