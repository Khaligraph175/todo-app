import FreeSimpleGUI as sg

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")
submit_button = sg.Button("Submit")

window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1],
                           [option2],
                           [option3],
                           [option4],
                           [submit_button]])

window = sg.Window("Animal Quiz", layout)

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break
  if event == "Submit":
    if values[0]:
        sg.popup("Incorrect! Dolphins are not amphibians.")
      elif values[1]:
        sg.popup("Incorrect! Dolphins are not fish.")
      elif values[2]:
        sg.popup("Correct! Dolphins are mammals!")
      elif values[3]:
        sg.popup("Incorrect! Dolphins are not birds.")
      else:
        sg.popup("Please select an answer!")

window.close()