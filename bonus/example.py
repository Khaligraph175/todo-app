import FreeSimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input()

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button]])

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break
  if event == "Convert":
    try:
       feet = float(values["feet"])
       inches = float(values["inches"])
       meters = feet * 0.3048 + inches * 0.0254
       window["output"].update(value=f"{meters:.3f} meters")
    except ValueError:
       window["output"].update(value="Please enter valid numbers")

window.close()