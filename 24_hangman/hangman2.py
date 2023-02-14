import random
word_list = ["Ram","Krishna","Shivam"]
choosen = random.choice(word_list)
print(f"choosen word is {choosen}")

display = []
for letter in choosen:
    display += "_"
print(display)

end_of_game = False
while end_of_game==False:
    user_input = input("Guess a letter! ").lower()
    for position in range(len(choosen)):
        letter = choosen[position]
        print(f"Current position : {position}\n Current letter :{letter}\n Guesses letter :{user_input}")
        if letter == user_input:
            display[position] = letter
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You win")