import subprocess
target_dir = ""
target_dir = input("Enter your target directory: ")
targets = subprocess.check_output(['sudo', 'ls', '-aRqp', f'{target_dir}'])
targets_str = targets.decode('utf-8')
target_files = targets_str.split(":")
target_files_dict = {}

for file_list in target_files:
    file_list = file_list.split("\n")
    target_files_dict[file_list[0]] = file_list[1::]

print(target_files_dict)
