#[!] DISCLAIM-R: performing hacking attempts on computers that you do not own (without permission) is illegal!

# import python libraries
import socket
import sys
from termcolor import colored, cprint



# create scan function
def scan(target, ports):
    print(f"\n Starting Scan for host {target}")
    for port in range(1, ports):
        scan_port(target, port)

# create scan port function
def scan_port(ip_address, port):
    if save_report == 'Y':
        with open(f'{ip_address}_report.txt', 'a+') as report_file:

            try:
                    # initiate socket objects
                    sock = socket.socket()
                    sock.connect((ip_address, port))

                    # if open port, print OPEN statement
                    cprint(f"[-] Port {str(port)}: OPEN", "green")
                    report_file.write(f"\n [-] Host {ip_address} Port {str(port)}: OPEN")
                    # close socket object
                    sock.close()

            except:
                    # print all ports for verbose report
                    if report_detail == 1:
                        pass  # if want a concise report with only OPEN ports

                    elif report_detail == 2:
                        cprint(f"[-] Port {str(port)}: CLOSED", "red")
                        report_file.write(f"\n [-] Host {ip_address} Port {str(port)}: CLOSED")
    else:
        try:
            # initiate socket objects
            sock = socket.socket()
            sock.connect((ip_address, port))

            # if open port, print OPEN statement
            cprint(f"[-] Port {str(port)}: OPEN", "green")

            # close socket object
            sock.close()
        except:
            # print all ports for verbose report
            if report_detail == 1:
                pass  # if want a concise report with only OPEN ports

            else:
                cprint(f"[-] Port {str(port)}: CLOSED", "red")

# print banner
print('''
                                                                                                       
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗      ██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║      ██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║█████╗██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║╚════╝██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║      ██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝      ╚═╝  ╚═╝                                                                                      
                                                                                                       
port scan-r v.1. ethical hacking tool - for educational purposes ONLY

[!] DISCLAIM-R: performing hacking attempts on computers that you do not own (without permission) is illegal!
''')

# create target, ports & report detail variables from user inputs
targets = input("[*] Enter target host ip addresses to scan separated by commas (e.g. X.X.X.X, X.X.X.X): ")
port = int(input("[*] Enter number of ports to scan: "))
ports = port + 1
report_detail = int(input("[*] Report detail options: Type [1] for OPEN ports only OR [2] for all ports: "))
save_report = input("Save report? (Type Y/N) ")

# if comma separated values present, scan multiple ports
if ',' in targets:
    print("[*] Scanning multiple targets")
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '), ports)

else:
    print(f"[*] Scanning host {targets}")
    scan(targets, ports)
