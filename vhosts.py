import helpers

###
### vHosts Dialogs
###


def vhostCreateDialog():

    ''' vHost creation dialog '''

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

    vhostCreate(domain, aliases, email, use_https, use_le)
    return


def vhostDeleteDialog():

    ''' vHost deletion dialog '''

    print("--- vHost deletion dialog started ---")

    print("Enter domain name: (EX: domain.zone)")
    domain = input()
    print("Save files: [Y/n]")
    save_files = helpers.boolQuestion("y")
    vhostDelete(domain, save_files)
    return

def vhostEnableDialog():

    ''' vHost enabling dialog '''

    print("--- vHost enabling dialog started ---")

    vhostToggleDialog("enable")
    return

def vhostDisableDialog():

    ''' vHost disabling dialog '''

    print("--- vHost disabling dialog started ---")

    vhostToggleDialog("disable")
    return

def vhostToggleDialog(action):

    ''' vHost toggle dialog '''

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
    return

###
### vHosts actions
###

def vhostCreate(domain, aliases, use_https, use_le):

    ''' vHost creation '''

    print("vhostCreate action")
    # ToDo
    return

def vhostDelete(domain, save_files):

    ''' vHost deletion '''

    print("vhostDelete action")
    # ToDo
    return

def vhostEnable(domain, affect_httpd, affect_nginx, affect_certbot):

    ''' vHost enabling '''

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
    return

def vhostDisable(domain, affect_httpd, affect_nginx, affect_certbot):

    ''' vHost disabling '''

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
    return