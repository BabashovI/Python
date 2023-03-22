import smtplib

sender = 'ad_gunu@qwe.com'
receivers = ['qwe']

message = """From: Happy Birthday <ad_gunu@qwe.com>
To: To Person <qwe.qwe@qwe.az>
Subject: Happy Birthday

Dear Vahid
 
"""

try:
    smtpObj = smtplib.SMTP('smtp.qwe.com')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")
