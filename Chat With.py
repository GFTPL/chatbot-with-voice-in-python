from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import time

bot = ChatBot("My Bot")

convo = [
    "hi",
    "May I help you?",
   "My computer does not turn on, what do I do now?",
   "URL:https://help.gnome.org/users/gnome-help/stable/power-willnotturnon.html.en#:~:text=Computer%20not%20plugged%20in%2C%20empty,has%20run%20out%20of%20battery).",
   "What do I do when my computer crashes?",
   "URL: https://www.drivereasy.com/knowledge/how-to-fix-computer-crashing/",
   "What do I do if my hard disk fails to work?",
   "URL: https://dzone.com/articles/what-do-when-hard-drive-fails",
   "Why is my computer mouse acting erratically?",
   "URL: https://dzone.com/articles/what-do-when-hard-drive-fails",
   "The wheel on my mouse isn't working properly, what do I do?"
   "URL: https://www.computerhope.com/issues/ch000981.htm#:~:text=Clean%20the%20mouse&text=Try%20cleaning%20the%20mouse%2C%20especially,Mouse%20cleaning%20help.",
   "How can I clean my keyboard?",
   "URL1: https://www.wikihow.com/Clean-a-Keyboard Url2: https://www.youtube.com/watch?v=Tw_tpElJbxY"
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

main = Tk()

main.geometry("550x600")

main.title("My Chat bot")
img = PhotoImage(file="Ro.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)



 


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=2000, height=20, yscrollcommand=sc.set) 
sc.pack(side=RIGHT, fill=Y)
#scd = Scrollbar(frame)

#scd = Scrollbar(frame, orient='horizontal')
#scd.pack()
msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

def timer():
    global a
    a = 0
    time.sleep(5)
    #time.sleep(5)
    while a != 5:
        #print()
        a+=1
    else :
        msgs.insert(END, "bot : " + str("How Can I help You?"))
def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query) 
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    textF.delete(0, END)
    msgs.yview(END)
    timer()  



# creating text field

textF = Entry(main, font=("Verdana", 10))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()

def enter_func(event):
    btn.invoke()
main.bind('<Return>', enter_func)


main.mainloop()   
