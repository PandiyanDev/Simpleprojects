print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay, Let's play :)")
count =0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    count += 1
else:
    print("Incorrect!")
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    count += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    count += 1
else:
    print("Incorrect!")
    
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    count += 1
else:
    print("Incorrect!")
    
print("You got " +str(count)+ " questions correct out of " +str(4)+" questions!")