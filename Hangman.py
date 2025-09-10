import random

wordList=["apple","banana","melon","orange","grape","pear"]
chosenWord=wordList[random.randint(0,6)]
letters=[]
missLet=0
while missLet==0:
  for x in chosenWord:
    if x in letters:
      print(x,end=" ")
    else:
      print("_",end=" ")
      missLet+=1
  if missLet==0:
    print(f"Well done! The word was {chosenWord}")

  guess=input("Please guess a letter in the word: ")
  letters.append(guess)
