from flask import Flask
from twilio import twiml
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  resp = twiml.Response()
  resp.message("Thank you for registering with the NHS SMS reminder service.")
  return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
