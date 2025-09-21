import random
from collections import Counter
someWords = '''monkey crocodile dog cat cow  ostrich camel fox rabit Elephant pig turtle penguin goat sheep tiger rat donkey horse wolf zebra 
panda snake bear giraffe eagle panther deer squirrel chimpanzee jackal leopard raccoon  '''
someWords = someWords.split(' ')
 #randomly choose a secret word from our "somewords" list
word = random.choice(someWords)
if __name__ == '__main__':
    print ('Guess the word! HINT: word is a name of a animal')

    for i in word:
        #for printing  the empty spaces for letters of the word
        print('_',end=' ')
    print()

    playing = True
    #list for storing the letters guessed by the player
    letterGussed = ''
    chances = len(word) + 2
    # choice = 0
    flag = 0
    try:
        while(chances !=0) and flag == 0:
            # Flag is updated when the word is correctly gussed 
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue
            #validation of the guess
            if not guess.isalpha():
                print('Enter only a letter ')
                continue
            elif len(guess) > 1:
                print('only a SINGLE Letter!!')
                continue
            elif guess in letterGussed:
                print('you have already guessed that letter')
                continue
            elif guess not in word:
                chances -= 1
                print(f"❌ Wrong guess! Chances left: {chances}")
                continue

            #if letter is gussed correctly
            if guess in word:
                 # add the guessed letter
                   letterGussed += guess

                # print the word with guessed letters
            correct = True
            for char in word:
                if char in letterGussed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')
                    correct = False
                        #if user has gussed all the letters 
            if(Counter(letterGussed)== Counter(word)):
                        #the game is end
                        print("The word is : ",end=' ')
                        print(word)
                        flag =1
                        print("Congratulations!! YOU WON 🥳🥳")
            
                        break #to break out of the for loop
                        
            else:
                     print('_',end=' ')

        #if user has use all of his chances
        if chances <=0 and (Counter(letterGussed) != Counter(word)):
            print()
            print('You lost! Try again  ❌..')
            print("The word was {}".format(word))
    except KeyboardInterrupt:
        print()
        print('TRY AGAIN!!🙃🙃')        
        exit()
