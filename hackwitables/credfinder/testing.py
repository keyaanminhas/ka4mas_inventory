import subprocess



command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True, shell= True).stdout.decode()


print(command_output)