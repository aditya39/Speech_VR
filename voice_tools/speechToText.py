import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
os.environ["OMP_NUM_THREADS"] = "6" # export OMP_NUM_THREADS=4
from faster_whisper import WhisperModel

from deepgram import Deepgram
import asyncio, json
import sys
import time

fastWhisper_model_base = "base"
        # Run on GPU with FP16
model = WhisperModel(fastWhisper_model_base, device="cuda", compute_type="int8")

def speechToTextWhisper(audio_input):
    start = time.time()
    print("============ Speech To Text Start ============")
    try:
        
        sentences = []
        
        # or run on GPU with INT8
        # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
        # or run on CPU with INT8
        #model = WhisperModel(fastWhisper_model_base, device="cpu", compute_type="int8", cpu_threads=12)
        segments, _ = model.transcribe(audio_input, beam_size=1, language="id")
        for segment in segments:
            sentences.append(segment.text)
            #print(segment.text)
        #print(sentences)

            print( "Hasil SpeechToText : ", segment.text)
        print("Time to process: ", time.time() - start)
        
        return(sentences)
    except: return("Error")
    print("===================== End =====================")
# Example filename: deepgram_test.py


def speechToTextDeepgram(audio_input):
    # Your Deepgram API Key
    DEEPGRAM_API_KEY = '435b140742df560c06258b90535e1d77ccd27b7e'
    # Location of the file you want to transcribe. Should include filename and extension.
    FILE = audio_input
    # Mimetype for the file you want to transcribe
    # Include this line only if transcribing a local file
    # Example: audio/wav
    MIMETYPE = 'audio/m4a'

    async def main():
        # Initialize the Deepgram SDK
        deepgram = Deepgram(DEEPGRAM_API_KEY)

        # Check whether requested file is local or remote, and prepare source
        if FILE.startswith('http'):
            # file is remote
            # Set the source
            source = {
            'url': FILE
            }
        else:
            # file is local
            # Open the audio file
            audio = open(FILE, 'rb')

            # Set the source
            source = {
            'buffer': audio,
            'mimetype': MIMETYPE
            }

        # Send the audio to Deepgram and get the response
        response = await asyncio.create_task(
            deepgram.transcription.prerecorded(
            source,
            {
                'punctuate': True,
                'model': 'base',
                'language': 'id'
            }
            )
        )
        # Write the response to the console
        #print(json.dumps(response, indent=4))
        # Write only the transcript to the console
        print(response["results"]["channels"][0]["alternatives"][0]["transcript"])
        try:
            # If running in a Jupyter notebook, Jupyter is already running an event loop, so run main with this line instead:
            #await main()
            asyncio.run(main())
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            print(f'line {line_number}: {exception_type} - {e}')