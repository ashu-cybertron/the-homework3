import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("fanofbitlalpur@gmail.com", "jaishreeram123@")
message = "Hey developer the file committed by you for training model has some flaws due to which accuracy of model is not good so some tweaks are automatically done to get better accuracy of model"
s.sendmail("fanofbitlalpur@gmail.com", "anandashutosh803@gmail.com", message)
print("Mail Sent")
s.quit() 
