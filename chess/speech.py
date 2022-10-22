import speech_recognition as sr
import pyaudio
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     r.adjust_for_ambient_noise(source);
#     print("Threshold: ", r.energy_threshold)
#     print("Speak: ")
#     audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio,language="vi-VI")
#         print("Said -->: {}".format(text))
#     except:
#         print("Error!")

def recogVoice():
    r = sr.Recognizer()
    text = ''
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source);
        print("Threshold: ", r.energy_threshold)
        print("Threshold: ", r.energy_threshold)
        print("Speak: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="vi-VI")
            print("Said -->: {}".format(text))
        except:
            print("Error, Speak again!")
    return text

def extract_xy(text_from_voice):
    if verify_input(text_from_voice):
        xy = int(text_from_voice)
        if xy < 89:
            y = xy % 10
            x = int((xy - y)/10)
        else:
            print("Invalid Input")
            return (0,0)
        return (x,y)
    return (0,0)

def verify_input(input):
    # dasdsa
    if input == '':
        return False
    try:
        int(input)
        return True
    except ValueError:
        return False
    return True

if __name__ == "__main__":
    print("Final result: ", extract_xy(recogVoice()))
