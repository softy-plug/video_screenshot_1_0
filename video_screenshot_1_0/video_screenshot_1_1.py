import os

# Prompt user to choose starting folder
choice = input("Start from current folder? (y/n): ")

if choice.lower() == 'y':
   folder_path = os.getcwd()  # Get the current folder path
else:
   folder_path = input("Enter the folder path: ")

# Verify if the entered folder path is valid
if not os.path.isdir(folder_path):
   print("Invalid folder path!")
else:
   print("Folder path:", folder_path)

input_time = input("Enter the input time: ")  # Added input menu
#input_time = int(input("Enter the input time: "))

def modify_bat_files(folder_path):

for root, _, files in os.walk(folder_path):
   for file_name in files:
       if file_name.endswith(".bat"):
           file_path = os.path.join(root, file_name)
           with open(file_path, 'r') as file:
               lines = file.readlines()

           with open(file_path, 'w') as file:
               for line in lines:
                   if line.startswith('ffmpeg'):
                       line = line.replace('ss 00:00:03', f'ss {input_time}')
                       file.write(line)
                   else:
                       file.write(line)

           print(f"Modified {file_path}")

# folder_path = input("Enter the folder path: ")  # Added input menu
# folder_path = os.getcwd()  # Set the folder_path to current working directory

modify_bat_files(folder_path)

# work in progress

# softy_plug