
ans1 = "2"
ans2 = "India"
ans3 = "Rabindranath Tagore"
ans4 = "Hockey Player"
ans5 = "5"

score = 0

asking_question = input("What is addition of 1 + 1? :")
if asking_question == ans1:
    score += 1

asking_question = input("What is name of our country? :")
if asking_question == ans2.lower():
    score += 1

asking_question = input("Who wrote janaganamana? :")
if asking_question == ans3.lower():
    score += 1

asking_question = input("Who was Major Dhyan Chand? :")
if asking_question == ans4.lower():
    score += 1

asking_question = input("what is the addition of 3 + 2 :")
if asking_question == ans5:
    score += 1
print(f"Your Score is : {score}")


if score == 5:
    grade = "A+"
elif score == 4:
    grade = "A"
elif score == 3:
    grade = "B"
elif score == 2:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
