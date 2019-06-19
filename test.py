from O365 import Account
import configparser
config = configparser.ConfigParser()
config.read('config.ini')


credentials = (config['Azure']['ApplicationID'], config['Azure']['ClientSecret'])

account = Account(credentials)  # the default protocol will be Microsoft Graph
account.authenticate(scopes=['basic', 'message_all'])
m = account.new_message()
m.to.add('to_example@example.com')
m.subject = 'Testing!'
m.body = "George Best quote: I've stopped drinking, but only while I'm asleep."
m.send()