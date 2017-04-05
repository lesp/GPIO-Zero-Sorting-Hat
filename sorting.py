from gpiozero import Button, LED
from random import choice
from time import sleep

button = Button(22)
gryffindor = LED(2)
slytherin = LED(3)
hufflepuff = LED(27)
ravenclaw = LED(17)

phrases = ["Difficult, you are very difficult to sort","You are a hero, I know which house you belong to","I sense a darkness in your magic","When duty calls you will do your bit for the school"]
houses = ["Gryffindor","Slytherin","Hufflepuff","Ravenclaw"]
print("Press the button to learn which house you will be joining")
while True:
    button.wait_for_press()
    message = choice(phrases)
    house = choice(houses)
    print(message, house)
    if house == "Gryffindor":
        gryffindor.blink(0.2,0.2)
        sleep(5)
        gryffindor.off()
    elif house == "Slytherin":
        slytherin.blink(0.2,0.2)
        sleep(5)
        slytherin.off()
    elif house == "Hufflepuff":
        hufflepuff.blink(0.2,0.2)
        sleep(5)
        hufflepuff.off()
    elif house == "Ravenclaw":
        ravenclaw.blink(0.2,0.2)
        sleep(5)
        ravenclaw.off()


    #print(message, house)
    sleep(0.2)
