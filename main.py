import sys
import os

def testDialog():
    print("get test")
    test1 = input()
    print(test1)
    return

def mainMenu():
    print('''
Choose action:
1. Create vHost
2. Delete vHost
3. Enable vHost
4. Disable vHost
0. Close
''')
    action = input()
    match action:
        case "1":
            vhostCreateDialog()
        case "2":
            vhostDeleteDialog()
        case "3":
            vhostEnableDialog()
        case "4":
            vhostDisableDialog()
        case "0":
            exit()
        case _:
            mainMenu()
    return

def vhostCreateDialog():
    print("--- vHost creation dialog started ---")
    print("Enter domain name: (EX domain.zone)")
    domain = input()
    print("Enter domain aliases separated by spaces: (EX: www.domain.zone)")
    aliases = input()
    print("Use https?: (Y/n)")
    use_https = boolQuestion("y")
    print("Use let`s encrypt?: (Y/n)")
    use_le = boolQuestion("y")
    vhostCreate(domain, aliases, use_https, use_le)
    mainMenu()
    return

def vhostCreate(domain, aliases, use_https, use_le):
    print("vhostCreate action")
    # ToDo
    return

def vhostDeleteDialog():
    print("--- vHost deletion dialog started ---")
    print("Enter domain name: (EX domain.zone)")
    domain = input()
    vhostDelete(domain)
    mainMenu()
    return

def vhostDelete(domain):
    print("vhostDelete action")
    # ToDo
    return

def vhostEnableDialog():
    print("--- vHost enabling dialog started ---")
    vhostToggle("enable")
    mainMenu()
    return

def vhostDisableDialog():
    print("--- vHost disabling dialog started ---")
    vhostToggle("disable")
    mainMenu()
    return

def vhostToggle(action):
    print("Enter domain name: (EX domain.zone)")
    domain = input()
    print("Affect httpd: (Y/n)")
    affect_httpd = boolQuestion("y")
    print("Affect nginx: (Y/n)")
    affect_nginx = boolQuestion("y")
    print("Affect certbot: (Y/n)")
    affect_certbot = boolQuestion("y")
    if action == "enable":
        vhostEnable(domain, affect_httpd, affect_nginx, affect_certbot)
    else:
        vhostDisable(domain, affect_httpd, affect_nginx, affect_certbot)
    return

def vhostEnable(domain, affect_httpd, affect_nginx, affect_certbot):
    print("vhostEnable action")
    # ToDo
    return

def vhostDisable(domain, affect_httpd, affect_nginx, affect_certbot):
    print("vhostDisable action")
    # ToDo
    return

def boolQuestion(default):
    inputRes = input()
    match inputRes:
        case "y":
            res = "y"
        case "Y":
            res = "y"
        case "n":
            res = "n"
        case "N":
            res = "n"
        case "":
            res = default
        case _:
            print("Please answer \"Y\" or \"N\"")
            res = boolQuestion(default)
    return res

mainMenu()