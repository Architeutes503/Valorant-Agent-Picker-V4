import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import B
import pyautogui
import time


# Define the window's contents
layout = [[sg.Text("Which agent do you want to play with?")],
          [sg.Combo(["Astra", "Breach", "Brimstone", "Cypher", "Jett", "Killjoy", "Omen", "Phoenix",
                     "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"], key='-agentSelect-')],
          [sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Save locations'), sg.Button('Options'),  sg.Button('Quit')]]

# Create the window
window = sg.Window('Agent Picker', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    elif event == 'Options':
        print("Options")

    elif event == 'Save locations':
        print("Save locations")

        # Saves the location of the cursor
        class LocationSaver:
            def __init__(self, name):
                self.name = name
                sg.popup(f"Please hover you cursor over {name} and wait until you get a message box that sais, that it has been saved. You have 3 seconds.")
                time.sleep(3)
                self.mouseX, self.mouseY = pyautogui.position()
                sg.popup(f"Done {name}.")

        # Writes the cursor coordinates into a file
        class LocationWriter:
            def __init__(self, mouseX, mouseY):
                self.mouseX = mouseX
                self.mouseY = mouseY
                locations.write(str(mouseX))
                locations.write("\n")
                locations.write(str(mouseY))
                locations.write("\n")

        # Explanation how the program works
        sg.popup(
            "This programm saves the location of all the agents and the lock in button.")
        sg.popup("The locations get saved in the same folder this program is in.")

        # Creates the file the locations get saved in.
        locations = open("locations.txt", "w")

        # List of all the agents in the game
        agents = ["Astra", "Breach", "Brimstone", "Cypher", "Jett", "Killjoy", "Omen",
                  "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru", "LockIn"]

        # For loop to save the coordinates
        for agent in agents:
            s = agent + "S"
            w = agent + "W"
            s = LocationSaver(agent)
            w = LocationWriter(s.mouseX, s.mouseY)

        sg.popup("All locations have been saved.")

    elif event == 'Ok':
        window['-OUTPUT-'].update('You successfully selected ' + values['-agentSelect-'])
        
        
        # Open the locations.txt and read all the coordinates into an array.
        with open("locations.txt") as file:
            coordinates = [coordinates.strip() for coordinates in file.readlines()]


        # Astra
        astraMouseX = coordinates[0]
        astraMouseY = coordinates[1]

        # Breach
        breachMouseX = coordinates[2]
        breachMouseY = coordinates[3]

        # Brimstone
        brimstoneMouseX = coordinates[4]
        brimstoneMouseY = coordinates[5]

        # Cypher
        cypherMouseX = coordinates[6]
        cypherMouseY = coordinates[7]

        # Jett
        jettMouseX = coordinates[8]
        jettMouseY = coordinates[9]

        # Killjoy
        killjoyMouseX = coordinates[10]
        killjoyMouseY = coordinates[11]

        # Omen
        omenMouseX = coordinates[12]
        omenMouseY = coordinates[13]

        # Phoenix
        phoenixMouseX = coordinates[14]
        phoenixMouseY = coordinates[15]

        # Raze
        razeMouseX = coordinates[16]
        razeMouseY = coordinates[17]

        # Reyna
        reynaMouseX = coordinates[18]
        reynaMouseY = coordinates[19]

        # Sage
        sageMouseX = coordinates[20]
        sageMouseY = coordinates[21]

        # Skye
        skyeMouseX = coordinates[22]
        skyeMouseY = coordinates[23]

        # Sova
        sovaMouseX = coordinates[24]
        sovaMouseY = coordinates[25]

        # Viper
        viperMouseX = coordinates[26]
        viperMouseY = coordinates[27]

        # Yoru
        yoruMouseX = coordinates[28]
        yoruMouseY = coordinates[29]

        # LockIn
        lockMouseX = coordinates[30]
        lockMouseY = coordinates[31]

        counter = 0

        sleep = 1

        # Astra
        if values['-agentSelect-'] == "Astra":
            sg.popup("You chose Astra.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(astraMouseX), int(astraMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Breach
        if values['-agentSelect-'] == "Breach":
            sg.popup("You chose Breach.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(breachMouseX), int(breachMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Brimstone 
        elif values['-agentSelect-'] == "Brimstone":
            sg.popup("You chose Brimstone.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(brimstoneMouseX), int(brimstoneMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Cypher
        elif values['-agentSelect-'] == "Cypher":
            sg.popup("You chose Cypher.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(cypherMouseX), int(cypherMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Jett
        elif values['-agentSelect-'] == "Jett":
            sg.popup("You chose Jett.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(jettMouseX), int(jettMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Killjoy
        elif values['-agentSelect-'] == "Killjoy":
            sg.popup("You chose Killjoy.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(killjoyMouseX), int(killjoyMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Omen
        elif values['-agentSelect-'] == "Omen":
            sg.popup("You chose Omen.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(omenMouseX), int(omenMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Phoenix
        elif values['-agentSelect-'] == "Phoenix":
            sg.popup("You chose Phoenix.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(phoenixMouseX), int(phoenixMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Raze
        elif values['-agentSelect-'] == "Raze":
            sg.popup("You chose Raze.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(razeMouseX), int(razeMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Reyna
        elif values['-agentSelect-'] == "Reyna":
            sg.popup("You chose Reyna.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(reynaMouseX), int(reynaMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Sage
        elif values['-agentSelect-'] == "Sage":
            sg.popup("You chose Sage.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(sageMouseX), int(sageMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Skye
        elif values['-agentSelect-'] == "Skye":
            sg.popup("You chose Skye.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(skyeMouseX), int(skyeMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Sova
        elif values['-agentSelect-'] == "Sova":
            sg.popup("You chose Sova.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(sovaMouseX), int(sovaMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Viper
        elif values['-agentSelect-'] == "Viper":
            sg.popup("You chose Viper.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(viperMouseX), int(viperMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # Yoru
        elif values['-agentSelect-'] == "Yoru":
            sg.popup("You chose Yoru.")
            time.sleep(sleep)
            while counter <= 50:
                pyautogui.moveTo(int(yoruMouseX), int(yoruMouseY))
                pyautogui.click()
                pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
                pyautogui.click()
                counter = counter + 1


        # InvalidAgent
        else:
            sg.popup("This isnt a valid agent.")
            time.sleep(3)

        # Finish up by removing from the screen
        window.close()
