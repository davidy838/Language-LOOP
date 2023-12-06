import speech_recognition as sr


def speechValidator(audio, correct):
# Initialize recognizer
    r = sr.Recognizer()

    user_input = r.recognize_google(audio, language='zh-CN')

    if (user_input == correct):
        return True
    else:
        return False 



