from os import environ, path
from dotenv import load_dotenv
from twilio.rest import Client
import logging

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# Configure logger
logging.basicConfig(filename='sms/error.log', format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# Initiate logger object
logger = logging.getLogger()
 
# Set threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


account_sid = environ.get('TWILIO_ACCOUNT_SID')
auth_token = environ.get('TWILIO_AUTH_TOKEN')

# instantiating the Client
client = Client(account_sid, auth_token)

# sending message
message = client.messages.create(
    body='Hi there, this is a text from Twilio SMS.', 
    from_='+15617944728',
    status_callback='http://postb.in/1234abcd',
    to='+13105551234'
)

# Log response
print(message)
logger.info(message)