import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("fanofbitlalpur@gmail.com", "jaishreeram123@")
message = "Hi ashutosh your model is ready and giving best accuracy"
s.sendmail("fanofbitlalpur@gmail.com", "anandashutosh803@gmail.com", message)
print("Mail Sent")
s.quit() 
