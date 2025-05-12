import FreeSimpleGUI as sg

def km_to_miles(km):
    return float(km) / 1.6

label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter distance in km", key="kms")
miles_button = sg.Button("Convert")
output = sg.Text(key="output")

window = sg.Window("Km to Miles Converter",
    layout=[[label, input_box], [miles_button, output]],
    font=('Helvetica', 14))

while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = values['kms']
            try:
                result = km_to_miles(km)
                window['output'].update(value=f"{result:.2f} miles")
            except ValueError:
                window['output'].update(value="Please enter a number")
        case sg.WIN_CLOSED:
            break

window.close()