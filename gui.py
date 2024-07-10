import readAndWriteFiles
import FreeSimpleGUI as g
from readAndWriteFiles import  file_read,file_write



label = g.Text('Enter the Data')
InText = g.InputText(tooltip='Enter the Text',key='text')
add_button = g.Button('Add')
list_box = g.Listbox(values = file_read(),key='list',enable_events = True,size = [50,15])
edit_button = g.Button('Edit')
w = g.Window('My first Gui Code',layout=[[label,InText],[add_button],[list_box,edit_button]])


while True:

    event,values= w.read()
    # w.read() will return a tuple as (Add,{0: 'hi'}).Here event=Add and values={0: 'hi'}

    print(event)
    print(values)

    match event:
        case "Add":
            data_list = file_read()
            data_list.append(values['text'] + '\n')
            file_write(data_list)
            w['list'].update(values=data_list)

        case 'list':
            w['text'].update(value=values['list'][0])
        case 'Edit':
            data_to_edit = values['list'][0]
            new_data = values['text']
            data_list = file_read()
            index = data_list.index(data_to_edit)
            data_list[index] = new_data + '\n'
            file_write(data_list)
            print(data_list)
            w['list'].update(values=data_list)

        case g.WIN_CLOSED:
            break







w.close()


