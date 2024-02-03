# MOHAMMED's Python-based Quiz Game

print("WELCOME TO THE COMPUTER SCIENCE QUIZ")

# Ensure there is a space for a smoother visual presentation
playing = input("Would you like to participate? (yes/yeah/ye): ")

# Accept "yes", "yeah" and "ye" as valid responses
if playing.lower() not in ["yes", "yeah", "ye"]:
    print("Thank you for considering! Goodbye.")
    quit()

print("\nGreat! Let's dive into the quiz.")
score = 0

# Question 1
answer = input("1. What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect. The correct answer is 'Central Processing Unit'.")

# Question 2
answer = input("2. What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect. The correct answer is 'Graphics Processing Unit'.")

# Question 3
answer = input("3. What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect. The correct answer is 'Random Access Memory'.")

# Question 4
answer = input("4. What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect. The correct answer is 'Power Supply'.")

# Display results
print("\nYou answered " + str(score) + " out of 4 questions correctly!")
percentage = (score / 4) * 100
print("Your score is {:.2f}%.".format(percentage))

if percentage == 100:
    print("Congratulations! You aced the quiz!")
elif percentage >= 75:
    print("Well done! You have a solid understanding of computer science.")
else:
    print("Keep learning! You can improve your knowledge in computer science.")
