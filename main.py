import quiz_runner
import menu
from quizzes import quizzes

points = [0,0] #First position is points earned, second position is total points that could have been earned.
grade_boundaries = (
    (0.97, "A+"),
    (0.93, "A"),
    (0.90, "A-"),
    (0.87, "B+"),
    (0.83, "B"),
    (0.80, "B-"),
    (0.77, "C+"),
    (0.73, "C"),
    (0.70, "C-"),
    (0.67, "D+"),
    (0.65, "D"),
    (0, "F")
)

def surround_in_hashtags(to_hashtag):
    to_hashtag = str(to_hashtag)
    to_hashtag = "# " + to_hashtag + " #"
    return len(to_hashtag)*"#" + "\n" + to_hashtag + "\n" + len(to_hashtag)*"#"

print("Welcome!")

while True:
    choice = menu.display(quizzes)
    if choice == "q":
        break
    else:
        points[1] += len(quizzes[choice]["Questions"])
        points[0] += quiz_runner.start(quizzes[choice]["Questions"])

for grade in grade_boundaries[::-1]:
    if points[0] / points[1] >= grade[0]:
        final_grade = (grade[1], f"{int((round(points[0] / points[1],2))*100)}%")

results = surround_in_hashtags(f"You scored {points[0]} out of {points[1]}!")

final_grade = surround_in_hashtags(f"That is a grade {final_grade[0]} ({final_grade[1]}%).")

print(f"\n{results}\n\n{final_grade}")
