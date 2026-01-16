import nlpcloud


class NLPApp:
    def __init__(self):


       self.__database={}
       self.__first_menu()

    def __first_menu(self):
        first_input = input("""
                Hi ! how would you like to proceed ?
                1. Not a member? Register
                2. Already a member? Login
                3.Galti se aa gaye? Exit
                """)


        if first_input=='1':
            self.__register()
        elif first_input=='2':
            self.__login()
        else:
            exit()

    def __second_menu(self):
        second_input = input("""
                Hi ! how would you like to proceed ?
                1. NER
                2. Language Detection
                3. Sentiment Analysis
                4. Logout
                """)

        if second_input=='1':
            self.__ner()
        elif second_input=='2':
            self.__language_detection()
        elif second_input=='3':
            self.__sentiment_analysis()
        else:
            exit()

    def __register(self):
        name = input("Enter your name : ")
        email = input("Enter your email : ")
        password = input("Enter your password : ")

        if email in self.__database:
            print("email already registered")
        else:
            self.__database[email]=[name,password]
            print("Registered successfull,now Login")
            self.__login()

    def __login(self):
        email=input("Enter your email : ")
        password=input("Enter your password : ")

        if email in self.__database:
            if self.__database[email][1]==password:
                print("Login Successful")
                self.__second_menu()
                #self.__first_menu()
            else:
                print("wrong password")
                self.__login()
        else:
            print("email not registered")
            self.__first_menu()

    def __ner(self):
        para=input("enter the paragraph")
        search_term=input("what would you like to search for? ")

        client = nlpcloud.Client("gpt-oss-120b", "0b9d561c1dc95be8b3ebdc594c809d815201dd99", gpu=True)
        response=client.entities(para,searched_entity=search_term)
        print(response)

    def __language_detection(self):
        para=input("enter the langauge  to detection ")
        client = nlpcloud.Client("python-langdetect", "0b9d561c1dc95be8b3ebdc594c809d815201dd99", gpu=False)
        response=client.lang_detection(para)
        print(response)

    def __sentiment_analysis(self):

        para = input("enter the paragraph : ")

        client = nlpcloud.Client("gpt-oss-120b", "0b9d561c1dc95be8b3ebdc594c809d815201dd99", gpu=True)
        responce=client.sentiment(para)
        print(responce)
        print("*"*50)


        # l=[]
        #
        # for i in responce['scored_labels']:
        #     l.append(i['score'])
        #
        # index = sorted(list(enumerate(l)),key=lambda x:x[1],reverse=True)[0][0]
        # print(['scored_labels'][index]['label'])


obj = NLPApp()
