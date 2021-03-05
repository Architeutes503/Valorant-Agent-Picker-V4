import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import B
import pyautogui
import time


# Define the window's contents
layout = [[sg.Text("Which agent do you want to play with?")],
          [sg.Combo(["Astra", "Breach", "Brimstone", "Cypher", "Jett", "Killjoy", "Omen", "Phoenix",
                     "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"], key='-agentSelect-')],
          [sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Choose location file'), sg.Button('Save locations'),  sg.Button('Quit')]]

# Create the window
window = sg.Window('Agent Picker', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    elif event == 'Choose location file':
        filename = sg.popup_get_file('Enter the file you wish to process')
        sg.popup('Location file successfully saved.', filename)

    elif event == 'Save locations':
        print("Save locations")

        # Saves the location of the cursor
        class LocationSaver:
            def __init__(self, name):
                self.name = name
                sg.popup(
                    f"Please hover you cursor over {name} and wait until you get a message box that sais, that it has been saved. You have 3 seconds.")
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

# Finish up by removing from the screen
window.close()


