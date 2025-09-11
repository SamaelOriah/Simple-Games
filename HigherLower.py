def Help():
    print("""A random number is chosen depending on your preferred difficulty level.
        
    Easy= between 1 and 20
    Medium= between 1 and 40
    Hard = between 1 and 100
          """)
print("Welcome to Higher or Lower. Would you like to read the rules?")
ans=input("Enter your response here >> ").upper
if ans=="Y" or "YES":
    Help()