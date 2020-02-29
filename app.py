from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import Fetch_reply

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no=request.form.get('From')
    
    reply= Fetch_reply(msg, phone_no)
    
    # Create reply 
    resp = MessagingResponse()
    resp.message(reply)  #.text

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)