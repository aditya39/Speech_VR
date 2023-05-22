import logging
logging.basicConfig(filename='../logs/wideVR-assistant-bot.log', level=logging.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
from flaskConfig import app, request
import time
import requests
import json
import base64
from voice_tools.speechToText import speechToTextWhisper
from voice_tools.textToSpeech import textToSpeech

"""# Test client for interacting with Rasa bot

import requests

sender = input("What is your name?\n")

bot_message = ""
while bot_message != "Bye":
	message = input("What's your message?\n")

	print("Sending message now...")

	r = requests.post('http://localhost:5201/webhooks/rest/webhook', json={"sender": sender, "message": message})

	print("Bot says, ")
	for i in r.json():
		bot_message = i['text']
		print(f"{i['text']}")"""

@app.route("/chat", methods=["POST"])
def main():
    botMessage = []
    startTime = time.time()
    data = request.get_json(force=True)
    sender = data["sender"]; message = data["message"]
    r = requests.post('http://localhost:5201/webhooks/rest/webhook', json={"sender": sender, "message": message})
    
    for i in r.json():
        message = i['text']
        print(f"{i['text']}")
        botMessage.append(message)
    return json.dumps({"sender":"bot", "message":botMessage, "timeStamp": time.time() - startTime})

@app.route("/v1/chat-with-bot", methods=["POST"])
def speechToText_fastWhisper():
    # Start the timer for whole process
    start_time_whole = time.time()
    # Get the base64 string from Request and decode it and Save it to the memory
    data = request.get_json(force=True)
    ip_address = request.remote_addr
    logging.info("IP Address: {}, Using Service faceShape".format(ip_address))

    m4a_file = open("temp.m4a", "wb")
    decode_string = base64.b64decode(data["voice"])
    m4a_file.write(decode_string)

    # start the timer for image processing
    start_time_processing = time.time()
    isError = False
    try:
        textMessage = speechToTextWhisper("temp.m4a")
    except Exception as e:
        logging.error(e)
        isError = True

    print(textMessage)
    botMessage = ""

    try:
        sender = data["sender"]; message = str(textMessage[0])
        print(message)
        r = requests.post('http://localhost:5201/webhooks/rest/webhook', json={"sender": sender, "message": message})
        for i in r.json():
            message = i['text']
            print(f"{i['text']}")
            botMessage = botMessage + message + ". "
        
        print(botMessage)

    except Exception as e:
        logging.error(e)
        isError = True

    #try:
    botVoice = textToSpeech(botMessage)
    #except Exception as e:
    #    logging.error(e)
    #    isError = True

    if isError == True:
        json_response = { 
            'status' : 'failed',	 
            'botVoice' : "-",
            'timestamp_whole' : str(start_time_whole - time.time()),
            'timestamp_processing' : str(start_time_processing - time.time())}

        return json.dumps(json_response)

    else:
        json_response = { 
            'status' : 'success',	 
            'botVoice' : str(botVoice),
            'timestamp_whole' : str(start_time_whole - time.time()),
            'timestamp_processing' : str(start_time_processing - time.time())}

        return json.dumps(json_response)            

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5200, debug=True)