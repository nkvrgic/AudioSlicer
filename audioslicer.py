from tkinter import *
from tkinter import scrolledtext
from tkinter.filedialog import * #use filename = askopenfilename()
from tkinter import ttk
from pydub import *


#VARS
songs = []
audiofile = ""
trackfile = ""
outpath = ""

root = Tk()
root.geometry("320x400")
root.resizable(False, False)

#Construct Frames
ft = Frame(root, height=100, width=320, padx=5, pady=10, relief=RAISED, bd=1)
ft.pack(side=TOP)
fb = Frame(root, height=200, width=320, padx=5, relief=RAISED, bd=1)
fb.pack()

#Frame 2 Widgets
termframe = Frame(fb, pady=5)
termframe.pack(side=TOP)
term = scrolledtext.ScrolledText(master=termframe, height=10, width=300,  pady=5)
term.pack(side=TOP)

pbarframe = Frame(fb, pady=5)
pbarframe.pack()
pbar = ttk.Progressbar(pbarframe, orient="horizontal", mode="determinate",
                       length=320)
pbar.pack()


#FUNCTIONS
def termPrint(e):
    term.insert(END, e)
    term.insert(END, "\n")
    
def loadAudio():
    global audiofile
    audiofile = askopenfilename()
    termPrint("Audio File Selected:\n" + audiofile)

def loadTracklist():
    global trackfile
    trackfile = askopenfilename()
    termPrint("Tracklist Selected:\n" + trackfile)
    
def setOut():
    global outpath
    outpath = askdirectory()
    termPrint("Files Will Be Written To:\n" + outpath)
    
def milliParse(a, b):
    a = int(a)*60
    b = int(b)
    summ=a+b
    return int(summ*1000)

    
def slice():
    global audiofile
    global trackfile
    global outpath
    print(audiofile)
    
    rawAudio = AudioSegment.from_mp3(audiofile)
    f = open(trackfile, "r")
    songs = [i.split(",") for i in f]
    f.close()
    for j in songs:
        startTime = milliParse(j[1].split(":")[0],j[1].split(":")[1])
        endTime = milliParse(j[2].split(":")[0],j[2].split(":")[1])
        step1 = rawAudio[:endTime]
        step2 = step1[-(endTime-startTime):]
        step2.export(j[0]+".mp3", format="mp3")
        termPrint(j[0] + " Extracted")
    termPrint("Done!")

       
        




#Frame 1 Widgets
header = Label(ft, text="Audio Slicer", relief=GROOVE, width=320,
               font=("",12,"bold"))
header.pack()

l1 = Frame(ft, width=200, pady=5)
l1.pack()
Label(l1, text="Load Audio File:  ").pack(side=LEFT)

openFileImage = PhotoImage(file="openfile.png")
openFileImage = openFileImage.subsample(30,30)

loadAudioButton = Button(l1,image=openFileImage, padx=40,
                         command=lambda:loadAudio())
loadAudioButton.pack(side=RIGHT)

l2 = Frame(ft, width=200, pady=5)
l2.pack()

Label(l2, text="Load Tracklist:  ").pack(side=LEFT)

loadTracklistButton = Button(l2,image=openFileImage,
                             command=lambda:loadTracklist())
loadTracklistButton.pack(side=RIGHT)

l3 = Frame(ft, width=200, pady=5)
l3.pack()

Label(l3, text="Choose Output Path:  ").pack(side=LEFT)

loadTracklistButton = Button(l3,image=openFileImage,
                             command=lambda:setOut())
loadTracklistButton.pack(side=RIGHT)

sliceButton = Button(ft, text="Slice and Export", width = 200,height=2,
                     command=lambda: slice())
sliceButton.pack(side=BOTTOM)



root.mainloop()



