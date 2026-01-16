from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import Api


class NLPApp:
    def __init__(self):

        #object of api class
        self.dbo=Database()
        self.api=Api()

        # login ka gui load karna
        self.root = Tk()
        self.root.title("NLPApp")
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry("400x600")
        self.root.configure(bg="#21395C")

        #login gui
        self.login_gui()

        self.root.mainloop()

    def login_gui(self):

        #clear function to clear n
        self.clear()

        #npl heading
        heading=Label(self.root,text="NLPApp",bg="#21395C",fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',20,'bold'))

        #first label for email
        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        #Entry for text
        self.email_input =Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        # first label for password
        label2=Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        # Entry for text
        self.password_input = Entry(self.root,show='*',width=50)
        self.password_input.pack(pady=(5,10),ipady=4)

        #login btn and perform login
        login_btn=Button(self.root,text="Login",width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        #label 3
        label3=Label(self.root,text='Not a Member?')
        label3.pack(pady=(20,10))

        #redirect btn and register page
        redirect_btn=Button(self.root,text="Register Now",command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def register_gui(self):
        self.clear()

        #heading
        heading = Label(self.root, text="NLPApp", bg="#21395C", fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 20, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, show='*', width=50)
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text="Register", width=30, height=2,command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a Member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Login Now", command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def perform_registration(self):
        name= self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()

        #obj call and response check
        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo("Success",'Registration Successful. You can login now')
        else:
            messagebox.showinfo('Error',"Email already exists")

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response= self.dbo.search(email, password)
        if response:
            messagebox.showinfo('success','Login Successful')
            #here the new method
            self.home_gui()
        else:
            messagebox.showinfo('error','Incorrect Password/Email')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#21395C", fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 20, 'bold'))

        sentiment_btn = Button(self.root, text="Sentiment Analysis", width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text="Named Entity Recognition", width=30, height=4,
        command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text="Emotion Prediction", width=30, height=4,
        command=self.perform_registration)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text="Logout", command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#21395C", fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading = Label(self.root, text="Sentiment Analysis", bg="#21395C", fg='white')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(20, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text="Analyze", command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='',bg="#21395C",fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text="Go Back", command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result=self.api.sentiment(text)

        self.sentiment_result['text']=result

    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text="NLPApp", bg="#21395C", fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading = Label(self.root, text="Named Entity Recognition", bg="#21395C", fg='white')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(20, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter the text to search')
        label2.pack(pady=(20, 10))

        self.ner_search_input = Entry(self.root, width=50)
        self.ner_search_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(self.root, text="Analyze", command=self.do_ner_analysis)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg="#21395C", fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 16))


        goback_btn = Button(self.root, text="Go Back", command=self.home_gui)
        goback_btn.pack(pady=(10, 10))


    def do_ner_analysis(self):
        search = self.ner_search_input.get()
        # search_result = self.api.s( search)
        text = self.ner_input.get()
        result = self.api.ner(text,search)
        self.ner_result['text']=result


        self.sentiment_result['text'] = result





nlp = NLPApp()