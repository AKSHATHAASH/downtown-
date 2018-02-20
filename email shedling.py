import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("Akshatha.17cs@gmail.com","Akshathaakash7")
msg="hi how are you"
s.sendmail("Akshatha.17cs@gmail.com","achuthk99@gmail.com",msg)
print("success")
s.quit()
