# Quiz Application

# 1. Title and Developer Name
print("Welcome to Quiz Application")
print("Developer: China Bea\n")

# 2. Name of the user and welcome screen 
def welcome_screen(name):
    print(f"Welcome, {name}!")

# 4. Menu for Answer and Quit
def display_menu():
    print("\nMenu:")
    print("1. Answer the Quiz")
    print("2. Quit")
    choice = input('Enter "Answer" for option 1, or "Quit" for option 2: ')
    return choice

# Function to calculate the score
def calculate_score(answers, user_answers):
    score = sum([1 for i, answer in enumerate(answers, 1) if answer.lower() == user_answers.get(i, "").lower()])
    return score

# 5. List of Questions
questions = [
"Which company developed Python?", 
    "What is the official integrated development environment (IDE) for Python on Android?", 
    "What programming language is Pydroid primarily designed for?", 
    "Which Python function is used to get user input?",
    "What does the acronym IDE stand for?",
    "In Python,what symbol is used for a single-line comment?", 
    "What is the purpose of the print() function in Python?", 
    "Which built-in function is used to get the length of a list in Python?", 
    "Which Python data type is used to store a sequence of characters?", 
    "What is the default file extension for Python source code files?" 
]

# List of Correct Answers
answers = ["PSF",
# (Python Software Foundation)
"Pydroid", "Python", "input()",
"Integrated Development Environment",  
 "#", "Output", "len", "String",".py" ]
 
#3. Loop
# Main Program 
while True:
    name = input("Type your name: ")
    welcome_screen(name)
    
    while True:
        choice = display_menu()
        
        if choice == "Answer":
            user_answers = {}
            for i, question in enumerate(questions, 1):
                user_answer = input(f"{i}. {question} \nAnswer: ")
                user_answers[i] = user_answer
            
            score = calculate_score(answers, user_answers)
            #6. Display the Score of the user
            print(f"\nYour Score: {score}/10")
        
        elif choice == "Quit":
            print("\nThank you. Have a nice day!")
            exit()
        
        else:
            print('Invalid choice. Please enter "Answer" for option 1, or "Quit" for option 2.')
