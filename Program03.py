print("Let's play the Mystery code game!")

import random
code = random.randrange (1000,10000)
print("Here are the digits", code, "that are valid guesses.")
chances = 5 
guess = int(input(f'Enter a 4 digit number and you have {chances} guesses: '))
if guess == code:
  print("Congratulations, you won!")
else:
  guesses = 0
  while guess != code and chances:
    guesses += 1
    chances -= 1
    digit = 0
    guess = str(guess)
    code = str(code)
    correct = ['X'] * 4
    for i in range (0,4):
      if guess[i] == code[i]:
        digit += 1
        correct[i] = code[i]
    if digit < 4 and digit > 0 and chances:
      print("You guessed", digit, "number correctly.")
      print('Here are the numbers you have guessed: ')
      for num in correct:
        print(num, end="")
      print('\n')
      guess = int(input(f'Enter a 4 digit number and you have guess {chances} left: '))
    elif digit == 0 and chances:
      print("You guessed ",chances," correctly")
      guess = int(input(f'Enter a 4 digit number and you have guess {chances} left: '))
  if guess == code:
    print("Congratulations, you won!")
  if chances == 0:
     print("Sorry, you loose!")
