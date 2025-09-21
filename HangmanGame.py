import random

someWords = '''monkey crocodile dog cat cow ostrich camel fox rabbit Elephant
 pig turtle penguin goat sheep tiger rat donkey horse wolf zebra panda snake bear 
 giraffe eagle panther deer squirrel chimpanzee jackal leopard raccoon'''
words = someWords.split()            # split on any whitespace
word = random.choice(words).strip().lower()  # normalize: remove whitespace + lowercase

print('Guess the word! HINT: word is a name of an animal\n')

# show blanks
print(' '.join('_' for _ in word))
print()

guessed = set()                      # store guessed letters
chances = len(word) + 2              # you can choose another fixed number like 6
won = False

try:
    while chances > 0 and not won:
        guess = input('Enter a letter to guess: ').strip().lower()

        if not guess.isalpha() or len(guess) != 1:
            print('Please enter a single alphabet letter.')
            continue

        if guess in guessed:
            print('You have already guessed that letter.')
            continue

        guessed.add(guess)

        if guess in word:
            print('✅ Correct!')
        else:
            chances -= 1
            print(f'❌ Wrong guess! Chances left: {chances}')

        # print current progress
        progress = ' '.join([c if c in guessed else '_' for c in word])
        print(progress)

        # win condition: all unique letters in the word have been guessed
        if set(word).issubset(guessed):
            print('\nThe word is:', word)
            print('Congratulations!! YOU WON 🥳🥳')
            won = True
            break

    if not won:
        print('\nYou lost! Try again ❌')
        print('The word was:', word)

except KeyboardInterrupt:
    print('\nTRY AGAIN!! 🙃')