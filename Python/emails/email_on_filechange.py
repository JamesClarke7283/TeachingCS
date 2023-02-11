import hashlib
import smtplib
import ssl
import time

context = ssl.create_default_context()

SERVER_DOMAIN = "james-clarke.ynh.fr"
FROM_ADDR = "demo@james-clarke.ynh.fr"
TO_ADDR = "james@james-clarke.ynh.fr"
PASSWORD = input("Enter Password:\t")
MESSAGE = "File Was Changed"

prevhash = ""
while True:
    with open("./test", "rb") as f:
        hashfile = hashlib.md5(f.read()).hexdigest()
        if hashfile != prevhash:
            with smtplib.SMTP(SERVER_DOMAIN, 587) as server:
                server.starttls(context=context)
                server.login(FROM_ADDR, PASSWORD)
                server.sendmail(FROM_ADDR, TO_ADDR, msg=MESSAGE)
            print(hashfile)
        time.sleep(2)
        prevhash = hashfile
