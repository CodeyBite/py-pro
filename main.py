import os 


print("Welcome to Robospeaker 1.1 created by Kosal for ubuntu")
while True:                                         
    x = input("Enter what you want me to speak: ")
    if x == "q":
        os.system("espeak 'bye bye friend'")
        break

    
    command = f"espeak {x}"

    os.system(command)