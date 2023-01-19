import colorama
import time
from colorama import *
from discord_webhook import *
import string
import secrets
colorama.init()
user = string.ascii_lowercase + string.digits
pwdd = string.ascii_letters + string.digits
gm = string.ascii_lowercase + string.digits
print(Fore.LIGHTRED_EX+"[-] Loading libraries...")
time.sleep(0.25)
print("[-] Loading dependencies...")
time.sleep(0.15)
print(Fore.LIGHTMAGENTA_EX+"[CRACKED BY POOPOOMAN] Logged in!")	
time.sleep(0.35)
print("Welcome to rapidgmail.")
time.sleep(0.25)
webhook_bruh = input(Fore.LIGHTBLUE_EX+"Enter webhook URL: ")
print("Attaching URL to server...")
time.sleep(0.01)
webhook_conbruh = input("What do you want your webhook to say for a test message? ")
webhook = DiscordWebhook(url=str(webhook_bruh), content=str(webhook_conbruh))
response = webhook.execute()
time.sleep(0.25)
n = 0
x = int(input("How many gmails do you want to generate? "))
while n <= x:
    n = n + 1
    embed_color_pallete = '8b0000', '000000', 'FFFFFF', 'FFA500', 'FFFF00', '00FF00', '000FF', 'A020F0', 'FFC0CB'
    color_pallete = Fore.RED, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX
    bruh = 'Billy', 'Joe', 'Willie', 'Will', 'Bob', 'Bobby', 'Rob', 'Robert', 'Joeson', 'Ryan', 'Wyatt', 'Jessica', 'Louis', 'Eddie', 'Mitch', 'Matthew'
    las = ' Odinson', ' Willson', ' Rose', ' Smith', ' Duggins', ' Witherspoon', ' Taylor', ' Westsmithson', ' Gonzalez'
    color = ''
    for i in range(1):
        color += ''.join(secrets.choice(color_pallete))
    embed_color = ''
    for i in range(1):
        embed_color += ''.join(secrets.choice(embed_color_pallete))
    firstname = ''
    for i in range(1):
        firstname += ''.join(secrets.choice(bruh))
    lastname = ''
    for i in range(1):
        lastname += ''.join(secrets.choice(las))
    name = str(firstname)+str(lastname)
    print(str(color)+"[-] Generated names, now generating gmail name...")
    time.sleep(0.25)
    a = ''
    for i in range(5):
        a += ''.join(secrets.choice(gm))
    b = ''
    for i in range(5):
        b += ''.join(secrets.choice(gm))
    c = ''
    for i in range(5):
        c += ''.join(secrets.choice(gm))
    d = ''
    for i in range(5):
        d += ''.join(secrets.choice(gm))
    e = ''
    for i in range(5):
        e += ''.join(secrets.choice(gm))
    gmail = str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+'.'+str(e)
    print("[-] Generated gmail, now generating password...")
    time.sleep(0.75)
    pwd = ''
    for i in range (99):
        pwd += ''.join(secrets.choice(pwdd))
    print('[-] Sending results to webhook...')
    webhook = DiscordWebhook(url=str(webhook_bruh))
    embed = DiscordEmbed(title='Gmail '+str(n)+' Generated', description='Gmail Name: '+str(name)+'\n\n'+'Gmail: '+str(gmail)+'@gmail.com'+'\n\n'+'Password: '+str(pwd)+'\n\n'+'**rapidgmail by max**', color=str(embed_color))
    webhook.add_embed(embed)
    response = webhook.execute()
if n >= x:
    print(Fore.GREEN+"Gmail generating finished, exiting program in 2 seconds...")
