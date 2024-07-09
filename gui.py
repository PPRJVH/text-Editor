import readAndWriteFiles
import FreeSimpleGUI as g


label = g.Text('Enter the Data')
InText = g.InputText(tooltip='Enter the Text')
button = g.Button('Add')

w = g.Window('My first Gui Code',layout=[[label,InText],[button]])

w.read()
w.close()
