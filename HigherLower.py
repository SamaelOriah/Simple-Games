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