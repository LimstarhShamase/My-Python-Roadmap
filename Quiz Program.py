print("********Quizzz Time!!!!********")
print("**Python Basics Quiz by yours truly, Limstarh_Shamase**")
print()
answer1 = int(input('Q1) What does this program output[print("123")] \n1. An integer assigned with the value hundred and 23\n 2. A float assigned with the value hundred and 23 \n3. An string assigned with the value 123:\n '))
print()
answer2 = int(input('Q2) What is wrong with this code[print(name,"Limstarh")] \n1. The variable name was never declared in the input\n 2. Nothing it ouputs the name Limstarh in the console\n 3. None of the above:\n '))
print()
answer3 = int(input('Q3) What is the container for this variable[price = 3500.00]\n1. A float with the value of 3500.00\n2. An integer with the value of 3500.00\n3. A string with the value of 3500.00\n4. A boolean with the value of 3500.00 :\n '))
print()
answer4 = int(input('Q4) What is the container for this variable[score = "A plus"]\n1. A float with the value of A plus\n2. An integer with the value of A plus\n3. A string with the value of A plus\n4. A boolean with the value of A plus:\n '))
print()
answer5 = int(input('Q5) What is the container for this variable[price = 350]\n1. A float with the value of 350\n2. An integer with the value of 350\n3. A string with the value of 350\n4. A boolean with the value of 350:\n '))
print()
answer6 = int(input('Q6) What is the container for this variable[passedExam = true]\n1. A float with the value of true\n2. An integer with the value of true\n3. A string with the value of true\n4. A boolean with the value of true:\n '))
print()
score = 0

if answer1 == 3:
    score += 5
if answer2 == 1:
    score += 5
if answer3 == 1:
    score += 5
if answer4 == 3:
    score += 5
if answer5 == 2:
    score += 5
if answer6 == 4:
    score += 5

print("You got", score)

