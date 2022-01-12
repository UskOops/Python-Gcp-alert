from google.cloud import bigquery
import pandas as pd
import numpy as np
#google_in=bigquery("Your GCP acess key","your Google Associate Tag,"US") preciso corrigir esse erro
#query="SELECT * FROM `bigquery-public-data`"


product=google_in.query("select * from `Your BigQuery Table`")
df=pd.DataFrame(product)
df.columns=['Product','Date','Value']


def send_email(title,no-value):
            import smtplib

            gmail_user = "your gmail id"
            gmail_pwd = "your gmail password"
            FROM = 'Sender email id'
            TO = ['Receiver email id'] #precisa ser uma lista?
            SUBJECT = "No data"
            TEXT = "We not received any data "

            # preparando mensagem
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:
                #server = smtplib.SMTP(SERVER) 
                server = smtplib.SMTP("smtp.gmail.com", 587) #a porta 465 não funciona!
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                server.quit()
                print 'successfully sent the mail'
            except:
                print "failed to send mail"

print no-value.title
value = transactions.value_and_currency[0]
print value
expected_value <= 1 # Enter your expected price

if value<=expected_value:
    message(transactions.title)
    send_email(product.title,value)



