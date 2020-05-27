import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("email@gmail.com", "password")
message = "Hey developer the file committed by you for training model has some flaws due to which accuracy of model is not good so some tweaks are automatically done to get better accuracy of model"
s.sendmail("email@gmail.com", "reciever@gmail.com", message)
print("Mail Sent")
s.quit() 
