from asyncio.windows_events import NULL
from importlib.resources import path
import tkinter as tk
import os
import csv
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from turtle import position, width
from PIL import ImageTk,Image
root = tk.Tk()
def audio():
    song=filedialog.askopenfilename()
    os.system('"%s"'%song)

def enc():
    import wave
    # read wave audio file
    song = wave.open(filedialog.askopenfilename(), mode='rb')
    # Read frames and convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # The "secret" text message
    string=inputtxt.get(1.0,"end-1c")
    lbl.config(text="Hidden Audio: " +string,font="Times 12 bold")

    if string == " ":
        {
            messagebox.showinfo("ENCODE","Please Hide Text...")
        }
    else:
        {
            messagebox.showinfo("ENCODE","Message Hidden Successfully!")
        }
    # Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
    string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
    # Convert text to bit array
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

    # Replace LSB of each byte of the audio data by one bit from the text bit array
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    # Get the modified bytes
    frame_modified = bytes(frame_bytes)

    # Write bytes to a new wave audio file
    with wave.open(filedialog.asksaveasfilename(), 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()
user_name = Label(root,text = "Enter Your Message",font="Times 12 bold").place(x =150,y = 200)
inputtxt=tk.Text(root,height=5,width=25)
inputtxt.place(x=300,y=200)
#button5=tk.Button(root,text="Encode",command=enc)
#button5.pack()

lbl=tk.Label(root,text="")
lbl.place(x=300,y=300)

def popup():
    import wave
    #song=filedialog.askopenfilename()
    song=wave.open(filedialog.askopenfilename(),mode='rb')
    os.system("C:\Adi\Audio Steganalysis")

    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # Extract the LSB of each byte
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

    # Convert byte array back to string
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))

    # Cut off at the filler characters
    decoded = string.split("###")[0]

    #Chech if secret message is present or not!!
    if decoded =='':
        {
            messagebox.showinfo("ANALYSIS","No Hidden Message...")
        }
    elif decoded == string :
        {
            messagebox.showinfo("ANALYSIS","No Hidden Message...")
        } 
    # Print the extracted text
    else:
        {
            messagebox.showinfo("ANALYSIS","Hidden Message is There!!!! \n" "Message is: " +decoded)
        }
    song.close()

my_pic=ImageTk.PhotoImage(file="image\\nist.jpg")
my_label=Label(root,image=my_pic)
my_label.pack(side=tk.BOTTOM)
my_label.place(x=10,y=360)
my_label1=Label(root,text="B.TECH PROJECT\n by\n Aditya & Muddassir",font = "Times 15 bold",fg ="Purple")
my_label1.place(x=280,y=350)
root.title("Audio Steganalysis")
root.geometry("700x500")
#root.configure(bg="black")
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Encode",fg="White",command=enc,height = 1 , width = 5, bg = "black" ,font = "Times 20 bold" , borderwidth = 10)
button.pack(side=LEFT)
button2 = tk.Button(frame,text="Decode",command=popup,height = 1 , width = 5, bg = "black" , fg = 'white',font = "Times 20 bold" , borderwidth = 10)
button2.pack(side=LEFT,padx=20, pady=20)
button3 = tk.Button(frame, text="PLAY",fg="Blue",command=audio,height = 1 , width = 5, bg = "black" ,font = "Times 20 bold" , borderwidth = 10)
button3.pack(side=LEFT,padx=2, pady=20)
button4 = tk.Button(frame, text="QUIT",fg="red",command=quit,height = 1 , width = 5, bg = "black" ,font = "Times 20 bold" , borderwidth = 10)
button4.pack(side=LEFT,padx=20, pady=20)

root.mainloop()