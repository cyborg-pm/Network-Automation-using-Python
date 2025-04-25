from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',  # Replace with your device IP
    'username': 'admin',
    'password': 'password',
}

vlans = [
    'vlan 10',
    'name Engineering',
    'vlan 20',
    'name HR',
]

try:
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_config_set(vlans)
        print("VLANs configured successfully:\n", output)
except Exception as e:
    print(f"Error: {e}")