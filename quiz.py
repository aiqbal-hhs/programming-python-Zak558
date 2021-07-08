print("Whats up person, here is my quiz to see how much you know about Minecraft Through these questions.")

print("Make sure you put the two capital letters for the first and lastname of the person in the first question. Alright lets get started, and good luck!")

score =0

creator = input("Who is the creator of Minecraft?")

if creator == "Markus Persson":
    print("correct!")
    score += 1
else:
  print("incorect!")
print("Your score is", score)

first = input("What was the first official version of minecraft that released?")

if first == "1.0.0":
    print("correct!")
    score += 1
else:
  print("incorect!")
print("Your score is", score)

update = input("What version is The world of colour update update?")

if update == "1.12":
    print("correct!")
    score += 1
else:
  print("incorect!")
print("Your score is", score)

console = input("When was mincraft console edition released?")

if console == "2011":
    print("correct!")
    score += 1
else:
  print("incorect!")
print("Your score is", score)

bedrock = input("When was mincraft bedrock edition released?")

if bedrock == "2011":
    print("correct!")
    score += 1
else:
  print("incorect!")
print("Your score is", score)

wither = input("When did the wither get introduced?")

if wither == "1.4.2":
    print("correct!")
    score += 1
else:
  print("incorect!")
print("Your score is", score)

ocean = input("When did ocean monuments get introduced?")

if ocean == "1.8":
    print("correct!")
    score += 1
else:
  print("incorect!")
print("Your score is", score)

block = input("What block can not be broken in survival mode?")

if block == "bedrock":
    print("correct!")
    score += 1
else:
  print("incorect!")
print("Your score is", score)

print ("You scored {} points!".format(score))
