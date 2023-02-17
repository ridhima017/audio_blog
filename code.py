#import library
import speech_recognition as sr
#Initialize recognizer class (for recognizing the speech)
r sr.Recognizer()
code=""
name=input("Enter blog name")
#asks for details while starting a new blog
lang-input("Enter language choice: ")
dict={"French": "fr-FR", "German": "de-DE", "Hindi":"hi-IN", "English":"en-IN", "Telugu":"te-IN"}
#5 languages used for prototype
for item in dict:
if lang==item: code-dict[item]
break→→→ print("Your journey has started")
choice="" 1st=[]
while(choice!="exit"):
with sr.Microphone() as source: print("Talk")
audio_text = r.listen(source)
#listen function is used to reocord audio
print("Time over, thanks")
try:
1st.append(text)
choice=input()
except:
print("Sorry, I did not get that")
for item in 1st: 
    print (item, end=".") 
#audio is converted to text and stored
