import helpers
import install
import vhosts

def configure():
    #ToDo
    return

def mainMenu():
    print('''
Choose action:
1. Create vHost
2. Delete vHost
3. Enable vHost
4. Disable vHost
8. Configure
9. Install packages
0. Close
''')
    action = input()
    match action:
        case "0":
            exit()
        case "1":
            vhosts.vhostCreateDialog()
            mainMenu()
        case "2":
            vhosts.vhostDeleteDialog()
            mainMenu()
        case "3":
            vhosts.vhostEnableDialog()
            mainMenu()
        case "4":
            vhosts.vhostDisableDialog()
            mainMenu()
        case "8":
            #ToDo
            mainMenu()
        case "9":
            install.installPackagesDialog()
            mainMenu()
        case "t":
            helpers.isPlatformSupported()
            helpers.getPlatform()
        case _:
            mainMenu()
    return

def main():
    # ToDo: config loader
    is_config_loaded = 'y'
    if is_config_loaded == 'y':
        mainMenu()
    else:
        mainMenu()
    return

main()
