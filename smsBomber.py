import smtplib

#Set gmail username and password
GMAIL_USERNAME = 'emample@gmail.com'
GMAIL_PASSW = 'example'

#message send method
def sendMessage(sender, receiver, message):
    try:
        smtpserver = smtplib.SMTP('smtp.gmail.com',587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.login(GMAIL_USERNAME, GMAIL_PASSW)
        smtpserver.sendmail(sender, receiver, '\r' + message)
        smtpserver.close()
        print ('Successfully sent email')
    except Exception:
        print ('Error: unable to send email')

#Enter message recipients' numbers here
receivers = []
#Enter message to send
message = 'ENTER MESSAGEG HERE'
#Enter amount to send
numberToSend = 100

for _ in range(0,numberToSend):
    for receiver in receivers:
        sendMessage(GMAIL_USERNAME, receiver, message)
