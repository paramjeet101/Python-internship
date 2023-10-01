from tkinter import *
import smtplib, ssl

root=Tk()
root.title("Gmail Sender")
root.geometry("800x500")
root.config(bg="#333333")

def send_msg():
    try:
       
        username=text1.get()
        password=text2.get()
        to=text3.get()
        subject=text4.get()
        body=text5.get()
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = username
        msg['To'] = to
        msg['Body']=body
        if username=="" or password=="" or to=="" or subject=="" or body=="":
               message_label.config(text="Plz fill all the details to send.")
           
        else:
            server = smtplib.SMTP('smtp.gmail.com', 587) 
            server.ehlo()
            server.starttls()
            server.login(username,password)  
            server.sendmail(username, to, msg.as_string())  
            server.quit()
            
    except:
         message_label.config(text="Error while sending message.")

def reset_msg():
    name_input.delete(0,'end'),
    password_input.delete(0,'end'),
    to_entry.delete(0,'end'),
    subject_entry.delete(0,'end'),
    body_entry.delete(0,'end')
    
text_label=Label(root,text="Fill The Form To Send Mail",font=("Times",24))
text_label.place(relx=0.30,rely=0.05)
name_label=Label(root,text="Enter Your Gmail:",font=("Times",20))
name_label.place(relx=0.20,rely=0.2)
input_label=Label(root,text="Enter Your Password:",font=("Times",20))
input_label.place(relx=0.20,rely=0.3)
to_label=Label(root,text="To:",font=("Times",20))
to_label.place(relx=0.20,rely=0.4)
subject_label=Label(root,text="Subject:",font=("Times",20))
subject_label.place(relx=0.20,rely=0.5)
body_label=Label(root,text="Body:",font=("Times",20))
body_label.place(relx=0.20,rely=0.6)
message_label=Label(root,text="",font=("Times",20))
message_label.place(relx=0.37,rely=0.72)

text1=StringVar()
text2=StringVar()
text3=StringVar()
text4=StringVar()
text5=StringVar()

name_input=Entry(root,textvariable=text1,font=("Times",20))
name_input.place(relx=0.5,rely=0.2)
password_input=Entry(root,textvariable=text2,font=("Times",20))
password_input.place(relx=0.5,rely=0.3)
to_entry=Entry(root,textvariable=text3,font=("Times",20))
to_entry.place(relx=0.5,rely=0.4)
subject_entry=Entry(root,textvariable=text4,font=("Times",20))
subject_entry.place(relx=0.5,rely=0.5)
body_entry=Entry(root,textvariable=text5,width=35,font=("Times",20))
body_entry.place(relx=0.5,rely=0.6)

send_btn=Button(root,text="Send",command=send_msg)
send_btn.place(relx=0.40,rely=0.82)
reset_btn=Button(root,text="Reset",command=reset_msg)
reset_btn.place(relx=0.50,rely=0.82,)

root.mainloop()

