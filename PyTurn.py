import csv
import configparser
config = configparser.ConfigParser()
import time
InputCsvFile  = 'TurnAways2019.csv'
OutputCsvFile = 'FlaggedItems.csv'
flaggedNumBook = 5
flaggedNumJournal = 10
def processCsvTA(InputCsvFile, OutputCsvFile, flaggedNumBook):
    with open(InputCsvFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        turn_flag = flaggedNumBook
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
                myFile = open(OutputCsvFile, 'w')
                with myFile:
                    writer = csv.writer(myFile, delimiter=',')
                    writer.writerow(row)
            else:
                line_count += 1
                turn_aways = list()
                for item in row[7]:
                    if int(item) > turn_flag:
                        turn_aways = turn_aways + row
                        with open(OutputCsvFile, 'a') as fd:
                            writer = csv.writer(fd, delimiter=',')
                            writer.writerow(row)

                    else:
                        break



config.read('config.ini')
fromaddr = config['Outlook']['email']
toaddr = config['Outlook']['email']
email = config['Outlook']['email']
password = config['Outlook']['password']
username = config['Outlook']['username']

from O365 import Account, Connection


credentials = (config['Azure']['ApplicationID'], config['Azure']['ClientSecret'])

scopes = ['https://graph.microsoft.com/Mail.Send']




con = Connection(credentials, scopes=scopes)

m = account.new_message()
m.to.add(toaddr)
m.subject = 'Testing!'
m.body = "George Best quote: I've stopped drinking, but only while I'm asleep."
m.send()
#monthly
# note add to dashboard
#journals 10
#books 5
#just email to Carissa & this go to collection dev eventually

