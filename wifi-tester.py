#!/usr/bin/env python
# v0.1-Alpha Script to Test & Harden connected wifi

import os
import subprocess
import platform
import sys
import time
import threading

def print_logo():
    print(' ')
    print('██╗    ██╗██╗███████╗██╗   ████████╗███████╗███████╗████████╗███████╗██████╗ ')
    print('██║    ██║██║██╔════╝██║   ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗')
    print('██║ █╗ ██║██║█████╗  ██║█████╗██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝')
    print('██║███╗██║██║██╔══╝  ██║╚════╝██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗')
    print('╚███╔███╔╝██║██║     ██║      ██║   ███████╗███████║   ██║   ███████╗██║  ██║')
    print(' ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝      ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝')
    print('                                                                By @Reaperg0d')
    print(' ')
    print('>>> Simple python script to determine if Connected WIFI needs any hardning. <<< ')
    print('\n')

# Call print logo function
#print(print_logo())

def detect_os():
    os_name = platform.system()
    if os_name == "Windows":
        return "DETECTED HOST OS = Windows."
    elif os_name == "Linux":
        return "DETECTED HOST OS = Linux."
    elif os_name == "Darwin":
        return "DETECTED HOST OS = macOS."
    else:
        return f"DETECTED HOST OS = Operating system unrecognized : {os_name}"

# Spinner animation function
def loading_spinner():
    spinner = ['|', '/', '-', '\\']
    for _ in range(20):  # Run for 20 iterations
        for symbol in spinner:
            sys.stdout.write(f'\r{symbol} Processing...')  # Overwrite the line
            sys.stdout.flush()
            time.sleep(0.2)  # Delay to make it visible    
    
    
# Call the function
# print(detect_os())

def print_menu():
    print("Please choose an option:\n")
    print("1 - Scan")
    print("2 - Full target scan")
    print("3 - Custom scan")
    print("EE - Exit")

def scan():
    print("Performing Scan1...")
    # Replace with the actual scan command
    # subprocess.run(['your_scan_command'])
    try:
        result = subprocess.run(['echo', 'nmap --help'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Scan failed with error: {e.stderr}")

def full_target_scan():
    print("Performing Full Target Scan...")
    # Replace with the actual full target scan command
    # subprocess.run(['your_full_target_scan_command'])
    print("Full Target Scan completed.")

def custom_scan():
    print("Performing Custom Scan...")
    # Replace with the actual custom scan command
    # subprocess.run(['your_custom_scan_command'])
    print("Custom Scan completed.")

################################################
# Function to check security for Linux Hosts ##
##############################################
def check_wifi_security_linux():
    try:
        # Run the command to get Wi-Fi network details
        output = subprocess.check_output(["nmcli", "-t", "-f", "active,ssid,security", "dev", "wifi"], encoding="utf-8")
        
        # Find the active connection and check its security
        for line in output.splitlines():
            if "yes" in line:  # "yes" indicates the active connection
                if "WPA" in line or "WEP" in line:
                    return "The Wi-Fi network is secured."
                else:
                    return "The Wi-Fi network is open."
        return "No active Wi-Fi connection found."
    except subprocess.CalledProcessError as e:
        return f"Failed to retrieve Wi-Fi details: {e}"

# Call the function
#print(check_wifi_security_linux())


##################################################
# Function to check security for Windows Hosts ##
################################################

def check_wifi_security_windows():
    try:
        # Run the command to get Wi-Fi network details
        output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"], encoding="utf-8")
        
        # Check if the encryption type is present in the output
        if "WPA" in output or "WEP" in output:
            return "The Wi-Fi network is secured."
        else:
            return "The Wi-Fi network is open."
    except subprocess.CalledProcessError as e:
        return f"Failed to retrieve Wi-Fi details: {e}"

# Call the function
#print(check_wifi_security_windows())


##############################################
# Function to check security for MAC Hosts ##
############################################


def check_wifi_security_mac():
    try:
        # Run the `airport` command to get Wi-Fi information
        output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"], encoding="utf-8")
        
        # Check for the presence of encryption in the output
        if "WPA" in output or "WEP" in output:
            return "The Wi-Fi network is secured."
        elif "none" in output:
            return "The Wi-Fi network is open."
        else:
            return "Unable to determine Wi-Fi security status."
    except subprocess.CalledProcessError as e:
        return f"Failed to retrieve Wi-Fi details: {e}"

# Call the function
#print(check_wifi_security_mac())


def get_wifi_ssid_linux():
    try:
        # Run the nmcli command to get Wi-Fi connection details
        output = subprocess.check_output(['nmcli', '-t', '-f', 'active,ssid', 'dev', 'wifi'], encoding='utf-8')
        
        # Find the active connection and return its SSID
        for line in output.splitlines():
            if line.startswith('yes:'):
                return line.split(":")[1]
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"
    
def main():
    # Call spinner animation
    loading_spinner()
    print("\nDone!")
    
    # Call print logo function
    print(print_logo())
    
    # Call the function to detect Host OS
    print(detect_os())

    # Call the function
    print(f"Connected SSID: {get_wifi_ssid_linux()}")

    
"""
    while True:
        print_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                scan()
            elif choice == 2:
                full_target_scan()
            elif choice == 3:
                custom_scan()
            elif choice == E:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
"""

if __name__ == "__main__":
    main()