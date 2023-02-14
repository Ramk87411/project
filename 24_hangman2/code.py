import random
import word 
import life_stage

# print(word_list.word_list) # test wordlist import
print(life_stage.logo) #test import logo 
print ("Welcome to hangman Game! ")
choosen = random.choice(word.word_list).lower()

end_of_lives = False
lives = 6
# print(f"Choosen word is: {choosen}") # to keep track of program 


#2nd stage  create blank 
display = []
for i in range (len(choosen)): # to create the _ list of choosen word
    display += "_"
# print(display)

while not end_of_lives:
    user_input = input("Guess a letter! ").lower()
    
    for position in range(len(choosen)):
        letter = choosen[position]
        if letter == user_input:
            display[position] = letter
    
    if user_input not in choosen:
        print(f"You have guessed {user_input}, That's not right word .you will loose life")
        lives -= 1
        if lives == 0:
            end_of_lives = True 
            print("you lose.")
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_lives = True
        print("You Win.")
    
    print(life_stage.stages[lives])



