import random
def Help():
    print("""A random number is chosen depending on your preferred difficulty level.
        
    Easy= between 1 and 20
    Medium= between 1 and 40
    Hard = between 1 and 100
    
    You will guess a number between that range and you will be told if you need to go lower or higher.
    Depending on your difficulty you have a certain number of attempts to do it in.
          """)
print("Welcome to Higher or Lower. Would you like to read the rules?")
ans=input("Enter your response here >> ").upper
if ans=="Y" or "YES":
    Help()

print("""Which difficulty do you want?
      
1. Easy
2. Medium
3. Hard""")
ans=int(input("Enter your answer here >>"))
match ans:
    case 1:
        selectNum=random.randint(1,20)
        attempts=3
    case 2:
        selectNum=random.randint(1,40)
        attempts=5
    case 3:
        selectNum=random.randint(1,100)
        attempts=7
while attempts >0:
    guess=int(input("Please enter a number: "))
    if selectNum - guess > 0:
        attempts-=1
        print(f"Higher. {attempts} attempts left.")
    elif selectNum - guess <0:
        attempts-=1
        print(f"Lower. {attempts} attempts left.")
    elif selectNum-guess==0:
        print("Well done, you guessed the number correctly!")
        break
if attempts==0:
    print(f"Ran out of attempts. The number was {selectNum}.")