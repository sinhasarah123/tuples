class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + ": " + self.meaning
    flashcard=[]
    print("Welcome to the Flashcard App!")
    while(True):
        word=input("enter your word:")
        meaning=input("enter the meaning of the word:")
        option=int(input("enter 1 to add more flashcards or 0 to stop:"))
        if (option):
            break
        
        print("\nYour Flashcards:")
        for i in flashcard:
            print(i)
        