import subprocess

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

# Call the function
print(f"Connected SSID: {get_wifi_ssid_linux()}")

