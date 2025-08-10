from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def handle_message(message: str) -> str:
    """Processes incoming message and returns a reply."""
    message = message.lower().strip()
    if "hello" in message:
        return "Hi there! 👋 How can I assist you today?"
    elif "pricing" in message:
        return "We offer services starting at KES 1000."
    elif "bye" in message:
        return "Goodbye! 👋 Have a great day!"
    else:
        return "Sorry, I didn't understand that. Try 'hello', 'pricing', or 'bye'."

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    user_message = request.values.get("Body", "")
    sender = request.values.get("From", "")
    logging.info(f"Received message from {sender}: {user_message}")

    bot_reply = handle_message(user_message)

    response = MessagingResponse()
    response.message(bot_reply)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, redirect
import urllib.parse

app = Flask(__name__)

@app.route("/item")
def generate_whatsapp_link():
    item = request.args.get("name", "your item")
    source = request.args.get("source", "your ad")

    message = f"Hi, I saw the {item} ad on {source.capitalize()}. Is it still available?"
    encoded_message = urllib.parse.quote(message)
    
    whatsapp_number = "254754597946"
    wa_link = f"https://wa.me/{whatsapp_number}?text={encoded_message}"

    return redirect(wa_link)

