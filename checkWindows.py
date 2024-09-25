import subprocess

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
print(check_wifi_security_windows())

