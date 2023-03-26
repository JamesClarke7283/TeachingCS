import subprocess
import os

cd_target = ''
done = False


def find_last(target_dir):
    targets_raw = subprocess.check_output(['sudo', 'ls', '-p', f'{target_dir}'])
    targets_str = targets_raw.decode('utf-8')
    targets = targets_str.split('\n')
    print(targets)
    for target in targets:  # <--------- 'target'
        if '/' in target:
            print("\n-------===FOUND===-------")  # testing
            print(target, end="\n\n")
            return target
        else:
            pass

def cd_dir(cd_target):
    os.chdir(f'{cd_target}')

target_dir = input("Enter your target directory: ")

while done == False:
    cd_target = find_last(target_dir)
    print(cd_target) # testing
    cd_dir(cd_target)
    break