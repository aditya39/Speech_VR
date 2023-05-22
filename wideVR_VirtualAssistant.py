import sys
sys.path.insert(0, 'voice_tools')

import logging
import os
import time
import json
from voice_tools.speechToText import speechToTextWhisper
from flask import Flask, request
#from tomonkey import faceShapeDetection
import base64

#default_dir = os.getcwd()
### route request from JSON android
## Route for KTP Extraction using YOLO
app = Flask(__name__)

@app.route("/v1/speechtotext", methods=["POST"])
def speechToText_fastWhisper():
    # Start the timer for whole process
    start_time_whole = time.time()
    # Get the base64 string from Request and decode it and Save it to the memory
    voice = request.get_json(force=True)['voice']
    ip_address = request.remote_addr
    logging.info("IP Address: {}, Using Service faceShape".format(ip_address))

    m4a_file = open("temp.m4a", "wb")
    decode_string = base64.b64decode(voice)
    m4a_file.write(decode_string)

    # start the timer for image processing
    start_time_processing = time.time()

    json_data = speechToTextWhisper("temp.m4a")

    timeused_whole = time.time() - start_time_whole
    timeused_processing = time.time() - start_time_processing
    # Create JSON Format Data for send back to Android
    if json_data == "Error":
        json_response = { 
        'status' : 'Failed',	 
        'data' : "empty",
        'timestamp_whole' : str(timeused_whole),
        'timestamp_processing' : str(timeused_processing)}

        logging.info(json_response)
        logging.info("--- %s seconds ---" % (timeused_processing))

        print("Failed")

        # Return the JSON Format Data
        return json.dumps(json_response)

    else:
        json_response = { 
            'status' : 'success',	 
            'data' : json_data,
            'timestamp_whole' : str(timeused_whole),
            'timestamp_processing' : str(timeused_processing)}

        logging.info(json_response)
        logging.info("--- %s seconds ---" % (timeused_processing))
        print("Success")

        # Return the JSON Format Data
        return json.dumps(json_response)


if __name__ == '__main__':
    #os.chdir(default_dir)
    app.run(debug=True, host='0.0.0.0', port=4000)