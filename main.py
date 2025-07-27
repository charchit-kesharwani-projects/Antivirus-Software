import sys

from tkinter import *
from tkinter import filedialog
import random
import os
import time
import engine

os.startfile("C:\\Users\\asus\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\real-time-protection_setting.bat")

window = Tk()

window.title("Threat Blocker")
window.geometry('1500x650')
window.maxsize("1500","650")
window.minsize("1500","650")


# Create a Label widget for the text "Terminal Window"
terminal_label = Label(window, text="Terminal Window", font = "times 12 bold")
# Specify the x and y coordinates where you want to place the label
x_coordinate_label = 140
y_coordinate_label = 130
# Place the label at the specified coordinates
terminal_label.place(x=x_coordinate_label, y=y_coordinate_label)

# Create a Text widget to display terminal-like output
terminal_output = Text(window, width=50, height=20, bd=1, relief="sunken")
terminal_output.pack(side=LEFT, padx=10, pady=10)

# Redirect print output to the Text widget
def redirect_output(text_widget):
    class StdoutRedirector:
        def __init__(self, text_widget):
            self.text_widget = text_widget

        def write(self, str):
            self.text_widget.insert(END, str)
            self.text_widget.see(END)

    sys.stdout = StdoutRedirector(text_widget)

# Call the function to redirect output
redirect_output(terminal_output)







nj = Frame(window, width=1500, height = 650)
nj.pack()
nj.pack_propagate(0)

def mainFrameNj():

    global opring
    global quickScanImg
    global junkFileRemoverImg
    global ramBoosterImg
    global photoScan
    global nj

    nj.destroy()

    nj = Frame(window, width=1100, height = 600)
    nj.pack()
    nj.pack_propagate(0)



    def junkFileRemoverFunc():
        ri = engine.juckFileRemover
        ri()

    def ramBoosterFunc():
        ri = engine.ramBooster
        ri()

    def customScanFunc():
        source_path = filedialog.askdirectory(title='Select the Parent Directory')
        print(source_path)
        ri = engine.virusScanner
        ri(source_path)

    def writeFile(write):
        switch_check = open("C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\real-time_switch.blink","w")
        switch_check.write(write)
        switch_check.close()

    def AV_switch():
        switch_check = open("C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\real-time_switch.blink","r")
        Pos = switch_check.readline()
        switch_check.close()    
    

        if Pos == 1 or Pos == "1" :
            print(Pos)
            writeFile("0")
        
            tls.configure(image = photog)
        
    
        elif Pos == 0 or Pos == "0":
            print(Pos)
            writeFile("1")
        
            tls.configure(image = photoi)

    opring = 5

    def buleAnimation_():
        global opring

        buleAnimationPlus00.configure(image = buleAnimationPlusList[opring])


        if opring == 0:
            opring = 5

        opring -= 1

        buleAnimationPlus00.after(200,buleAnimation_)



    photoi = PhotoImage(file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\0.png").subsample(3,3)
    photog = PhotoImage(file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\0 a.png").subsample(3,3)
    photoScan = PhotoImage(file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\scan l.png").subsample(4,4)
    junkFileRemoverImg = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\junk file remover.png").subsample(4,4)
    quickScanImg = PhotoImage(file ="C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\quick scan.png").subsample(4,4)
    ramBoosterImg = PhotoImage(file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\ram booster.png").subsample(4,4)

    buleAnimationPlus0 = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\blue ani\\0.png").subsample(21,21)
    buleAnimationPlus1 = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\blue ani\\1.png").subsample(21,21)
    buleAnimationPlus2 = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\blue ani\\2.png").subsample(21,21)
    buleAnimationPlus3 = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\blue ani\\3.png").subsample(21,21)
    buleAnimationPlus4 = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\blue ani\\4.png").subsample(21,21)
    buleAnimationPlus5 = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\blue ani\\5.png").subsample(21,21)


    buleAnimationPlusList = [buleAnimationPlus0,buleAnimationPlus1,buleAnimationPlus2,buleAnimationPlus3,buleAnimationPlus4,buleAnimationPlus5]




    bitLinkMainLabel = Label(nj, text = "Threat Blocker", font = "Times 30 bold")
    bitLinkMainLabel.pack(side = TOP, pady = 20)

    tls = Button(nj, text = 'Click Me !', image = photoi, bd=0, command=AV_switch)
    tls.pack(side = TOP, pady = 0)

    quickScan = Button(nj, image = quickScanImg, bd = 0, command = quickScanFrame)
    quickScan.place( x = 90 , y = 410)
    label_text = Label(nj, text="Quick Scan")
    label_text.place(x=124, y=550)
    
    fscan = Button(nj, image = photoScan, bd = 0, command = customScanFunc)
    fscan.place(x = 350 , y = 410)
    label_text = Label(nj, text="Custom Scan")
    label_text.place(x=370, y=550)

    junkFileRemover = Button(nj, image = junkFileRemoverImg ,bd = 0, command = junkFileRemoverFunc)
    junkFileRemover.place( x = 610 , y = 410)
    label_text = Label(nj, text="Junk File Remover")
    label_text.place(x=625, y=550)

    ramBooster = Button(nj, image = ramBoosterImg , bd = 0, command = ramBoosterFunc)
    ramBooster.place( x = 870 , y = 410)
    label_text = Label(nj, text="RAM Booster")
    label_text.place(x=900, y=550)

    buleAnimationPlus00 = Label(nj, image = buleAnimationPlus0)
    buleAnimationPlus00.place(x = 50, y = 10)

    buleAnimation_()


def quickScanFrame():
    global nj
    global backButtonImg
    global prog0
    global prog1
    global prog2
    global prog3
    global prog4
    global prog5
    global io
    global ranHashShower
    global samB
    global rMVirus

    with open("C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\virusHash.unibit", "r") as nr:
        samB = nr.readlines()
        nr.close()



    nj.destroy()

    nj = Frame(window, width=1100, height = 600)
    nj.pack()
    nj.pack_propagate(0)

    io = 0

    def removeVirusBtn():
        try : 
            with open("switch_virusscanner.bb","r") as bb:
                io = list(bb.readlines())
                bb.close()
        except:pass

        try:
            for i in io:
                i = i[0:len(i)-1]
                print(i," Removed")
                os.remove(i)
        except:pass


    def progressBarAni():
        global io
        
        progLabel.configure(image = progList[io])

        io += 1

        

        id = progLabel.after(500, progressBarAni)

        if io == 5:
            io = 0
            try : 
                with open("switch_io.bb","r") as nri:
                    xxc = nri.read()
                    nri.close()
                
                if xxc == "1" or xxc == 1:
                    progLabel.after_cancel(id)
            
            except:pass

    def textShower():
        global samB

        ranHashShower.configure(state='normal')
        ranHashShower.delete("1.0",END)
        ranHashShower.insert(INSERT,samB[random.randint(0,len(samB)-1)])

        id = ranHashShower.after(100, textShower)

        try : 
            with open("switch_io.bb","r") as nri:
                xxc = nri.read()
                nri.close()
                
            if xxc == "1" or xxc == 1:
                ranHashShower.after_cancel(id)
            
        except:pass

    def VirusFoundPathX():

        try:
            with open ("switch_virusscanner.bb","r") as X:
                cc = X.readlines()
                X.close()
        

            virusFoundPaths.configure(state='normal')
            virusFoundPaths.delete("1.0",END)
            virusFoundPaths.insert(INSERT,cc)


        except:pass

        id = virusFoundPaths.after(200, VirusFoundPathX)

    backButtonImg = PhotoImage(file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\back button.png").subsample(4,4)
    prog0 = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\progress bar\\0.png").subsample(1,3)
    prog1 = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\progress bar\\1.png").subsample(1,3)
    prog2 = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\progress bar\\2.png").subsample(1,3)
    prog3 = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\progress bar\\3.png").subsample(1,3)
    prog4 = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\progress bar\\4.png").subsample(1,3)
    prog5 = PhotoImage( file = "C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\res\\progress bar\\5.png").subsample(1,3)
    progList = [prog0,prog1,prog2,prog3,prog4,prog5]

    bitLinkMainLabel = Label(nj, text = "Quick Scan", font = "Times 21 bold")
    bitLinkMainLabel.pack(side = TOP, pady = 20)

    backButton = Button(nj, image = backButtonImg, bd = 0, command = mainFrameNj)
    backButton.place(x = 10 , y = 10)

    progLabel = Label(nj, image = prog0)
    progLabel.place(x = 250, y = 70)


    pathLabel = Label(nj, text = "Virus Scanner", font = "Times 20 bold")
    pathLabel.place(x = 350, y = 130)

    ranHashShower = Text(nj, width=50, height=1, bd = 0, font= ('Sans Serif', 13, 'bold'),foreground="green")
    ranHashShower.place( x = 350 , y = 170)
    ranHashShower.insert(INSERT, "Write Something About Yourself")
    ranHashShower.configure(state='disabled')

    virusDetet = Label(nj, text = "Virus Found", font = "Times 20 bold")
    virusDetet.place(x = 350, y = 230)

    virusFoundPaths = Text(nj, width=100, height=10, bd = 0, font= ('Sans Serif', 13, 'bold'),foreground="red")
    virusFoundPaths.place( x = 50 , y = 290)
    virusFoundPaths.insert(INSERT, "No Virus Found")
    virusFoundPaths.configure(state='disabled')

    rMVirus = Button(nj, text = "Remove Virus", font = "Times 20 bold", command = removeVirusBtn)
    rMVirus.place(x = 350, y = 230)

    textShower()

    progressBarAni()

    os.startfile("C:\\Users\\asus\\Desktop\\anti test demo\\Bit-Link-Python-Antivirus-DEMO-main\\scannerStartQuick.bat")

    VirusFoundPathX()


    # Get the list of all files in directory tree at given path

        




mainFrameNj()





window.mainloop()