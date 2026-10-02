def start(quiz): # Question layout: {"Question": "How old is the sun?", "Answers": ("Dog", "I don't know", "At least one year"), "Answer", 2}
    point_counter = 0
    for question in quiz:
        print(question["Question"])

        print("\nYour choices for answer are...")
        answer_count = 0
        for answer in question["Answers"]:
            print(f"Answer {answer_count+1}: {answer}")
            answer_count += 1

        while True:
            try:
                user_answer = int(input("\nEnter answer your answer: "))-1 #-1 to account for python counting from 0
                break
            except:
                print("The answer you entered was not detected as a valid integer. Please only enter the number associated with your answer.")

        if user_answer == question["Answer"]:
            print("\nCorrect! +1 point!")
            point_counter += 1
        else:
            print("Incorrect...")
    return point_counter
