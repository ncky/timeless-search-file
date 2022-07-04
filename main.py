from NotableSearch import NotableSearch
from TradeSearch import TradeSearch
import PySimpleGUI as sg
import tkinter as tk
from tkinter import Scrollbar, simpledialog


s = NotableSearch()

def get_notable_list(jewel_list):
    temp_list = []
    for node in jewel_list:
        if node in s.data.node_indices_graphid:
            temp_list.append(s.data.node_indices_graphid[node]["Name"])
    
    return temp_list

def check_notables(notable_list, seed, jeweltype, full): #takes a list of notables and returns it results
    temp_list = []
    for node in notable_list:
        if full < 1:
            temp_list.append(s.search(jeweltype, node, seed)['Id'])
        else: #
            temp_list.append(s.search(jeweltype, node, seed))
    return temp_list



type_list = list(s.data.jewels)
jewel_list = list(s.data.jewel_node_link)
notable_list = []
result_list = []
seed = 2000
jeweltype = "Elegant Hubris"
sg.theme('DarkBlue')

layout = [  [sg.Listbox(values=jewel_list, size=(8, 22),enable_events=True, key='-LISTBOX-', default_values=jewel_list[0], no_scrollbar=True), sg.Listbox(values=get_notable_list(s.data.jewel_node_link[jewel_list[0]]), size=(20, 22),enable_events=False, key='-LISTBOX2-', no_scrollbar=True), sg.Listbox(values=result_list, size=(50, 22),enable_events=True, key='-LISTBOX3-', no_scrollbar=True)],
            [sg.Slider(range=(s.data.jewels[jeweltype]["minSeed"], s.data.jewels[jeweltype]["maxSeed"]), disable_number_display=True , default_value=s.data.jewels[jeweltype]["minSeed"], resolution=1, orientation='h', enable_events=True, key='-SLIDER-'), sg.Text('Seed') , sg.InputText(seed, size=(30,4), key='-SEED-')],
            [sg.Text('Type'), sg.Combo(values=type_list, default_value=type_list[2], enable_events=True, key='-JTYPE-'),],
            [sg.Button('Search Socket', size=(30,2), key='-BUTTON-'),sg.Text('Search for:'), sg.InputText("aura", size=(15,4), key='-SEARCH-'),],
            [sg.Text('Results Found: 0\nMost Found: 0', key='-RESULTNO-'), sg.Listbox(values=[], key='-LISTBOX4-', size=(8,10),enable_events=True),sg.Button('Buy Jewel', size=(30,2), key='-BUY-')],
         ]
#sg.Slider( range=(s.data.jewels[jeweltype]["minSeed"], s.data.jewels[jeweltype]["maxSeed"])default_value=s.data.jewels[jeweltype]["minSeed"], resolution=s.data.jewels[jeweltype]["seedIncrement"], tick_interval=s.data.jewels[jeweltype]["seedIncrement"], ),
#Draw the window
window = sg.Window('Timeless Jewels', layout, size=(800,600))


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if '-SLIDER' in event: 
        seed = int(values['-SLIDER-'])
        window['-SEED-'].update(seed)
    seed = int(values['-SEED-'])
    jeweltype = values['-JTYPE-']
    if (seed < s.data.jewels[jeweltype]["minSeed"] or seed > s.data.jewels[jeweltype]["maxSeed"]):
        seed = s.data.jewels[jeweltype]["minSeed"]

    window['-SLIDER-'].update(seed, range=(s.data.jewels[jeweltype]["minSeed"], s.data.jewels[jeweltype]["maxSeed"]))
    notable_list = get_notable_list(s.data.jewel_node_link[values['-LISTBOX-'][0]])
    
    window['-LISTBOX2-'].update(notable_list)
    window['-LISTBOX3-'].update(check_notables(notable_list, seed, jeweltype, 0))

    if '-LISTBOX4-' in event:
        seed = values['-LISTBOX4-'][0]
        window['-SLIDER-'].update(seed)
        window['-SEED-'].update(seed)
        window['-LISTBOX2-'].update(notable_list)
        window['-LISTBOX3-'].update(check_notables(notable_list, seed, jeweltype, 0))
    
    if '-BUY-' in event:
        TradeSearch(seed, jeweltype)

    if '-BUTTON-' in event:
        temp_count_max = 0
        temp_seed = [0]
        stat_value = 0
        searchfor = values['-SEARCH-']
        for i in range(s.data.jewels[jeweltype]["minSeed"],s.data.jewels[jeweltype]["maxSeed"]+1, s.data.jewels[jeweltype]["seedIncrement"]):
            temp_count = 0
            temp_stat_value = 0
            temp_jewel = check_notables(get_notable_list(s.data.jewel_node_link[values['-LISTBOX-'][0]]), i, jeweltype, 1)
            for notable in temp_jewel: 
                if searchfor in notable['Id']:
                    temp_count += 1
                    temp_stat_value += int(notable['Stat1Min'])
            if temp_count == temp_count_max:
                temp_seed.append(i)
            if temp_count > temp_count_max:
                temp_count_max = temp_count
                temp_seed = [i,]
                stat_value = temp_stat_value
            
        if temp_count_max == 0: 
            temp_seed = [0]

        seed = temp_seed[0]
        window['-SLIDER-'].update(seed)
        window['-SEED-'].update(seed)
        window['-LISTBOX2-'].update(notable_list)
        window['-LISTBOX3-'].update(check_notables(notable_list, seed, jeweltype, 0))
        window['-LISTBOX4-'].update(temp_seed)
        window['-RESULTNO-'].update(f"Results Found: {len(temp_seed)}\nMost Found: {temp_count_max}\nTotal Stat: {stat_value}\n")



window.close()