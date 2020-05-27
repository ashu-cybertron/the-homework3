import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("email@gmail.com", "password")
message = "Hi ashutosh your model is ready and giving best accuracy"
s.sendmail("email@gmail.com", "reciever@gmail.com", message)
print("Mail Sent")
s.quit() 
