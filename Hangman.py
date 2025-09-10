import random

wordList=["apple","banana","melon","orange","grape","pear"]
chosenWord=wordList[random.randint(0,5)]
letters=[]
finWord=False
attempts=8
while finWord==False:
  missLet=0
  for x in chosenWord:
    if x in letters:
      print(x,end=" ")
    else:
      print("_",end=" ")
      missLet+=1

  if missLet==0:
    finWord=True
    print(f"\nWell done! The word was {chosenWord}")
  elif attempts==0:
    print(f"Bad Luck! The word was {chosenWord}.")
  print()
  guess=input("\nPlease guess a letter in the word: ")
  if guess not in chosenWord:
    attempts-=1
    print(f"\nNot in word. {attempts} attempts left.")
  letters.append(guess)
