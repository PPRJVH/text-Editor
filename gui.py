import FreeSimpleGUI as G
from readAndWriteFiles import file_read, file_write
import time
import os
# Search in google pysimplegui themes go to images and select.
G.theme('NeutralBlue')

if not os.path.exists('store.txt'):
    with open('store.txt', 'w') as file:
        pass

time_ = G.Text('', key='t')
label = G.Text('Enter the Data')
InText = G.InputText(tooltip='Enter the Text', key='text')
add_button = G.Button(key='Add', image_source='add.png', size=3)

list_box = G.Listbox(values=file_read(), key='list', enable_events=True, size=[45, 15])
edit_button = G.Button('Edit')

delete_button = G.Button('Delete')

exit_button = G.Button('Exit')

w = G.Window('My first Gui Code', layout=[[time_], [label, InText, add_button],
                                          [list_box, edit_button, delete_button],
                                          [exit_button]], font=('Helvetica', 13))


while True:

    event, values = w.read(timeout=200)
    # w.read() will return a tuple as (Add,{0: 'hi'}).Here event=Add and values={0: 'hi'}
    w['t'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # if we need to know how the code is running remove the below comments
    # print(event)
    # print(values)

    match event:
        case "Add":
            data_list = file_read()
            data_list.append(values['text'] + '\n')
            file_write(data_list)
            w['list'].update(values=data_list)

        case 'list':
            w['text'].update(value=values['list'][0])
        case 'Edit':
            try:

                data_to_edit = values['list'][0]
                new_data = values['text']
                data_list = file_read()
                index = data_list.index(data_to_edit)
                data_list[index] = data_list[index].strip('\n')
                data_list[index] = new_data + '\n'
                file_write(data_list)
                print(data_list)
                w['list'].update(values=data_list)
            except IndexError:
                G.popup('Select the item First!', font=('Helvetica', 10))

        case 'Delete':
            try:
                data_to_delete = values['list'][0]
                data_list = file_read()
                index = data_list.index(data_to_delete)
                data_list.pop(index)
                file_write(data_list)
                w['list'].update(values=data_list)
                w['text'].update(value='')
            except IndexError:
                G.popup('Select the item First!', font=('Helvetica', 10))

        case 'Exit':
            break

        case G.WIN_CLOSED:
            break
w.close()
