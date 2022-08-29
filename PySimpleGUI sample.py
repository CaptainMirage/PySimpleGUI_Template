# Version : Sample
# > import.exe

# >Theme.exe
sg.theme('DarkAmber')

# >Sample_Layout.exe
SampleLayout = [
    [sg.Text("Sample text")],
    [sg.Button("Sample Button"), sg.Button("Sample Exit")]
]

# >Sample_Window.exe
SampleWin = sg.Window(title="Sample title", layout=SampleLayout, grab_anywhere=True, resizable=True)

# >Sample_EventsLoop.exe
while True:
    SampleEvent, SampleValue = SampleWin.read(timeout=200)            # >>event operation sample

    if SampleEvent == "Sample Exit" or SampleValue == sg.WIN_CLOSED:         # >>Exit operation sample
        break

SampleWin.close()