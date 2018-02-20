import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("akshathaashu990@gmail.com","Akshatha123")
msg="hi how are you"
s.sendmail("akshathaashu990@gmail.com","anitharathnam.kv@gmail.com",msg)
print("success")
s.quit()
