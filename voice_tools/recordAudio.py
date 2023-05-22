import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

def record():
    # Sampling frequency
    freq = 44100
    
    # Recording duration
    duration = 5
    
    # Start recorder with the given values
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=2)
    
    print("Recording..")
    # Record audio for the given number of seconds
    sd.wait()
    print("Recording finished.")
    
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    filename = "recording0.mp3"
    write(filename, freq, recording)

    return filename