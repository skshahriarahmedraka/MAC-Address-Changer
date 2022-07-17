import subprocess

interface="wlan0"
mac="22:11:22:11:11:22"

subprocess.call(f"sudo ifconfig {interface} down",shell=True)
subprocess.call(f"sudo ifconfig {interface} hw ether {mac}",shell=True)
subprocess.call(f"sudo ifconfig {interface} up",shell=True)
subprocess.call(f"sudo ifconfig",shell=True)

