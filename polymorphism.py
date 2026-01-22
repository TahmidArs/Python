class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language of India")
    def type(self):
        print("India is a developing country")
class England():
    def capital(self):
        print("London is the capital of England")
    def language(self):
        print("English is the most widely spoken language of England")
    def type(self):
        print("England is a developed country")
obj_ind=India()
obj_eng=England()
for country in (obj_ind, obj_eng):
    country.capital()
    country.language()
    country.type()