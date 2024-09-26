class Words:
    def __init__(self, vocabulary, meaning):
        self.vocabulary = vocabulary
        self.meaning = meaning

class Dictionary:
    def __init__(self) -> None:
        self.dictionary = {}

    def add_word(self, vocabulary, meaning):
        if vocabulary in self.dictionary:
            print(f"This {vocabulary} is already in the dictionary")
        else:
            self.dictionary[vocabulary] = Words(vocabulary, meaning)

    def edit_word(self, old_word):
        word = self.dictionary.get(old_word)
        if word:
            new_meaning = input("Input new meaning: ")
            word.meaning = new_meaning
            print(f"The word '{old_word}' now means: {new_meaning}")
        else:
            print(f"The word '{old_word}' is not in the dictionary")

    def search_word(self, vocabulary):
        query = vocabulary.lower()
        found = False
        for word in self.dictionary.values():
            if query in word.vocabulary.lower():
                print(f"{word.vocabulary}: {word.meaning}")
                found = True
        if not found:
            print(f"The word '{query}' is not in the dictionary")

    def list_words(self):
        for word in self.dictionary.values():
            print(f"{word.vocabulary}: {word.meaning}")

    def delete_word(self, delete_word):
        if delete_word in self.dictionary:
            del self.dictionary[delete_word]
            print(f"The word '{delete_word}' has been deleted.")
        else:
            print(f"The word '{delete_word}' is not in the dictionary")

class DictionaryApp:
    def __init__(self):
        self.dictionary = Dictionary()

    def run(self):
        while True:
            print("Menu:")
            print("1. Search for a word")
            print("2. Add a new word")
            print("3. Edit an existing word")
            print("4. Delete a word")
            print("5. List all words")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                search_word = input("Enter the word to search for: ")
                if search_word == "":
                    return "Search word is empty"
                self.dictionary.search_word(search_word)

            elif choice == '2':
                word = input("New word: ")
                if word == "":
                    return "Word is empty"
                meaning = input("New meaning: ")
                if meaning == "":
                    return "Meaning is empty"
                self.dictionary.add_word(word, meaning)

            elif choice == '3':
                word = input("Input the word you want to edit: ")
                if word == "":
                    return "Word is empty"
                self.dictionary.edit_word(word)

            elif choice == '4':
                delete_word = input("Input the word you want to delete: ")
                if delete_word == "":
                    return "Word is empty"
                self.dictionary.delete_word(delete_word)

            elif choice == '5':
                self.dictionary.list_words()

            elif choice == '6':
                break

            else:
                print("Invalid choice, please try again.")
