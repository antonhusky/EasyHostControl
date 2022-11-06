import helpers

###
### vHosts Dialogs
###

def vhostCreateDialog():
    print("--- vHost creation dialog started ---")
    print("Enter domain name: (EX: domain.zone)")
    domain = input()
    print("Enter domain aliases separated by spaces: (EX: www.domain.zone)")
    aliases = input()
    print("Admin email: (EX: admin@domain.zone)")
    email = input()
    print("Use httpd?: [Y/n] (If no it will use only nginx)")
    use_httpd = helpers.boolQuestion("y")
    print("Use https?: [Y/n] (If no vhost will be available only by http)")
    use_https = helpers.boolQuestion("y")
    print("Use let`s encrypt?: [Y/n] (If no it's generate selfsigned ssl certificate)")
    use_le = helpers.boolQuestion("y")
    vhostCreate(domain, aliases, email, use_httpd, use_https, use_le)

def vhostDeleteDialog():
    print("--- vHost deletion dialog started ---")
    print("Enter domain name: (EX: domain.zone)")
    domain = input()
    print("Save files: [Y/n]")
    save_files = helpers.boolQuestion("y")
    vhostDelete(domain, save_files)

def vhostEnableDialog():
    print("--- vHost enabling dialog started ---")
    vhostToggleDialog("enable")

def vhostDisableDialog():
    print("--- vHost disabling dialog started ---")
    vhostToggleDialog("disable")

def vhostToggleDialog(action):
    print("Enter domain name: (EX: domain.zone)")
    domain = input()
    print("Affect httpd: [Y/n]")
    affect_httpd = helpers.boolQuestion("y")
    print("Affect nginx: [Y/n]")
    affect_nginx = helpers.boolQuestion("y")
    print("Affect certbot: [Y/n]")
    affect_certbot = helpers.boolQuestion("y")
    if action == "enable":
        vhostEnable(domain, affect_httpd, affect_nginx, affect_certbot)
    else:
        vhostDisable(domain, affect_httpd, affect_nginx, affect_certbot)

###
### vHosts actions
###

def vhostCreate(domain, aliases, email, use_httpd, use_https, use_le):
    print("vhostCreate action")
    # ToDo
    pass

def vhostDelete(domain, save_files):
    print("vhostDelete action")
    # ToDo
    pass

def vhostEnable(domain, affect_httpd, affect_nginx, affect_certbot):
    print("vhostEnable action")
    if affect_httpd == 'y':
        # ToDo
        print("affect_httpd")
    if affect_nginx == 'y':
        # ToDo
        print("affect_nginx")
    if affect_certbot == 'y':
        #ToDo
        print("affect_certbot")

def vhostDisable(domain, affect_httpd, affect_nginx, affect_certbot):
    print("vhostDisable action")
    if affect_httpd == 'y':
        # ToDo
        print("affect_httpd")
    if affect_nginx == 'y':
        # ToDo
        print("affect_nginx")
    if affect_certbot == 'y':
        # ToDo
        print("affect_certbot")