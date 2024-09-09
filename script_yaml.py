import yaml
import subprocess

# Load the YAML file
with open("/root/params.yaml", 'r') as file:
    config = yaml.safe_load(file)

# Accessing the values:
eth_ip = config['network_settings']['ros__parameters']['ETH_IP']
eth_netmask = config['network_settings']['ros__parameters']['ETH_NETMASK']
wifi_ssid = config['network_settings']['ros__parameters']['WIFI_SSID']
wifi_pass = config['network_settings']['ros__parameters']['WIFI_PASS']

lw20 = config['payload_settings']['ros__parameters']['LW20']
megaphone = config['payload_settings']['ros__parameters']['MEGAPHONE']
sf45 = config['payload_settings']['ros__parameters']['SF45']
ntrip = config['payload_settings']['ros__parameters']['NTRIP']

# Run the subprocesses using subprocess.call()
# Configure network interface eth0
subprocess.call(['ifconfig', 'eth1', 'inet', eth_ip, 'netmask', eth_netmask])

# Connect to Wi-Fi
subprocess.call(['nmcli', 'dev', 'wifi', 'connect', wifi_ssid, 'password', wifi_pass])

# Manage services based on settings
if lw20:
    subprocess.call(['systemctl', 'enable', 'argosdyne_lidar_lw20'])
    subprocess.call(['systemctl', 'start', 'argosdyne_lidar_lw20'])
else:
    subprocess.call(['systemctl', 'disable', 'argosdyne_lidar_lw20'])

if sf45:
    subprocess.call(['systemctl', 'enable', 'argosdyne_lidar_sf45'])
    subprocess.call(['systemctl', 'start', 'argosdyne_lidar_sf45'])
else:
    subprocess.call(['systemctl', 'disable', 'argosdyne_lidar_sf45'])
