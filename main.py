import random
import smtplib
print('********  Игра скажи число! ********')
code = random.randint(10000,100000)
coders = input("Напиши свою почту:")
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('botgameentercode@gmail.com','testbot123')
message_text = "your code is " + str(code)
smtpObj.sendmail("botgameentercode@gmail.com",coders,message_text)
cookies = input("Введите код из почты:")
if str(code) == cookies :
    print("Ого! А ты крутой =)!  ")
else:
    print("неверный код! =(")