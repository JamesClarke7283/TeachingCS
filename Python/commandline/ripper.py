import subprocess
import getpass

# Demonstrates how to use subprocess to run a command with sudo


def run_sudo_cmd(command):
    password = getpass.getpass(prompt='Password: ')
    p = subprocess.Popen(['sudo', '-S', '-p', '']+command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate(input=password.encode() + b'\n')

    if p.returncode == 0:
        print(stdout.decode())
    else:
        print(stderr.decode())


def shred(dev):
    print(f"Formatting {dev}")
    run_sudo_cmd(['mkfs.ext4', '-F', dev])
    print(f"Done quick formatting {dev}")
    run_sudo_cmd(['dd', 'if=/dev/zero', f'of={dev}', 'status=progress'])
    print(f"Done zeroing out {dev}")


device = input("Enter device to format: (e.g. /dev/sda1): ")
shred(device)
