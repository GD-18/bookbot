def count(file):
    return len(file)

def count_let(file:str)->dict:
    letter_count = {}
    for word in file:
        cur_word = word.lower()
        for letter in cur_word:
            if letter not in letter_count:
                letter_count[letter]=0
            letter_count[letter] += 1
    return letter_count

def get_book(path):
    with open(f"{path}") as f:
        return f.read()

def print_report(words_list : list[str],word_count :int,let_dict : dict) -> None:
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("\n")
    for item in words_list:
        if item['let'].isalpha(): 
            print(f"The '{item['let']}' character was found {item['count']} times")
    print("--- End report ---")

def sort_list_by_count(letter_count_dict:dict)->list[dict]:
    cur_list = []
    
    def cmp(cur_dict:dict):
        return cur_dict["count"]

    for key in letter_count_dict:
        cur_list.append({"let":key,"count":letter_count_dict[key]})
    
    cur_list.sort(reverse=True,key=cmp)

    return cur_list

    

def main():
    book = get_book("books/frankenstein.txt")
    bookArr =book.split()
   
    word_count = count(bookArr)
    letters_dict = count_let(bookArr)
    letters = sort_list_by_count(letters_dict)
    

    print_report(letters,word_count,letters_dict)


main()

        
    
        

