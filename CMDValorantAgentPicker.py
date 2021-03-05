import pyautogui
import time

#Open the locations.txt and read all the coordinates into an array.
with open("locations.txt") as file:
    coordinates = [coordinates.strip() for coordinates in file.readlines()]



#Breach
astraMouseX = coordinates[0]
astraMouseY = coordinates[1]

#Breach
breachMouseX = coordinates[2]
breachMouseY = coordinates[3]

#Brimstone
brimstoneMouseX = coordinates[4]
brimstoneMouseY = coordinates[5]

#Cypher
cypherMouseX = coordinates[6]
cypherMouseY = coordinates[7]

#Jett
jettMouseX = coordinates[8]
jettMouseY = coordinates[9]

#Killjoy
killjoyMouseX = coordinates[10]
killjoyMouseY = coordinates[11]

#Omen
omenMouseX = coordinates[12]
omenMouseY = coordinates[13]

#Phoenix
phoenixMouseX = coordinates[14]
phoenixMouseY = coordinates[15]

#Raze
razeMouseX = coordinates[16]
razeMouseY = coordinates[17]

#Reyna
reynaMouseX = coordinates[18]
reynaMouseY = coordinates[19]

#Sage
sageMouseX = coordinates[20]
sageMouseY = coordinates[21]

#Skye
skyeMouseX = coordinates[22]
skyeMouseY = coordinates[23]

#Sova
sovaMouseX = coordinates[24]
sovaMouseY = coordinates[25]

#Viper
viperMouseX = coordinates[26]
viperMouseY = coordinates[27]

#Yoru
yoruMouseX = coordinates[28]
yoruMouseY = coordinates[29]

#LockIn
lockMouseX = coordinates[30]
lockMouseY = coordinates[31]


print("Which agent do you want?")
print("1 -->  Astra")
print("2 -->  Breach")
print("3 -->  Brimstone")
print("4 -->  Cypher")
print("5 -->  Jett")
print("6 -->  Killjoy")
print("7 -->  Omen")
print("8 -->  Phoenix")
print("9 -->  Raze")
print("10 -->  Reyna")
print("11 --> Sage")
print("12 --> Skye")
print("13 --> Sova")
print("14 --> Viper")
print("15 --> Yoru")

userInput = input()
counter = 0

time.sleep(1)

#Astra
if userInput == "2":
    print("You chose Astra.")
    while counter <= 50:
        pyautogui.moveTo(int(astraMouseX), int(astraMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1



#Breach
if userInput == "2":
    print("You chose Breach.")
    while counter <= 50:
        pyautogui.moveTo(int(breachMouseX), int(breachMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1

    


#Brimstone
elif userInput == "3":
    print("You chose Brimstone.")
    while counter <= 50:
        pyautogui.moveTo(int(brimstoneMouseX), int(brimstoneMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Cypher
elif userInput == "4":
    print("You chose Cypher.")
    while counter <= 50:
        pyautogui.moveTo(int(cypherMouseX), int(cypherMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Jett
elif userInput == "5":
    print("You chose Jett.")
    while counter <= 50:
        pyautogui.moveTo(int(jettMouseX), int(jettMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Killjoy
elif userInput == "6":
    print("You chose Killjoy.")
    while counter <= 50:
        pyautogui.moveTo(int(killjoyMouseX), int(killjoyMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Omen
elif userInput == "7":
    print("You chose Omen.")
    while counter <= 50:
        pyautogui.moveTo(int(omenMouseX), int(omenMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Phoenix
elif userInput == "8":
    print("You chose Phoenix.")
    while counter <= 50:
        pyautogui.moveTo(int(phoenixMouseX), int(phoenixMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Raze
elif userInput == "9":
    print("You chose Raze.")
    while counter <= 50:
        pyautogui.moveTo(int(razeMouseX), int(razeMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Reyna
elif userInput == "10":
    print("You chose Reyna.")
    while counter <= 50:
        pyautogui.moveTo(int(reynaMouseX), int(reynaMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Sage
elif userInput == "11":
    print("You chose Sage.")
    while counter <= 50:
        pyautogui.moveTo(int(sageMouseX), int(sageMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Skye
elif userInput == "12":
    
    print("You chose Skye.")
    while counter <= 50:
        pyautogui.moveTo(int(skyeMouseX), int(skyeMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Sova
elif userInput == "13":
    print("You chose Sova.")
    while counter <= 50:
        pyautogui.moveTo(int(sovaMouseX), int(sovaMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Viper
elif userInput == "14":
    print("You chose Viper.")
    while counter <= 50:
        pyautogui.moveTo(int(viperMouseX), int(viperMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Yoru
elif userInput == "15":
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

