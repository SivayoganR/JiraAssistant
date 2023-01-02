import speech_recognition as sr
import pyttsx3
from playsound import playsound
import wikipedia
import pyjokes
import datetime
engine=pyttsx3.init()
rate = engine.getProperty('rate')
newVoiceRate = 120
engine.setProperty('rate', newVoiceRate)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
        engine.say(text)
        engine.runAndWait()
def main():
       
       
    def song(command):
        song=command.replace('play ','')
        playsound('.\\music\\'+song+'.wav')
        print(song)
    def search(command):
        search=command.replace('search','')
        info=wikipedia.summary(search,1)
        print(info)
        return info
    def joke():
        joke=pyjokes.get_joke()
        print(joke)
        return joke
            
    r = sr.Recognizer()
    def take_command():
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            print("Please say something...")

            audio = r.listen(source,phrase_time_limit=5)
            try:
                command=r.recognize_google(audio)
                if 'play' in command:
                    song(command)
                    result='playing song' 
                elif 'search' in command:
                    result=search(command)
                elif 'joke' in command:
                    result=joke()
                elif 'are you single' in command:
                    result='No I am commited with kapilan'
                    print('No I am commited with wifi')
                elif 'time' in command:
                    time=datetime.datetime.now().strftime('%I %M %p')
                    print(time)
                    result='Current time is' + time
                elif ('tablet' in command or 'tablets' in command) and 'how' in command:
                    print('2')
                    result='you should take 2 tablets'
                elif ('tablet' in command or 'tablets' in command) and ('which' in command or 'what' in command):
                    print('ttt')
                    result='you should take ttt tablet'
                elif 'how are you' in command:
                    result='I am fine and what about you'
                elif ('hello' in command or 'hi' in command or 'hai' in command):
                    result='hello friend'
                else:
                    result='Try something else'
            except Exception as e:
                command="Can't able to hear. Can you repeat once again?"
                result=command
               
                print("LICENSE.txtror : " + str(e))
            return result
    
        
    command=take_command()
    return command
            
        
#result=main()        
#print(result)



