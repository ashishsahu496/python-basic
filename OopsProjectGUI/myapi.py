import nlpcloud

class Api:

    def sentiment(self,text):
        self.text=text
        client = nlpcloud.Client("gpt-oss-120b", "0b9d561c1dc95be8b3ebdc594c809d815201dd99", gpu=True)
        response = client.sentiment(text, target="NLP Cloud")
        return response


    def ner(self,text,search):
        self.text = text
        self.search_text = search
        client = nlpcloud.Client("gpt-oss-120b", "0b9d561c1dc95be8b3ebdc594c809d815201dd99", gpu=True)

        response=client.entities(text,search)
        print(response)

    def language_detect(self,text):
        self.text=text

        client = nlpcloud.Client( "python-LangDetect","0b9d561c1dc95be8b3ebdc594c809d815201dd99", gpu=False)
        response=client.lang_detection(text)
        print(response)

# obj=Api()
# obj.ner("hello bhaiya ji","bhayaji")
ob=Api()
ob.language_detect("Python जलद प्रोटोटायपिंगसाठी तसेच उत्पादनासाठी तयार सॉफ्टवेअर विकासासाठी वापरला जाऊ शकतो.")



