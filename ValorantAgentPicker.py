import pyautogui
import time

#Open the locations.txt and read all the coordinates into an array.
with open("locations.txt") as file:
    coordinates = [coordinates.strip() for coordinates in file.readlines()]


#Breach
breachMouseX = coordinates[0]
breachMouseY = coordinates[1]

#Brimstone
brimstoneMouseX = coordinates[2]
brimstoneMouseY = coordinates[3]

#Cypher
cypherMouseX = coordinates[4]
cypherMouseY = coordinates[5]

#Jett
jettMouseX = coordinates[6]
jettMouseY = coordinates[7]

#Killjoy
killjoyMouseX = coordinates[8]
killjoyMouseY = coordinates[9]

#Omen
omenMouseX = coordinates[10]
omenMouseY = coordinates[11]

#Phoenix
phoenixMouseX = coordinates[12]
phoenixMouseY = coordinates[13]

#Raze
razeMouseX = coordinates[14]
razeMouseY = coordinates[15]

#Reyna
reynaMouseX = coordinates[16]
reynaMouseY = coordinates[17]

#Sage
sageMouseX = coordinates[18]
sageMouseY = coordinates[19]

#Skye
skyeMouseX = coordinates[20]
skyeMouseY = coordinates[21]

#Sova
sovaMouseX = coordinates[22]
sovaMouseY = coordinates[23]

#Viper
viperMouseX = coordinates[24]
viperMouseY = coordinates[25]

#Yoru
yoruMouseX = coordinates[26]
yoruMouseY = coordinates[27]

#LockIn
lockMouseX = coordinates[28]
lockMouseY = coordinates[29]


print("Which agent do you want?")
print("1 -->  Breach")
print("2 -->  Brimstone")
print("3 -->  Cypher")
print("4 -->  Jett")
print("5 -->  Killjoy")
print("6 -->  Omen")
print("7 -->  Phoenix")
print("8 -->  Raze")
print("9 -->  Reyna")
print("10 --> Sage")
print("11 --> Skye")
print("12 --> Sova")
print("13 --> Viper")
print("14 --> Yoru")

userInput = input()
counter = 0

time.sleep(1)

#Breach
if userInput == "1":
    print("You chose Breach.")
    while counter <= 50:
        pyautogui.moveTo(int(breachMouseX), int(breachMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1

    


#Brimstone
elif userInput == "2":
    print("You chose Brimstone.")
    while counter <= 50:
        pyautogui.moveTo(int(brimstoneMouseX), int(brimstoneMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Cypher
elif userInput == "3":
    print("You chose Cypher.")
    while counter <= 50:
        pyautogui.moveTo(int(cypherMouseX), int(cypherMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Jett
elif userInput == "4":
    print("You chose Jett.")
    while counter <= 50:
        pyautogui.moveTo(int(jettMouseX), int(jettMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Killjoy
elif userInput == "5":
    print("You chose Killjoy.")
    while counter <= 50:
        pyautogui.moveTo(int(killjoyMouseX), int(killjoyMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Omen
elif userInput == "6":
    print("You chose Omen.")
    while counter <= 50:
        pyautogui.moveTo(int(omenMouseX), int(omenMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Phoenix
elif userInput == "7":
    print("You chose Phoenix.")
    while counter <= 50:
        pyautogui.moveTo(int(phoenixMouseX), int(phoenixMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Raze
elif userInput == "8":
    print("You chose Raze.")
    while counter <= 50:
        pyautogui.moveTo(int(razeMouseX), int(razeMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Reyna
elif userInput == "9":
    print("You chose Reyna.")
    while counter <= 50:
        pyautogui.moveTo(int(reynaMouseX), int(reynaMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Sage
elif userInput == "10":
    print("You chose Sage.")
    while counter <= 50:
        pyautogui.moveTo(int(sageMouseX), int(sageMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Skye
elif userInput == "11":
    
    print("You chose Skye.")
    while counter <= 50:
        pyautogui.moveTo(int(skyeMouseX), int(skyeMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Sova
elif userInput == "12":
    print("You chose Sova.")
    while counter <= 50:
        pyautogui.moveTo(int(sovaMouseX), int(sovaMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Viper
elif userInput == "13":
    print("You chose Viper.")
    while counter <= 50:
        pyautogui.moveTo(int(viperMouseX), int(viperMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Yoru
elif userInput == "14":
    print("You chose Yoru.")
    while counter <= 50:
        pyautogui.moveTo(int(yoruMouseX), int(yoruMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#InvalidAgent
else:
    print("This isnt a valid agent.")
    time.sleep(3)

