import psutil
import PySimpleGUIQt as sg

layout = [
    [sg.Text("CPU Usage:", key='-CPU-')],
    [sg.Text("Memory Usage:", key='-MEM-')],
    [sg.Button('Exit')]
]

window = sg.Window("System Resource Monitor", layout)

while True:
    event, values = window.read(timeout=1000)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent

    window['-CPU-'].update(f"CPU Usage: {cpu}%")
    window['-MEM-'].update(f"Memory Usage: {mem}%")

window.close()
