import subprocess
import getpass

# Demonstrates how to use subprocess to run a command with sudo
def quick_format(device):
    password = getpass.getpass(prompt='Password: ')
    command = ['mkfs.ext4', '-F', device]
    print(f"Formatting {device}")
    p = subprocess.Popen(['sudo', '-S', '-p', '']+command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate(input=password.encode() + b'\n')

    if p.returncode == 0:
        print(stdout.decode())
        print(f"Successfully formatted {device}")
    else:
        print(stderr.decode())


device = input("Enter device to format: (e.g. /dev/sda1): ")
quick_format(device)
