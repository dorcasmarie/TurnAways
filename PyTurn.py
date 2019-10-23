import email, smtplib, ssl, csv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser
from datetime import date
import pandas as pd


config = configparser.ConfigParser()
config.read('config.ini')
InputCsvFile  = 'TurnAways102019.csv'
OutputCsvFile = 'FlaggedItems.csv'
flaggedNumBook = 5
flaggedNumJournal = 10

#pandas

def ejournal_turnaway(InputCsvFile, OutputCsvFile, flaggedNumJournal):
    csv_reader = pd.read_csv(InputCsvFile, delimiter=',')
    turn_aways = pd.DataFrame()
    for index, row in csv_reader.iterrows():
       if row.Turnaways > flaggedNumJournal:
        turn_aways = turn_aways.append(row)
    turn_aways.to_csv(OutputCsvFile, index=False)

ejournal_turnaway('TurnAways2019.csv', 'ejournal_output.csv', flaggedNumJournal)

#message part



subject = 'E-journal Turnaway ' + str(date.today())

msg = MIMEMultipart()
msg['From'] = config['Outlook']['email']
msg['To'] = config['Outlook']['email']
msg['Subject'] = subject


body = """Hello!

        This email is to inform you that the csv file with turnaways of ejournals is ready.
        Please see the attached file.

        Dorcas Washington """
msg.attach(MIMEText(body, 'plain'))

filename = 'ejournal_output.csv'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet_stream')

part.set_payload((attachment).read())

encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)
msg.attach(part)
text = msg.as_string()


connection = smtplib.SMTP('smtp.uc.edu', 25)
connection.sendmail('washids@uc.edu', 'washids@uc.edu', text)
connection.quit()


