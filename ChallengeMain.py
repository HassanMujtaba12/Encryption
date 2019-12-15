#Importing the modules and files
import webbrowser
from tkinter import *           #GUI Module
import matplotlib.pyplot as plt     #Allows to make a graph
import numpy as np                  #Allows to sort and arrange data
import Frequency as f               #Frequency file containing data to make a graph
import CaesarCipher as cc           #File contaning all the encryption programs

#-----------------------------------------------------------------------------------------------------------------------------------------------------#

class cipher():


    def __init__(self,master):
        new = 1
        url = "https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences"

        def openweb():
            webbrowser.open(url,new=new)
        def graph():
            f.making_chart(self.Result.get())       #Draws a Graph according to the output
        def Reset():      #Resets the boxes for user
            self.KEY.set("")                #Restting the Key entry box
            self.txtMsg.delete(1.0, END)
            self.Result.set("")
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
        def main_cipher_pro():          #Applies encryption according to the inputs from check boxes
            texttime = self.txtMsg.get(1.0,'end-1c')
            if (self.trans_cipher.get() == True) and (self.vegenere_cipher.get()==False) and (self.caesar_cipher.get() == False):
                
                if (self.encrypt.get() == True) and (self.decrypt.get()==False):
                    
                    self.Result.set(cc.encryptMessage(texttime,self.KEY.get()))             #Displaying Result
                elif (self.encrypt.get() == False) and (self.decrypt.get()==True):
                    self.Result.set(cc.encryptMessage(texttime,self.KEY.get()))
                else:
                    self.Result.set("Cant select both!!!")                
            elif (self.caesar_cipher.get() == True) and (self.vegenere_cipher.get()==False) and (self.trans_cipher.get() == False):
                if (self.encrypt.get() == True) and (self.decrypt.get()==False):
                    g=cc.encrypt(texttime,self.KEY.get())
                    self.Result.set(g)
                elif (self.encrypt.get() == False) and (self.decrypt.get()==True):
                    a=cc.decrypt(texttime,self.KEY.get())
                    self.Result.set(a)
                else:
                    self.Result.set("Cant select both!!!")
            elif (self.caesar_cipher.get() == False) and (self.vegenere_cipher.get()==True) and (self.trans_cipher.get() == False):
                if (self.encrypt.get() == True) and (self.decrypt.get()==False):
                    #g=cc.veg_encode(self.KEY.get(),texttime)
                    self.Result.set(cc.veg_encode(self.KEY.get(),texttime))
                elif (self.encrypt.get() == False) and (self.decrypt.get()==True):
                    #a=cc.veg_decode(self.KEY.get(),texttime)
                    self.Result.set(cc.veg_decode(self.KEY.get(),texttime))
                else:
                    self.Result.set("Can't Select Both!!!")
            else:
                self.Result.set("Choose one type of cipher!!!")
                
#-----------------------------------------------------------------------------------------------------------------------------------------------------#                
        #Creating the GUI for the user
        master.configure(bg='grey82')
        master.title("Caesar Cipher")
        master.option_add('*Font', 'Goergia 12') #font for all widgets
        master.option_add('*Background', 'ivory2')#background of all widgets
        master.option_add('*Label.Font', 'helvetica 14') #font for all labels
        master.geometry('835x700+100+100')  #w,h,x,y (top left corner)
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
        
        #frame 1 - Header ----- Adding title and formatting the frame1
        
        frame1 = Frame(master, bg = 'orange')
        frame1.pack(fill = 'both', expand = False) #fills window
            
        icon = PhotoImage(file = 'cipher.gif')
        lbl_icon = Label(frame1)
        lbl_icon.config(image = icon)
        lbl_icon.image = icon
        lbl_icon.pack(side = LEFT, padx = 10, pady = 10)
        label_heading = Label(frame1)
        label_heading.config(text = 'Caesar Cypher Cryptography',font=('helvetica 20 bold'), bg = 'orange') #override default
        label_heading.pack(side=LEFT, padx =10, pady=10)

        
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
        frameA = Frame(master, bg = 'orange')
        frameA.pack(fill = 'both', expand = False) #fills window
        asym_label = Label(frameA, text = 'Asymmetric and Symmetric Encryption (Info)',font = ('arial', 13, 'bold'))
        
        btn_asym = Button(frameA, bd = 5, 
                  fg = "white", font = ('arial', 12, 'bold'), 
                    width = 5, text = "Open", bg = "#02231C", 
                   command = openweb).pack(padx=10 , pady=10, side=RIGHT) 
        asym_label.config(bg='orange',fg ='#0000ff')
        asym_label.pack(side = RIGHT)
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------#        
        
        #Frame2 --> user input area
        frame2 = Frame(master, bg='blue')
        frame2.pack(fill = 'both', expand = True)
        frame2a=Frame(frame2, relief=GROOVE, borderwidth=1, bg='#0444BF')
        frame2a.pack(side=LEFT, fill = Y)
        
        #
        label_2a_heading = Label(frame2a)
        label_2a_heading.config(borderwidth=0,text = "Enter your text:",bg='#0444BF',font = ('arial', 13, 'bold'))
        label_2a_heading.pack(padx=10, pady=10)
        #
        self.txtMsg = Text(frame2a, font = ('arial', 16, 'bold'), 
              bd = 5, insertwidth = 4, bg = "powder blue", width =15, height =8, wrap = WORD)
        self.txtMsg.pack(padx=10, pady=10)
        #
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
        #frame2ab ---------- Check boxes for encryption type
        frame2ab=Frame(frame2, relief=GROOVE, borderwidth=1, bg='#0584F2')
        frame2ab.pack(side = LEFT, fill =Y)
        #
        label_2b_heading = Label(frame2ab)
        label_2b_heading.config(borderwidth=0, text = 'Encryption Type?',bg='#0584F2',font = ('arial', 13, 'bold'))
        label_2b_heading.pack(padx=10, pady=10)
        #
        self.caesar_cipher = BooleanVar(master)
        cb_1=Checkbutton(frame2ab, text='Caesar Cipher', variable=self.caesar_cipher)
        cb_1.pack(anchor=W,padx=10, pady=10)
        #
        self.vegenere_cipher = BooleanVar(master)
        cb_2=Checkbutton(frame2ab, text='Vegènere Cipher', variable=self.vegenere_cipher)
        cb_2.pack(anchor=W,padx=10, pady=10)
        #
        self.trans_cipher = BooleanVar(master)
        cb_3=Checkbutton(frame2ab, text='Vernam Cipher', variable=self.trans_cipher)
        cb_3.pack(anchor=W,padx=10, pady=10)

#-----------------------------------------------------------------------------------------------------------------------------------------------------#
        #frame2b ----------- Encrypt / Decrypt
        frame2b=Frame(frame2, relief=GROOVE, borderwidth=1, bg='#0AAFF1')
        frame2b.pack(side = LEFT, fill =Y)
        #
        label_2b_heading = Label(frame2b)
        label_2b_heading.config(borderwidth=0, text = 'Encrypt or Dycrypt? ',bg='#0AAFF1',font = ('arial', 13, 'bold'))
        label_2b_heading.pack(padx=10, pady=10)
        #
        self.encrypt = BooleanVar(master)
        cb_1=Checkbutton(frame2b, text='Encrypt', variable=self.encrypt)
        cb_1.pack(anchor=W,padx=10, pady=10)
        #
        self.decrypt = BooleanVar(master)
        cb_2=Checkbutton(frame2b, text='Decrypt', variable=self.decrypt)
        cb_2.pack(anchor=W,padx=10, pady=10)

#-----------------------------------------------------------------------------------------------------------------------------------------------------#
        
        #Frame 2c (KEY entry box)
        #
        frame2c = Frame(frame2, relief=GROOVE, borderwidth =1, bg = '#73C0F4')
        frame2c.pack(side=LEFT, fill = Y)
        #
        label_2c_heading = Label(frame2c)
        label_2c_heading.config(borderwidth = 0, text = 'Key: ',bg='#73C0F4',font = ('arial', 13, 'bold'))
        label_2c_heading.pack(anchor= W, padx = 10, pady = 10, side = TOP)
        self.KEY = StringVar()
        self.txtkey = Entry(frame2c, font = ('arial', 16, 'bold'),  
                                textvariable = self.KEY, bd = 5, insertwidth = 4, bg = "powder blue", justify = 'right') 
        self.txtkey.pack(padx=10,pady=10)


        #
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
        # Creating buttons
        btnReset = Button(frame2c, bd = 5, 
                  fg = "white", font = ('arial', 16, 'bold'), 
                    width = 5, text = "Reset", bg = "#02231C", 
                   command = Reset).pack(padx=10 , pady=10, side=BOTTOM) 
        btngraph = Button(frame2c, bd = 5, 
                  fg = "white", font = ('arial', 16, 'bold'), 
                    width = 5, text = "Graph", bg = "#02231C", 
                   command = graph).pack(padx=10 , pady=10, side=BOTTOM)  
        btnRun = Button(frame2c, bd = 5, 
                  fg = "white", font = ('arial', 16, 'bold'), 
                    width = 5, text = "RUN", relief = RAISED,bg = '#02231C',
                   command = main_cipher_pro).pack(padx=10 , pady=10, side=BOTTOM)        
        #btn_generate = Button(frame2c)
        #btn_generate.config(relief = RAISED,width = 5,bd=5, borderwidth=5, text = 'RUN ',command = main_cipher_pro)
        #btn_generate.pack(padx =10, pady = 10, side = BOTTOM)
#-----------------------------------------------------------------------------------------------------------------------------------------------------#        
        #FRAME 3 -------- Result Box
        frame3 = Frame(master, bg = 'blue')
        frame3.pack(fill = 'both', expand = True)
        label_3a=Label(frame3)
        label_3a.config(borderwidth=0, text='Result: ',bg='blue',fg='yellow',font=('arial',14,'bold'))
        label_3a.pack(side=LEFT)
        #
        self.Result = StringVar()
        txtService = Entry(frame3, font = ('arial', 16, 'bold'),  
             textvariable = self.Result, bd = 5, insertwidth = 4, 
                       bg = "powder blue", justify = 'right', width = 50) 
        txtService.pack(padx=10, pady=10, side = LEFT)  

#-----------------------------------------------------------------------------------------------------------------------------------------------------#        
#
# Combining all the results and running the main program.
        
def main():
    root=Tk()
    app=cipher(root)

    root.mainloop()

if __name__ == "__main__":
    main()        


