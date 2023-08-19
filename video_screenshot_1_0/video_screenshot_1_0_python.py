import os

bat_files = [f for f in os.listdir('.') if f.endswith('.bat')]

print("Select the number corresponding to the batch file you want to run:")
for i, f in enumerate(bat_files):
    print(f"{i+1}. {f}")

choice = int(input("Enter selection number: "))
if choice in range(1, len(bat_files)+1):
    os.system(f"{os.getcwd()}\\{bat_files[choice-1]}")
else:
    print("Invalid selection")
    input("Press Enter to exit")

# softy_plug