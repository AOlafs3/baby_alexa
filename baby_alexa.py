import speech_recognition as sr
import pyttsx3 as pyt
import datetime
import baby_database as db

listener = sr.Recognizer()
engine = pyt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
wake_word = 'nanny'
baby_name = 'unknown'


def speak(text, rate = 150):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        input_speech = listener.listen(source)

    try:
        print('Recognizing speech....')
        query = listener.recognize_google(input_speech)
        print(f'The input was: {query}')
    
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'
    
    return query

def say_ok():
    speak('OK', 160)


#main loop
if __name__ == '__main__':
    speak('I am Nanny, how may I help you?')

    while True:
        #parse as list
        query = parseCommand().lower().split()

        if query[0] == wake_word:
            query.pop(0)

            #list commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings!')
                else:
                    query.pop(0)
                    speech = ' '.join(query)
                    speak(speech)
            
            #diaper numero one
            if query[0] == 'diaper' and (query[1] == '1' or query[1] == 'one') :

                type = 'd1'

                #time elements
                now = datetime.datetime.now()
                date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                year = now.strftime("%Y")
                month = now.strftime("%m")
                day = now.strftime("%d")
                time = now.strftime("%H:%M")

                key = str(hash(date_time))

                db.insert_d1(key, type, date_time, year, month, day, time)
                say_ok()

            #diaper numero two
            if query[0] == 'diaper' and (query[1] == '2' or query[1] == 'two') :

                type = 'd2'

                #time elements
                now = datetime.datetime.now()
                date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                year = now.strftime("%Y")
                month = now.strftime("%m")
                day = now.strftime("%d")
                time = now.strftime("%H:%M")

                key = str(hash(date_time))

                db.insert_d1(key, type, date_time, year, month, day, time)
                say_ok()

            #tummy time
            if query[0] == 'tummy' and query[1] =='time':
                if query[2] == 'start':
                    start_time = datetime.datetime.now()
                    print(start_time)
                if query[2] == 'end' or query[2] == 'and':
                    end_time = datetime.datetime.now()

    