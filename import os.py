import os
import subprocess

# c = r"C:\\"
# # os.chdir(r"C:\\")
# subprocess.call(["php", "price_web.php"]);

# print(subprocess.call([r"php C:\Users\jackt\Desktop\price_web.php>"]))

# cmd = ["php", "price_web.php"]
# proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

# script_response = proc.communicate()
# print(script_response)

phpizzle = subprocess.check_output('php price_web.php', shell=True)
print(phpizzle)