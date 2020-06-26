from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot = ChatBot("My Bot")

convo = [
    "Hi"
    "Any issue??"
   "My computer does not turn on, what do I do now?",
   "Computer not plugged in, empty battery, or loose cable",
   "What do I do when my computer crashes?",
   "Reboot your computer.Make sure your CPU works properly.Boot in Safe Mode.Update your drivers.Run System File Checker.",
   "What do I do if my hard disk fails to work?",
   "As with most computer errors, your first step is to shut down your computer and restart it. This will help you determine whether or not you actually have a hard disk problem. If the disk is severely damaged then your computer will probably fail to restart properly. If this is the case then contact MCWare IT Solutions, this is a job for the professionals.",
   "Why is my computer mouse acting erratically?",
   "Users who have an optical mechanical mouse (most common mouse for desktop computers) are likely experiencing erratic behaviour because the mouse is not clean or is dirty. If you've cleaned the mouse and continue to encounter issues and this mouse has worked in the past fine unfortunately your mouse is likely defective. One additional test that can be done to help determine if this is the case or not is to connect the mouse to another computer. Otherwise we suggest replacing the mouse.",
   "The wheel on my mouse isn't working properly, what do I do?"
   "If you're running any version of Microsoft Windows and are encountering issues with the mouse wheel, first attempt to adjust the mouse settings through the Mouse Properties window. This window can be accessed by opening the Control Panel and double-clicking the Mouse icon.",
   "How can I clean my keyboard?",
   "The keys on a keyboard are only clipped on, with a knife or other thin object, carefully pop the keys off, this will allow you to clean under the keys as well as cleaning the keys themselves (make sure you remember where they went!)."
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
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=2000, height=20, yscrollcommand=sc.set) 
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