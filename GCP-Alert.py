from google.cloud import bigquery
import pandas as pd
import numpy as np
google_in=bigquery("Your GCP acess key","your Google Associate Tag,"US") 
#info gcp
query="SELECT * FROM `bigquery-public-data`" #query


product=google_in.query("select * from `Your BigQuery Table`") #precisa ser uma lista?
df=pd.DataFrame(product) #transforma em dataframe
df.columns=['Product','Date','Value'] #colunas


def send_email(title,no-value): 
            import smtplib

            gmail_user = "your gmail id"
            gmail_pwd = "your gmail password"
            FROM = 'Sender email id'
            TO = ['Receiver email id'] #precisa ser uma lista
            SUBJECT = "No data" #
            TEXT = "We not received any data " 

            # preparando mensagem
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s  
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT) 
            try:
                server = smtplib.SMTP(SERVER) #servidor smtp
                server = smtplib.SMTP("smtp.gmail.com", 587) #587 porta padrão
                server.ehlo() 
                server.starttls() #inicia sessão com TLS
                server.login(gmail_user, gmail_pwd) #login
                server.sendmail(FROM, TO, message) #envia email
                server.quit() #fecha sessão
                print 'successfully sent the mail' #mensagem de sucesso
            except:
                print "failed to send mail" #mensagem de erro

print no-value.title #titulo
value = transactions.value_and_currency[0] #valor
print value
expected_value <= 1 # Enter your expected price

if value<=expected_value: #se o valor for menor que o esperado
    message(transactions.title) #envia email
    send_email(product.title,value) #envia email



