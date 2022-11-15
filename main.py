import subprocess, os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.constants import END
from tkinter.messagebox import showinfo

# A simple java Editor and runner made by @DBanks93

# Creating the UI
root = tk.Tk()
root.title('Java runner/compiler/IDE (Made by Daniel Banks :)')
root.resizable(False, False)
root.geometry('750x300')

text = tk.Text(root, height=12)
text.grid(column=0, row=0, sticky='nsew')

path = ''

# Opens Java File
def openJavaFile():
    global path
    fileTypes = (('Java files', '*.java'), ('Text files', '*.txt'), ('All files', '*.*'))
    path = fd.askopenfilename(filetypes=fileTypes)
    if path:
        with open(path) as f:
            text.insert('1.0', f.read())

    saveButton.grid(column=0, row=1, sticky='n', padx=10, pady=10)
    compileButton.grid(column=0, row=2, sticky='n', padx=10, pady=10)

# Saves Javafile
def saveJavaFile():
    global path
    pathArray = list(path)
    for i in range(len(pathArray)):
        if pathArray[len(pathArray)-1-i] == '/':
            filenamePos = len(pathArray) - i
            break
    filename = path[filenamePos:]
    fileTypes = (('Java files', '*.java'), ('Text files', '*.txt'), ('All files', '*.*'))
    f = fd.asksaveasfile(mode='w', defaultextension="*.*", filetypes=fileTypes, initialfile=filename[:(len(filename)-5)])
    if f is None:
        return
    f.write(str(text.get(1.0, END)))
    f.close()
    
# Compiles Java file using subprocesses
def compileJavaFile():
    global path
    pathArray = list(path)
    for i in range(len(pathArray)):
        if pathArray[len(pathArray)-1-i] == '/':
            filenamePos = len(pathArray) - i
            break
    try:
        filePath = path[:filenamePos]
        filename = path[filenamePos:]
    except:
        return

    cmd = 'javac ' + filename

    p = subprocess.Popen(cmd, cwd=filePath, shell=True, stdout=subprocess.PIPE)
    subprocess_return = p.stdout.read()
    if subprocess_return.decode() == '':
        print("compiling successful")
    print(subprocess_return.decode())

# Runs the java file using Subproccess
# Runs java file in the relevant subprocess i.e. CMD for windows
def runJava():
    fileTypes = (('Java Class files', '*.class'), ('All files', '*.*'))
    path = fd.askopenfilename(filetypes=fileTypes)
    if path is None:
        return
    pathArray = list(path)
    for i in range(len(pathArray)):
        if pathArray[len(pathArray)-1-i] == '/':
            filenamePos = len(pathArray) - i
            break
    try:
        filePath = path[:filenamePos]
        filename = path[filenamePos:]
    except:
        return

    cmd = 'java ' + filename[:(len(filename)-6)]

    p = subprocess.Popen(cmd, cwd=filePath, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True,)
    print("*************************************************************************************\n                                PLEASE NOTE:                                \n You can only enter one input, if you have more just add set variables in the editor\n*************************************************************************************\n")
    entery = input("Enter the relvent input: ")
    print('\n')
    subprocess_return = p.communicate(entery.encode())[0]
    print(subprocess_return.decode())
    print("\nJava Program Finished")

openButton = ttk.Button(root, text='Open', command=openJavaFile)
openButton.grid(column=1, row=0, sticky='n', padx=10, pady=10)

runButton = ttk.Button(root, text="Run", command=runJava)
runButton.grid(column=1, row=1, sticky="n", padx=10, pady=10)

saveButton = ttk.Button(root, text="Save", command= saveJavaFile)

compileButton = ttk.Button(root, text="Compile", command= compileJavaFile)

root.mainloop()

