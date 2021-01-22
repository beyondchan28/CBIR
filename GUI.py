import PySimpleGUI as sg
# import PySimpleGUIQt as sg
import os.path
from colorDescriptor import ColorDescriptor as cd
from pandas import read_csv
import cv2
import ml
import random
# First the window layout in 2 columns
def train(image) :
    display = []
    image = cv2.imread(image)
    features = cd.describe(image)
    print(features)
    testing = ml.test(features)
    print(testing)
    url = "D:\opencv\index.csv"
    names = ['path', 'red', 'green', 'blue', 'diameter', 'jenis']
    dataset = read_csv(url, names=names)
    array = dataset.values
    lemon = array[0, 0:19]
    nipis = array[0, 20:39]
    orange = array[0, 40:59]
    print(lemon)
    if testing == 'lemon':
        display = lemon
    elif testing == 'nipis':
        display == nipis
    elif testing == 'orange':
        display = orange
    print(display)
    return display
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(20, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 10), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

image_viewer_column1 = [
    [sg.Text("result retrieve:")],
    [sg.Text(size=(40, 1), key="-TOUT1-")],
    [sg.Image(key="-IMAGE1-")],
]
# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column1),
        sg.Button("Go"),
    ]
]

window = sg.Window("Image Viewer", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)

        except:
            pass

    elif event == "Go":
        path1 = values["-FOLDER-"]
        path2 = listToString(values.get("-FILE LIST-"))
        path = path1+'/'+path2
        print(path)
        image = train(path)
        try:
            filename = os.path.join(image[0])
            window["-TOUT1-"].update(filename)
            window["-IMAGE1-"].update(filename=filename)
        except:
            pass
window.close()