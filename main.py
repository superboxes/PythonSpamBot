from tkinter import *
from tkinter import messagebox
import time
from pynput.keyboard import Key, Controller
import time, threading
error = False
keyboard = Controller()
spambotFinished = False
readmeFile = open("README.txt", 'r')
lines = readmeFile.readline(11)
password = "Password: 1"
allFinished = False

if lines == password:
    def spambotDiscord(zodis, kartai, laikas):  #discord spambot
        lol = 0
        while lol < kartai:
            lol += 1
            keyboard.type(zodis)
            keyboard.press(Key.enter)
            time.sleep(laikas)
        spambotFinished = True
        AllFinished = True
        messagebox.showinfo(title="Info", message="Spambot is done, turn off the program now!")
        quit()
        exit()


    def spambotMinecraft(zodis, kartai, laikas):  # minecraft spam botas
        lol = 0
        laikas += 1
        while lol < kartai:
            lol += 1
            keyboard.type('t')
            time.sleep(laikas)
            keyboard.type(zodis)
            keyboard.press(Key.enter)
        spambotFinished = True
        allFinished = True
        messagebox.showinfo(title="Info", message="SSpambot is done, turn off the program now!")
        quit()
        exit()



    def choiceFirst():
        root.destroy()
        global zodis
        global kartai
        global laikas

        def Submit():
            global kartai
            global zodis
            global laikas
            zodis = zodiss.get()
            try:
                kartai = int(kartais.get())
            except ValueError:
                messagebox.showwarning(title="Dumbass",
                                       message="At the times choice, you have to enter a number")
                messagebox.showinfo(title="Dumbass", message="Now you have to turn off the program!")
                exit()
                error = True
            try:
                laikas = int(laikass.get())
            except ValueError:
                messagebox.showwarning(title="Dumbass",
                                       message="At delay choice, you have to enter a number")
                messagebox.showinfo(title="Dumbass", message="Now you have to turn off the program!")
                exit()
                error = True
            if not error:
                window.destroy()
                window1 = Tk()
                window1.title("Dicord SpamBot")
                Label(window1, text="SpamBot is working!", font=("Arial", '20', "bold")).pack()
                messagebox.showinfo(title="Info",
                                    message="When you press ok, you will have 10 seconds to choose where the spambot will write!")
                time.sleep(10)
                x = threading.Thread(target=spambotDiscord(zodis, kartai, laikas), daemon=True)
                x.start
                window1.mainloop()
            else:
                exit()

        window = Tk()
        window.title("Discord SpamBot")
        Label(window, text="SuperBoxes", font=("Comic Sans MS", '20'), fg="green").grid(row=0, column=1)
        label = Label(window, text="Word/Sentence: ", font=("Arial", '20', "bold"))
        label.grid(row=1, column=0)
        zodiss = Entry(window, font=("Arial", '20', "bold"))
        zodiss.grid(row=1, column=1)
        label2 = Label(window, text="Times:  ", font=("Arial", '20', "bold"))
        label2.grid(row=2, column=0)
        kartais = Entry(window, font=("Arial", '20', "bold"))
        kartais.grid(row=2, column=1)
        label3 = Label(window, text="Delay:  ", font=("Arial", '20', "bold"))
        label3.grid(row=3, column=0)
        laikass = Entry(window, font=("Arial", '20', "bold"))
        laikass.grid(row=3, column=1)
        Button(window, text="Submit", font=("Arial", '15'), command=Submit).grid(row=4, column=1)

        window.mainloop()
    def choiceSeco():
        root.destroy()
        global zodis
        global kartai
        global laikas
        def Submit():
            global kartai
            global zodis
            global laikas
            zodis = zodiss.get()
            try:
                kartai = int(kartais.get())
            except ValueError:
                messagebox.showwarning(title="Dumbass", message="At the times choice, you have to enter a number")
                messagebox.showinfo(title="Dumbass", message="Now you have to turn off the program!")
                exit()
                error = True
            try:
                laikas = int(laikass.get())
            except ValueError:
                messagebox.showwarning(title="Dumbass", message="At delay choice, you have to enter a number")
                messagebox.showinfo(title="Dumbass", message="Now you have to turn off the program!")
                exit()
                error = True
            if not error:
                window.destroy()
                window1 = Tk()
                Label(window1, text="SpamBotas Veikia!", font=("Arial", '20', "bold")).pack()
                messagebox.showinfo(title="Info",
                                    message="When you press ok, you will have 10 seconds to choose where the spambot will write!")
                time.sleep(10)
                z = threading.Thread(target=spambotMinecraft(zodis, kartai, laikas), daemon=True)
                z.start
                window1.mainloop()

        window = Tk()
        window.title("Minecraft SpamBot")
        Label(window, text="SuperBoxes", font=("Comic Sans MS", '20'), fg="green").grid(row=0, column=1)
        label = Label(window, text="Word/Sentence: ", font=("Arial", '20', "bold"))
        label.grid(row=1, column=0)
        zodiss = Entry(window, font=("Arial", '20', "bold"))
        zodiss.grid(row=1, column=1)
        label2 = Label(window, text="Times:  ", font=("Arial", '20', "bold"))
        label2.grid(row=2, column=0)
        kartais = Entry(window, font=("Arial", '20', "bold"))
        kartais.grid(row=2, column=1)
        label3 = Label(window, text="Delay:  ", font=("Arial", '20', "bold"))
        label3.grid(row=3, column=0)
        laikass = Entry(window, font=("Arial", '20', "bold"))
        laikass.grid(row=3, column=1)
        Button(window, text="Submit", font=("Arial", '15'), command=Submit).grid(row=4, column=1)

        window.mainloop()



    root = Tk()
    root.title("Superboxes spambot")
    icon = PhotoImage(file='download.png')
    root.geometry("300x243")
    root.iconphoto(True, icon)
    Label(root, text="Choose SpamBot type:",
          font=("Arial", '15', "bold")).pack(side=TOP)

    button1 = Button(root,
                     text="Discord spambot",
                     command=choiceFirst,
                     font=("Arial", 20),
                     fg='#00f000',
                     bg='white',
                     relief=RAISED,
                     bd=10,
                     padx=20,
                     pady=20,
                     activeforeground='#00f000',
                     activebackground="white", )

    button2 = Button(root,
                     text="Minecraft spambot",
                     command=choiceSeco,
                     font=("Arial", 20),
                     fg='#00f000',
                     bg='white',
                     relief=RAISED,
                     bd=10,
                     padx=15,
                     pady=15,
                     activeforeground='#00f000',
                     activebackground="white", )

    button1.pack()
    button2.pack()
    root.mainloop()


else:
    print("Incorrect password!")
    time.sleep(10)