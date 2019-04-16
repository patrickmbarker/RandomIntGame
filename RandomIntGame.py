#This game picks a random number and you have to guess it
import random

playAgain = True

print('Let\'s play a game!')
print('Start by telling me your name.')
name = input()

print('Hey, ' + name + '!')

while playAgain:
    guessesTaken = 0

    correctNum = random.randint(1, 20)    
    print('I am thinking of a number between 1 and 20.')
    print('Can you guess it in 5 tries?')

    for gussesTaken in range(5):
        guessesTaken = guessesTaken + 1
        print('What is your guess?')
        guess = input()
        guess = int(guess)

        if guess < correctNum:
            print('Sorry. That is incorrect. You were a little low.')

        if guess > correctNum:
            print('Sorry. That is incorrect. You were a little high.')

        if guess == correctNum:
            break

    if guess == correctNum:
        guessesTaken = str(guessesTaken)
        print('Good job! You guessed correctly in only ' + guessesTaken + ' tries.')

    if guess != correctNum:
        correctNum = str(correctNum)
        print('You did not guess correctly in time.')
        print('The number I was thinking of was: ' + correctNum + '.')

    print('Would you like to play again?')
    answer = input()
    if answer == 'Yes':
        playAgain = 1
    if answer == 'No':
        print('Thanks for playing!')
        playAgain =0
    
    

      

      
      
