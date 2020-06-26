from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as ppo

engine  = ppo.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 130)
engine.setProperty('volume', 0.3) 
def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")

convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by Proud',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in Sirsa',
    'In which language you talk?',
]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)
trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main = Tk()

main.geometry("2500x900")

main.title("My Chat bot")
img = PhotoImage(file="Ro.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)



def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query) 
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
scd = Scrollbar(frame, orient='horizontal')
msgs = Listbox(frame, width=2000, height=20, yscrollcommand=sc.set, xscrollcommand=scd.set) 
scd.pack(side=RIGHT, fill=X)
sc.pack(side=RIGHT, fill=Y)
#scd = Scrollbar(frame)

#scd = Scrollbar(frame, orient='horizontal')
#scd.pack()
msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 10))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()

def enter_func(event):
    btn.invoke()
main.bind('<Return>', enter_func)


main.mainloop()