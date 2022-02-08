from distutils.errors import UnknownFileError
from tokenize import String
import speech_recognition as sr


# STT = speech to text
class stt:

    # Need a mic in order to hear stuff
    mic = sr.Microphone()

    # When we intialize, set up a recognizer and then adjust mic for background noise
    def __init__(self) -> None:

        # Intialize
        self.recognizer = sr.Recognizer()

        # Adjust the mic for ambient noise
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=4)
    

    # If the microphone needs readjustment, this module serves to adjust for background noise
    def adjust_for_background_noise(self, duration=4) -> None:
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=4)

    # Primary functionality. Converts speech to a string
    def speech_to_text(self) -> String:
            
        # Use the mic to listen to audio
        with self.mic as source:
            print("Mic active")

            audio = self.recognizer.listen(source)

            # Try to convert it to a string, if that doesn't 
            # work, adjust for background noise and try again
            try:

                ans = self.recognizer.recognize_sphinx(audio)

            except self.recognizer.UnknownValueError:
                print("Could not understand. Recalibrating")
                self.adjust_for_background_noise()
                self.speech_to_text()

            return ans


if __name__ == "__main__":

    rec = stt()

    print(rec.speech_to_text())