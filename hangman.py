import math
import random
import time

incorrects = int(input("how many incorrects do you want? (1 - 25)"))

list_of_words = ["cat", "dog", "animals", "uwu", "spam", "bungee", "swallow",
                 "American","among","amount","analysis","animal","another","answer","anything","appear"]

valid_answer = True
while(valid_answer):
    if(incorrects < 1 or incorrects > 25):
        print("not a valid answer")
        incorrects = int(input("how many incorrects do you want? (1 - 25)"))
    else:
        valid_answer = False

random_int = random.randint(0, len(list_of_words) - 1)
print("selecting word...")

time.sleep(3)

word = list_of_words[random_int]

length_word = len(word)
covered_word = "*" * length_word

while ("*" in covered_word) and (incorrects != 0):
    print("Word: {}".format(covered_word))
    print("Attempts Remaining: {}".format(incorrects))
    character_input = input("What character do you guess: ")
    
    incorrects -= 1

    word_make = ""
    ## for covered_word
    char_count = 0

    for character in word:
        if(character_input == character):
            word_make += character_input
        elif (covered_word[char_count] != "*"):
            word_make += covered_word[char_count]
        else:
            word_make += "*"
        char_count += 1
    covered_word = word_make

print("the word is {}".format(word))
    
    
        
