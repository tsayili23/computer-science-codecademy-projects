import random

name = "ryan"
question = "is this real life?"

rm = random.randint(1,9)
print(name + " " + question)

if rm == 9:
  print("yes-definitely")
elif rm == 8:
  print("it is decidedly so")
elif rm == 7:
  print("without a doubt")
elif rm == 6:
  print("reply hazy try again")
elif rm == 5:
  print("ask again later")
elif rm == 4:
  print("better not tell you now")
elif rm == 3:
  print("my sources no")
elif rm == 2:
  print("error")
