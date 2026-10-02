import quiz_runner
import menu
from quizzes import quizzes

points = [0,0] #First position is points earned, second position is total points that could have been earned.

print("Welcome!")

while True:
    choice = menu.display(quizzes)
    if choice == "q":
        break
    else:
        points[1] += len(quizzes[choice]["Questions"])
        points[0] += quiz_runner.start(quizzes[choice]["Questions"])
        
print(f"{points[0]} points earned of a possible {points[1]}!")
