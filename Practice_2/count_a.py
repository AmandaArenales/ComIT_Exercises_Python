"""Write an algorithm that requests the reading of a series of individual characters 
and count how many times the letter "a" is entered. The user ends by entering the "$" symbol."""

def count_a():
    character = input("Please, insert the first individual character: ")
    list_characters = []
    list_characters.append(character)

    while character != "$":
        character = input("Please, insert an individual character or $ symbol to stop: ")
        list_characters.append(character)

    count_a = list_characters.count("a")

    print(f"In this list {list_characters} the letter a was entered {count_a} times.")

count_a()



    
