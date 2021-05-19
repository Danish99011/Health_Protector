# --------------------Health programmer------------
# 9am - 5pm
# Water - water.mp3 - 3.5 litres==14 glasses--14 times == every 32 min(1920 sec) mein 1 glass- Drank - log
# Eyes - eyes.mp3 - every 30 min(1800 sec)-16times - EyDone - log
# Physical activity - physical.mp3 - every 45 min(2700 sec)-10times - ExDone - log 
# pygame module use hence import it
print("\t\t\t\t ------------Health App for Programmers------------")
name = input("Enter your name:")
print("Time constraint: 9am to 5pm(8 WORKING HOURS PROGRAM)\n")
print("This app includes following goals:-")
print("--You have to drink 3.5l in total, which means 1 glass in every 32 min.")
print("--Along with eye exercise in every 30 min.")
print("--And physical activity every 45 min.\n")
print("Every activity of yours will be recorded in a .txt file for further use.\n")
print("You can quit anytime...PRESS 'Q' TO EXIT.")

# in the below files the count and timer is not as rules above...it is set to minimun for testing

# i have made the code but i dont know how to run those 3 simultaneously..i can made water add, exercise app and eye app differently.

# import water_part1
# python file for the water drinking alert
# import eyes_part2
# python file for eye exercise
# import physical_part3
# python file for physical exercise
# importing the files didn't worked


# import subprocess
# subprocess.run("python3 water_part1.py & python3 eyes_part2.py",shell=True)
# importing subprocess didn't worked

# i have got the idea and now im trying something different

# import for playing music
from pygame import mixer
# import for time() attribute use for subtraction of current time and the second
from time import time
# import for datetime used for printing in the database
import datetime


# I DONT KNOW WHY THIS IS NOT WORKING...MAYBE THESE TWO MODULES DOESNT WORK SIMULTANEOULSY
# def current_time():
#     t = time.localtime()
#     current_time = time.strftime("%H:%M:%S", t)
#     return current_time

def gettime():
    """This is used to add current time of registration of the data"""
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S %d-%m-%Y")


# below 3 will be my current time in seconds for calculative work
init_water = time()
init_eyes = time()
init_exercise = time()
# these will be my constraints for alarm to work
water_timer = 1920
eyes_timer = 1800
exercise_timer = 2700

while True:
    if time() - init_water > water_timer:
        print("Alarm initiated...Drink a glass of water.")
        mixer.init()
        mixer.music.load("Water.mp3")
        mixer.music.set_volume(100)
        mixer.music.play()
        q = input("Press d to stop.")
        if q == "d":
            mixer.music.stop()
            f = open("water-record.txt", "a")
            f.write(str([str(gettime())]) + "\n")
            print(str(gettime()))
            print("Data has been successfully recorded.")
            f.close()
        elif q == "Q":
            mixer.music.stop()
            break
        else:
            print("You have entered something wrong. TRY AGAIN....")
        init_water = time()

    if time() - init_eyes > eyes_timer:
        print("Alarm initiated...TOO MUCH WATCHING.Start your eye exercise.")
        mixer.init()
        mixer.music.load("Eyes.mp3")
        mixer.music.set_volume(100)
        mixer.music.play()
        q = input("Press d to stop.")
        if q == "d":
            mixer.music.stop()
            f = open("eye-record.txt", "a")
            f.write(str([str(gettime())]) + "\n")
            print(str(gettime()))
            print("Data has been successfully recorded.")
            f.close()
        elif q == "Q":
            mixer.music.stop()
            break
        else:
            print("You have entered something wrong. TRY AGAIN....")
        init_eyes = time()

    if time() - init_exercise > exercise_timer:
        print("Alarm initiated...TOO MUCH SITTING.Start moving.")
        mixer.init()
        mixer.music.load("Physical.mp3")
        mixer.music.set_volume(100)
        mixer.music.play()
        q = input("Press d to stop.")
        if q == "d":
            mixer.music.stop()
            f = open("exercise-record.txt", "a")
            f.write(str([str(gettime())]) + "\n")
            print(str(gettime()))
            print("Data has been successfully recorded.")
            f.close()
        elif q == "Q":
            mixer.music.stop()
            break
        else:
            print("You have entered something wrong. TRY AGAIN....")
        init_exercise = time()

print(f"Thank you {name} for using our app...Wish you had a great time.\n\n")
print("\t\t\t\t\t------------- 'BE SAFE, BE HEALTHY' ------------------")
