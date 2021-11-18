import time
import colorama
import ping3
from tkinter import messagebox
print(colorama.Fore.LIGHTBLUE_EX + "*"*20 + "Pinger Made By 26max#6511" + "*"*25)
ip_address = input(colorama.Fore.LIGHTBLUE_EX + "Target IP OR Hostname: ")
count = int(input(colorama.Fore.LIGHTBLUE_EX + "Count of packages"))
package_size = int(input(colorama.Fore.LIGHTBLUE_EX + "Packages Size:"))
print("*" * 80)
count += 1
response = 0
failure = 0
for i in range(1, count):
    time.sleep(1)
    ping_checker = ping3.ping(ip_address, unit="ms", size=package_size)
    ping_checker = round(ping_checker, 0)
    print("*" * 80)
    print(colorama.Fore.LIGHTBLUE_EX + "Target is sending Response with a answer time:" + str(ping_checker) + "ms" + ":Package:" + str(i) + "Package Size:" + str(package_size))
    print("*" * 80)
    if ping_checker > 999:
        print(colorama.Fore.RED + "Target is off or you have a bad connection")
        failure += 1
    if ping_checker < 999:
        response += 1
count -= 1
end_result = response / count * 100
messagebox.showinfo("Ping Result", "Failures Packages = " + str(failure) + '\n' + "Successful Packages = " + str(response) +
                    '\n' + "Response Rate:" + str(end_result) + "%")
print("*"*80)