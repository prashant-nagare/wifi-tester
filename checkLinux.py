import subprocess

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
print(check_wifi_security_linux())

