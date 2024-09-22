
class Words:
    def __init__(self,vocabulary,meaning):
        self.vocabulary = vocabulary
        self.meaning = meaning
class Dictionary:
    def __init__(self) -> None:
        self.dictionary ={}
    def add_word(self,vocabulary,meaning):
        if vocabulary in self.dictionary:
            print(f"this {vocabulary} has been in dictionary")
        else:
            self.dictionary[vocabulary] = Words(vocabulary,meaning)
    def edit_word(self,old_word):
        while True:
            if old_word in self.dictionary:
                new_meaning = input("Input new meaning: ")
                self.dictionary[old_word].meaning = new_meaning
                print(f"This {old_word} is {new_meaning}")
            else:
                print(f"This {old_word} not in dictionary")
            break
    def search_word(self,vocabulary):
        query = vocabulary.lower()
        found = False
        for word in self.dictionary.values():
            if query in word.vocabulary.lower():
                print(f"{word.vocabulary}:{word.meaning}")
                found = True
            if not found:
                print(f"{query} not in dictionary")
    def list_words(self):
       for word in self.dictionary.values():
            print(f"{word.vocabulary}: {word.meaning}")
       
    def delete_word(self,vocabulary):

        if vocabulary in self.dictionary:
            del self.dictionary[vocabulary]
        else:
            print( f"this {vocabulary} not in dictionary")

class App:
    def __init__(self) -> None:
        self.dictionary = Dictionary()
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
                word = input("Input your word you want to edit: ")
                self.dictionary.edit_word(word)
            if choice == '4':
                delete_word = input("Input word you want delete: ")
                self.dictionary.delete_word(delete_word)
            if choice == '5':
                self.dictionary.list_words()
            if choice == '6':
                break
App().menu()