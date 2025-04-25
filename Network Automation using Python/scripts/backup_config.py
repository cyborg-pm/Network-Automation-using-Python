from netmiko import ConnectHandler
from datetime import datetime
import os

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

try:
    with ConnectHandler(**device) as net_connect:
        config = net_connect.send_command('show running-config')
        
        # Ensure backups directory exists
        os.makedirs('../backups', exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"../backups/backup_{device['host']}_{timestamp}.txt"
        
        with open(filename, 'w') as file:
            file.write(config)
        print(f"Backup saved to {os.path.abspath(filename)}")
except Exception as e:
    print(f"Error: {e}")