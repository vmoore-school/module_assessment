def display(quizzes):
    print("Please select a quiz to take:\n")
    x = 0
    for quiz in quizzes:
        print(f'Quiz {x+1}: {quizzes[x]["Category"]}')
        x+=1
    
    
    print("\nOr to quit, type q")
    while True:
        selection = input("Your choice: ")
        if selection.lower() != "q":
            try:
                selection = int(selection)-1
                return selection
            except:
                print("Your answer wasn't recognised. Please enter a valid integer, or q to quit.\n")
        else:
            return selection
