import pyautogui
import time

class LocationSaver:
    def __init__(self, name):
        self.name = name
        print(f"Please hover you cursor over {name} and wait until you get a message box that sais, that it has been saved. You have 3 seconds.")
        time.sleep(3)
        self.mouseX, self.mouseY = pyautogui.position()
        pyautogui.alert(f"Done {name}.")

class LocationWriter:
    def __init__(self, mouseX, mouseY):
        self.mouseX = mouseX
        self.mouseY = mouseY

        locations.write(str(mouseX))
        locations.write("\n")
        locations.write(str(mouseY))
        locations.write("\n")


#Explanation    
print("This programm saves the location of all the agents and the lock in button.")
print("The locations get saved in the same folder the ValorantAgentLocation.py is saved in.")
print("The ValorantAgentPicker.py needs to be in the same directory as the locations.txt is.\n")

locations = open("locations.txt", "w")

agents = ["Astra", "Breach", "Brimstone", "Cypher", "Jett", "Killjoy", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru", "LockIn"]

for agent in agents:
    s = agent + "S"
    w = agent + "W"

    s = LocationSaver(agent)
    w = LocationWriter(s.mouseX, s.mouseY)