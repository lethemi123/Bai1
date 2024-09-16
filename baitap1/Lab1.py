
        

class words:
    def __init__(self,vocabulary,meaning):
        self.vocabulary = vocabulary
        self.meaning = meaning
class dictionary:
    def __init__(self) -> None:
        self.dictionary ={}
    def add_word(self,vocabulary,meaning):
        if vocabulary in self.dictionary:
            print(f"this {vocabulary} has been in dictionary")
        else:
            self.dictionary[vocabulary] = words(vocabulary,meaning)
    def edit_word(self,old_word, new_word,new_meaning):
        if old_word in self.dictionary:
            del self.dictionary[old_word]
            self.dictionary[new_word,new_meaning] = words(new_word,new_meaning)
            print( f"Have edit done{old_word} to {new_word} and{new_meaning}")
        else:
            print(f"this {old_word} not in dictionary")
    def search_word(self,vocabulary):
        if vocabulary in self.dictionary:
            print (f"{vocabulary}: {self.dictionary[vocabulary].meaning}")
        else:
            print (f"this {vocabulary} not in dictionary")
    def list_words(self):
       for word in self.dictionary.values():
            print(f"{word.vocabulary}: {word.meaning}")
       
    def delete_word(self,vocabulary):

        if vocabulary in self.dictionary:
            del self.dictionary[vocabulary]
        else:
            print( f"this {vocabulary} not in dictionary")

class app:
    def __init__(self) -> None:
        self.dictionary = dictionary()
    def menu(self): 
        while True:     
            print("1 Search word")
            print("2 Add word")
            print("3 Edit word")
            print("4 Delete word")
            print("5 Show dictionary")
            print("6 Exit app")
            choice = input("Input choice 1 -> 6: ")
            if choice == '1':
                search_word = input("Input word to search: ")
                self.dictionary.search_word(search_word)
            if choice == '2':
                word = input("New word: ")
                meaning = input("New meaning: ")
                self.dictionary.add_word(word,meaning)
            if choice == '3':
                old_word = input("Input word you want edit in dictionary: ")
                new_word = input("Input Word: ")
                new_meaning = input("Input meaning: ")
                self.dictionary.edit_word(old_word,new_word,new_meaning)
            if choice == '4':
                delete_word = input("Input word you want delete: ")
                self.dictionary.delete_word(delete_word)
            if choice == '5':
                self.dictionary.list_words()
            if choice == '6':
                break
if __name__ == "__main__":
    S = app()
    S.menu()
#comment
def __str__(self):
    return f"{self.name()}"