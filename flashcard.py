class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word +'('+self.meaning+')'

flash=[]
print("Welcome to flashcard application")
#the followng loop will be repeated until user stops adding flashcards
while(True):
    word=input("enter the name you want to add to flashcard:")
    meaning=input("Enter the meaning of the word:")
    flash.append(flashcard(word,meaning))
    print("flashcard added successfully")
    option=int(input("enter 0,if you want to add another falshcard otherwise eneter 1:"))

    if(option):
        break

#printing all the flashcards
print("\nYour flashcards:")
for i in flash:
    print(">",i)