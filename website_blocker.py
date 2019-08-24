import platform
def block_function():
    content = file.read()
    if website_domain_name not in content:
        file.write(redirect_ip + " " + website_domain_name + "\n" )
    print("Status : {} is now blocked").format(website_domain_name)

def unblock_function():
    file_reset = 250
    file.truncate(file_reset)
    print("Status : Facebook is now unblocked")

def stat_check():
    content = file.read()
    if website_domain_name in content:
        print("{} is already blocked.").format(website_domain_name)
        command = input("Press U to unblock\nPress B to remain blocked\n")
    if website_domain_name not in content:
        print("{} is currently unblocked.").format(website_domain_name)
        command = input("Press B to block\nPress U to remain unlocked\n")

    if (command == "B") or (command == "b"):
        block_function()

    if (command == "U") or (command == "u"):
        unblock_function()

#driver code
host_file = r"/etc/hosts"
redirect_ip = "127.0.0.1"
website_domain_name = "www.facebook.com"
with open(host_file,'r+') as file:
    content = file.read()
    #block_function()
    #unblock_function()
    stat_check()
