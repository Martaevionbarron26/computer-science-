print("simple quiz")
tall_score = 0

answer = int(input("give a whole number that is less than 89.\n"))
if answer<89:
    tall_score = tall_score + 1


answer2 = int(input("give a whole number that is more than 67.\n"))
if answer2>67:
    tall_score = tall_score + 1 

answer3 = int(input("give a whole number that is less than -10.\n"))
if answer3<-10:
    tall_score = tall_score + 1

answer4 = int(input("give a whole number that is less than .1.\n"))
if answer4<.1:
    tall_score = tall_score + 1

answer5 = int(input("give a whole number that is more than -10.\n"))
if answer5<-10:
    tall_score = tall_score + 1

print(tall_score)
