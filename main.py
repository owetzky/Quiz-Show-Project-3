# Project Requirements:

# display the title and rules of the game 
# use ASCII art for the title 
# store at least 3 questions in a tuple, store answers in a separate tuple => Index Notation Examples
# use a loop to display the questions to the user from the "questions tuple"
# question inputs must be T or F, use input validation to ensure the user can only input valid answers (T or F), re-ask user if incorrect value entered (not a T or F)
# keep track of the questions the user answered correctly 
# at the end of the quiz display the number of questions the user answered correctly 

# ASCII Art 
print(r"""
 $$$$$$\  $$\   $$\ $$$$$$\ $$$$$$$$\       $$$$$$$$\ $$$$$$\ $$\      $$\ $$$$$$$$\ 
$$  __$$\ $$ |  $$ |\_$$  _|\____$$  |      \__$$  __|\_$$  _|$$$\    $$$ |$$  _____|
$$ /  $$ |$$ |  $$ |  $$ |      $$  /          $$ |     $$ |  $$$$\  $$$$ |$$ |      
$$ |  $$ |$$ |  $$ |  $$ |     $$  /           $$ |     $$ |  $$\$$\$$ $$ |$$$$$\    
$$ |  $$ |$$ |  $$ |  $$ |    $$  /            $$ |     $$ |  $$ \$$$  $$ |$$  __|   
$$ $$\$$ |$$ |  $$ |  $$ |   $$  /             $$ |     $$ |  $$ |\$  /$$ |$$ |      
\$$$$$$ / \$$$$$$  |$$$$$$\ $$$$$$$$\          $$ |   $$$$$$\ $$ | \_/ $$ |$$$$$$$$\ 
 \___$$$\  \______/ \______|\________|         \__|   \______|\__|     \__|\________|
""")

# display quiz title and rules 
print("Welcome to Quiz Time!")
print("Please answer each question with a 'T' for TRUE or a 'F' for FALSE. At the end of the quiz, the number of questions you answered correctly, will be displayed!")
print()
print("Goodluck!")
print()

#variable (correct answers) tracking, tuple for questions and answers 
correct = 0
numberOfQuestions = 3 
number = 0 

questions = ('Q1. There are exactly 193 countries on Earth?', 'Q2. There are 51 states in the US?', 'Q3. Texas has the highest state population in the US?')
answers = ('T', 'F', 'F')

# ask question, prompt user for input, validate input 
for question in questions:
  print(question)
  userGuess = input("Enter 'T' for TRUE, 'F' for FALSE: ")
  if(userGuess == answers[number]):
    correct += 1
  while(userGuess != 'T' and userGuess != 'F'):
    userGuess = input("Invalid. Enter 'T' for TRUE, 'F' for FALSE: ")
    print(question)
  number += 1 

# display user results using f-string 
print()
print(f"You answered {int(correct)} out of {len(questions)} questions correctly! Thanks for playing!") 