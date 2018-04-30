from reverse_func import *




while True:
    word = input("Please enter a word or sentence to be reversed:   ")
    if word.lower() == "quit" or word.lower() == "q":
        break
    else:
        print(reverse(word))
    