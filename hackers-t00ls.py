#################################################--import libraries and install if not installed--#################################################
import subprocess, platform, random, string, time, sys, os, re, smtplib
try:
    import pyfiglet, json, pprint, whois, pyperclip, requests as rq, pyshorteners as ps, scapy.all as scapy, netifaces
except ModuleNotFoundError:
    installing = input("is pip or pip3 installed?(pip/pip3)")
    print("modules are not installed")
    os.system(installing+" install netifaces pyfiglet pyperclip requests python-whois scapyw pyshorteners==1.0.1")
    print("Got An Error?, restart the program!")

import pyfiglet
if platform.system() == 'Windows':
    os.system("cls")
else:
    os.system("clear")

ascii_banner = pyfiglet.figlet_format("hackers-t00ls")
print(ascii_banner)
print("					By CxllZ")

ans=True
while ans:
    print ("""
    Make sure to turn off VPN, if using Nmap options\n    and make sure your connected to Internet for other options!\n    If You Get An Import Error Try Running The Script Again
    1. Geo Ip Lookup
    2. Port scan (NMAP)
    3. Url Backtracer
    4. Url shortener
    5. Whois
    6. SQLI Scanner (NMAP)
    7. WAF(WEB APP FIREWALL) Detection (NMAP)
    8. Temp Mail
    9. Email Bomber
    10. Password Gen
    11. Network Scanner(RESTART THE SCRIPT AS ROOT/SUDO OR ADMINISTRATOR)
    12. Exit
    """)
    ans=input("Choose Your T00l: ") 
    if ans=="1":
#################################################--GEO IP LOOKUP--#################################################
        import urllib.request
        if platform.system() == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(ascii_banner)
        print("					By CxllZ")
        ip = input("Enter Ip -->: ")
        url1 = "http://ip-api.com/json/"+ip+"?fields=mobile,proxy,hosting"
        url2 = "http://ipwhois.app/json/"+ip
        response2 = urllib.request.urlopen(url2) 
        response1 = urllib.request.urlopen(url1)
        data2 = response2.read()
        data1 = response1.read()
        values2 = json.loads(data2)
        values1 = json.loads(data1)
        print("NOT ACCURATE AS ALWAYS!")
        pprint.pprint(values1)
        pprint.pprint(values2)
        print("NOT ACCURATE AS ALWAYS!")
    elif ans=="2":
#################################################--NMAP PORT SCAN AND SET NMAP TO PATH--#################################################
        if platform.system() == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(ascii_banner)
        print("					By CxllZ")
        answer = None 
        while answer not in ("yes", "no"):
            print("Do You Have Nmap Installed?")
            answer = input("Enter yes or no: ") 
            if answer == "yes": 
                if platform.system() == 'Windows':
                    set_path = 'setx PATH "%PATH%;C:\\Program Files (x86)\\Nmap"'
                    os.system(set_path)
                    print("Finished Setting Nmap To PATH")
                    print("If you get an error open another cmd/terminal and execute python script")
                    ip = input("Enter IP To port Scan -->: ")
                    print ("nmap is scanning ip for ports please be patient")
                    print("Waiting for too long?, hit any key")
                    print ()
                    subprocess.call(['nmap', ip])
                    print("If No Results It Has No Open Ports!")
                else:
                    print("If you get an error open another cmd/terminal and execute python script")
                    ip = input("Enter IP To port Scan -->: ")
                    print ("nmap is scanning ip for ports please be patient")
                    print("Waiting for too long?, hit any key")
                    print ()
                    subprocess.call(['nmap', ip])
                    print("If No Results It Has No Open Ports!")
            elif answer == "no":
                print("")
                print("Install Nmap Here!:")
                print("Windows: https://nmap.org/dist/nmap-7.91-setup.exe")
                print("Mac Os: https://nmap.org/dist/nmap-7.91.dmg")
            else: 
    	        print("Please enter yes or no.") 
    elif ans=="3":
#################################################--URL BACKTRACER--#################################################
        from urllib.request import urlopen
        if platform.system() == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(ascii_banner)
        print("					By CxllZ")
        link = input("Enter Url Here -->: ")
        a = urlopen(link)
        print()
        print("Short Url Goes To:",  a.url)
    elif ans=="4":
#################################################--URL SHORTENER--#################################################
        if platform.system() == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(ascii_banner)
        print("					By CxllZ")
        link = input("Enter Url You Wish To Shorten -->: ")
        output = ps.Shortener().tinyurl.short(link)
        print(output)
    elif ans=="5":
#################################################--URL WHOIS--#################################################
        if platform.system() == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(ascii_banner)
        print("					By CxllZ")
        host = input("Enter Url To Whois(example.com) -->: ")
        print("Got An Error Try Running pip uninstall whois\n then pip install python-whois")
        print(whois.whois(host))
    elif ans=="6":
######################################--SQLI SCANNER--#################################################
        if platform.system() == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(ascii_banner)
        print("					By CxllZ")
        print("Do You Have Nmap Installed?")
        answer1 = input("Enter yes or no: ") 
        if answer1 == "yes": 
            if platform.system() == 'Windows':
                set_path = 'setx PATH "%PATH%;C:\\Program Files (x86)\\Nmap"'
                os.system(set_path)
                print("Finished Setting Nmap To PATH")
                print("If you get an error open another cmd/terminal and execute python script")
                w = input("Enter Top-Level-Domain Url To SQLI Scan(example.com) -->: ")
                print ("nmap is scanning website for SQLI please be patient")
                print("Waiting for too long?, hit any key")
                print ()
                subprocess.call(['nmap', '--script', 'http-sql-injection', w])
                print("If No Results It Has No SQLI Vulnerabilites")
            else:
                print("If you get an error open another cmd/terminal and execute python script")
                w = input("Enter  Top-Level-Domain Url To SQLI Scan(example.com) -->: ")
                print ("nmap is scanning website for SQLI please be patient")
                print("Waiting for too long?, hit any key")
                print ()
                subprocess.call(['nmap', '--script', 'http-sql-injection', w])
                print("If No Results It Has No SQLI Vulnerabilites")
        elif answer1 == "no":
            print("")
            print("Install Nmap Here!:")
            print("Windows: https://nmap.org/dist/nmap-7.91-setup.exe")
            print("Mac Os: https://nmap.org/dist/nmap-7.91.dmg")
        else: 
    	    print("Please enter yes or no.")
    elif ans=="7":
######################################--WAF(WEB APP FIREWALL) DETECTOR--#################################################
        if platform.system() == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(ascii_banner)
        print("					By CxllZ")
        print("Do You Have Nmap Installed?")
        answer2 = input("Enter yes or no: ") 
        if answer2 == "yes": 
            if platform.system() == 'Windows':
                set_path = 'setx PATH "%PATH%;C:\\Program Files (x86)\\Nmap"'
                os.system(set_path)
                print("Finished Setting Nmap To PATH")
                print("If you get an error open another cmd/terminal and execute python script")
                w = input("Enter Top-Level-Domain Url To WAF Detect(example.com) -->: ")
                print ("nmap is scanning url for waf's please be patient")
                print("Waiting for too long?, hit any key")
                subprocess.call(['nmap', '--script', 'http-waf-detect,http-waf-fingerprint', w])
                print("If No Results It Has No WAF")
            else:
                print("If you get an error open another cmd/terminal and execute python script")
                w = input("Enter Top-Level-Domain Url To WAF Detect(example.com) -->: ")
                print ("nmap is scanning url for waf's please be patient")
                print("Waiting for too long?, hit any key")
                print ()
                subprocess.call(['nmap', '--script', 'http-waf-detect,http-waf-fingerprint', w])
                print("If No Results It Has No WAF")
        elif answer2 == "no":
            print("")
            print("Install Nmap Here!:")
            print("Windows: https://nmap.org/dist/nmap-7.91-setup.exe")
            print("Mac Os: https://nmap.org/dist/nmap-7.91.dmg")
        else: 
    	    print("Please enter yes or no.")
    elif ans=="8":
######################################--TEMP-FAKE MAIL--#################################################
        import requests
        API = 'https://www.1secmail.com/api/v1/'
        domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
        domain = random.choice(domainList)
        def generateUserName():
            name = string.ascii_lowercase + string.digits
            username = ''.join(random.choice(name) for i in range(10))
            return username
        def extract():
            getUserName = re.search(r'login=(.*)&',newMail).group(1)
            getDomain = re.search(r'domain=(.*)', newMail).group(1)
            return [getUserName, getDomain]
        def print_statusline(msg: str):
            last_msg_length = len(print_statusline.last_msg) if hasattr(print_statusline, 'last_msg') else 0
            print(' ' * last_msg_length, end='\r')
            print(msg, end='\r')
            sys.stdout.flush()
            print_statusline.last_msg = msg
        def checkMails():
            reqLink = f'{API}?action=getMessages&login={extract()[0]}&domain={extract()[1]}'
            req = requests.get(reqLink).json()
            length = len(req)
            if length == 0:
                print_statusline("Your mailbox is empty. Hold tight. Mailbox is refreshed automatically every 5 seconds.")
            else:
                idList = []
                for i in req:
                    for k,v in i.items():
                        if k == 'id':
                            mailId = v
                            idList.append(mailId)
                x = 'mails' if length > 1 else 'mail'
                print_statusline(f"You received {length} {x}. (Mailbox is refreshed automatically every 5 seconds.)")
                current_directory = os.getcwd()
                final_directory = os.path.join(current_directory, r'All Mails')
                if not os.path.exists(final_directory):
                    os.makedirs(final_directory)
                for i in idList:
                    msgRead = f'{API}?action=readMessage&login={extract()[0]}&domain={extract()[1]}&id={i}'
                    req = requests.get(msgRead).json()
                    for k,v in req.items():
                        if k == 'from':
                            sender = v
                        if k == 'subject':
                            subject = v
                        if k == 'date':
                            date = v
                        if k == 'textBody':
                            content = v
                    mail_file_path = os.path.join(final_directory, f'{i}.txt')
                    with open(mail_file_path,'w') as file:
                        file.write("Sender: " + sender + '\n' + "To: " + mail + '\n' + "Subject: " + subject + '\n' + "Date: " + date + '\n' + "Content: " + content + '\n')
        newMail = f"{API}?login={generateUserName()}&domain={domain}"
        reqMail = requests.get(newMail)
        mail = f"{extract()[0]}@{extract()[1]}"
        pyperclip.copy(mail)
        print("\nYour temporary email is " + mail + " (Email address copied to clipboard.)" + "\n")
        print(f"Inbox of {mail}\n")
        while True:
            checkMails()
            time.sleep(5)
    elif ans=="9":
######################################--EMAIL BOMBER--#################################################
        print("Use a fake gmail acc to bomb and u must have support for 'less secure apps' set to 'turn on' on your Gmail. Here is the link to do so: https://www.google.com/settings/security/lesssecureapps")
        email_provider = 'smtp.gmail.com'
        email_address = input("Enter Attackers Gmail(Gmail ur using to bomb the vitim) -->: ")
        password = input("Enter Your Gmail Password(Gmail Password ur using to bomb the victim) -->: ")
        target_email = input("Enter Target email -->: ")
        msg = input("Enter your email message -->: ")
        email_amount = int(input("Enter your amount of email's -->: "))
        server = smtplib.SMTP(email_provider, 587)
        server.starttls()
        server.login(email_address, password)
        for _ in range(0,email_amount):
            server.sendmail(email_address,target_email,msg)
            print("sent!")
            time.sleep(1)
        print("sent {} emails. :)".format(email_amount))
        server.quit()
    elif ans=="10":
######################################--PASSWORD GEN--#################################################
        if platform.system() == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(ascii_banner)
        print("					By CxllZ")
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
        lowercase_letters = uppercase_letters.lower()
        digits = "0123456789"
        symbols = "!@£$%&?:<>"
        uppercheck = input("Do You Want To Include Upper Letters?(y/n): ")
        if uppercheck == 'y':
            upper = True
        else:
            upper = False
        lowercheck = input("Do You Want To Include Lower Letters?(y/n): ")
        if lowercheck == 'y':
            lower = True
        else:
            lower = False
        numcheck = input("Do You Want To Include Numbers?(y/n): ")
        if numcheck == 'y':
            nums = True
        else:
            nums = False
        symscheck = input("Do You Want To Include Symbols?(y/n): ")
        if symscheck == 'y':
            syms = True
        else:
            syms = False
        all = ""
        if upper:
            all += uppercase_letters
        if lower:
            all += lowercase_letters
        if nums:
            all += digits
        if syms:
            all += symbols
        choose_length = int(input("Enter Your Desired Length Of Passwords: "))
        choose_amount = int(input("Enter Your Desired Amount Of Passwords: "))
        length = choose_length
        amount = choose_amount
        for x in range(amount):
            password = "".join(random.sample(all, length))
            print(password)
######################################--NET SCANNER--#################################################
    elif ans=="11":
        def scan(ip):
            arp_req_frame = scapy.ARP(pdst = ip)

            broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
            
            broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

            answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 0.5, verbose = False)[0]
            result = []
            for i in range(0,len(answered_list)):
                client_dict = {"ip" : answered_list[i][1].psrc, "mac" : answered_list[i][1].hwsrc}
                result.append(client_dict)

            return result
        
        def display_result(result):
            print("-----------------------------------\nIP Address\tMAC Address\n-----------------------------------")
            for i in result:
                print("{}\t{}".format(i["ip"], i["mac"]))

        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][0]
        scanned_output = scan(default_gateway+"/24")
        display_result(scanned_output)
    elif ans=="12":
######################################--EXIT--#################################################
        exit()
    elif ans !="":
        print("\n Not A Valid Choice Try again") 
