import base64
import requests
import time


### PROSA.AI ###
url = "https://api.prosa.ai/v2/speech/tts"
api_key = "eyJhbGciOiJSUzI1NiIsImtpZCI6Ik5XSTBNemRsTXprdE5tSmtNaTAwTTJZMkxXSTNaamN0T1dVMU5URmxObVF4Wm1KaSIsInR5cCI6IkpXVCJ9.eyJhcHBsaWNhdGlvbl9pZCI6MTU1NTY1LCJsaWNlbnNlX2tleSI6Ijk1NTQ0ZmVhLTAwNjUtNDI2Mi1hM2ZhLWE1M2JiMzI3MzNkYyIsInVuaXF1ZV9rZXkiOiJjMmE4MjFmZC0wMzI2LTQ1YTYtODYyZS1jZmE5NmRmMGRkMDMiLCJwcm9kdWN0X2lkIjozLCJhdWQiOiJhcGktc2VydmljZSIsInN1YiI6IjYxNTVmZjliLTZkNzYtNDhmYS1iYzQ2LTI4ODYwMzY2MDYzMSIsImlzcyI6ImNvbnNvbGUiLCJpYXQiOjE2ODMwMTIxODZ9.Qnr85gbTUP_So2suMaEEKnGaHU1dtKB18UXDLR8rg24HjbT8wuafRfPbsOvyk5ix8TMrTQNaszcZ2nsGfYekLMfPaiR56izVxqo1RGZNS0U4bRSFemeOmyHVtelWi9z1_PeEkCU7QHzQLrTs-egEQGlC7qq2TEPGETIbbwmAyhrtwHnrN3Xw6GTSlpN4YyXONtgMgsfvODfcL9OUMQfe2H5lb5au0ehsQnncWovMRZzZdpjVVB7DJZCoxNSBUzm3YrMeLkuThJ8plkqoDXm4fim-x3uStnqVWyNZh0X4_9LdO85v6EGQHhscL1WG4a3hfgeDRtuv3eIi82McP1guuQ"

def textToSpeech(text):
    print("============ Text To Speech ==========")
    start = time.time()
    filename = "audio_file.mp3"
    text = str(text)

    audio_data = tts(text, "mp3")
    print(audio_data)
    with open(filename, "wb") as f:
        f.write(audio_data)

    print("Time to process : ", time.time() - start)
    print("=========== End of Text To Speech ===========")
    return audio_data, filename

def tts(text: str, audio_format: str) -> bytes:
    job = submit_tts_request(text, audio_format)
    #print(job)
    if job["status"] == "complete":
        return base64.b64decode(job["result"]["data"])

    # Job was not completed within the timeframe

def submit_tts_request(text: str, audio_format: str) -> dict:
    payload = {
        "config": {
            "model": "tts-dimas-storyteller",
            "wait": True,  # Blocks the request until the execution is finished
            "audio_format": audio_format
        },
        "request": {
            "text": text
        }
    }
    response = requests.post(url, json=payload, 
                             headers={"x-api-key": api_key}, timeout=20)
    return response.json()
