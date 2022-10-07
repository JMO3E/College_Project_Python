from tkinter import *
from registerClass import *

def show_layout(layout):
    layout.tkraise()

"""
 App Settings
"""
app = Tk()
app.title('Portal de Maestros')
app.geometry('1000x800')
app.resizable(False, False)

app.rowconfigure(0, weight=1)
app.columnconfigure(0,weight=1)

logInLayout = Frame(app, bg='#00c9c9')
menuLayout = Frame(app, bg='#00c9c9')
createRegisterLayout = Frame(app, bg='#00c9c9')
getAllDataLayout = Frame(app, bg='#00c9c9')
changeAllStudentDataLayout = Frame(app, bg='#00c9c9')
changeOneStudentDataLayout = Frame(app, bg='#00c9c9')

for frame in (logInLayout, menuLayout,createRegisterLayout,getAllDataLayout,changeAllStudentDataLayout,changeOneStudentDataLayout):
    frame.grid(row=0,column=0,sticky='nsew')


mainColor = StringVar()
mainColor.set('#00c9c9')

secondColor = StringVar()
secondColor.set('#00adad')

"""
 LogIn Layout -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def login_verified():
    usernameList = ['Host', 'juan24', 'pedro201', 'john33']
    passwordList = ['123','mascota12', 'carro102', 'pr13']

    for index in range(3):
        if checkUsername.get() == usernameList[index]:
            if checkPassword.get() == passwordList[index]:
                show_layout(menuLayout)
        else:
            incorrect_label['text']='The username or password is incorrect!!'

borderLogIn_Label = Label(logInLayout, height=1, bg="black")
borderLogIn_Label.pack(fill='x')

logIn_title = Label(logInLayout, text='Portal de Notas',fg="white", bg=mainColor.get(), font=('arial', 45, 'bold'))
logIn_title.pack(pady=25)

borderLogIn_Label = Label(logInLayout, height=1, bg="black")
borderLogIn_Label.pack(fill='x')

brLogin_labelOne = Label(logInLayout, height=2, bg=mainColor.get())
brLogin_labelOne.pack()

username_label = Label(logInLayout, text='Username', font=('arial', 13), bg=mainColor.get(), fg='white')
username_label.pack()

checkUsername = StringVar()
checkPassword = StringVar()

username_entry = Entry(logInLayout, textvariable=checkUsername, font=('arial', 12))
username_entry.pack()

brLogin_labelTwo = Label(logInLayout, height=1, bg=mainColor.get())
brLogin_labelTwo.pack()

password_label = Label(logInLayout, text='Password', font=('arial', 13), bg=mainColor.get(), fg='white')
password_label.pack()

password_entry = Entry(logInLayout, textvariable=checkPassword, font=('arial', 12))
password_entry.pack()

logIn_btn = Button(logInLayout, text='LogIn', command=login_verified)
logIn_btn.pack(pady=10)

incorrect_label = Label(logInLayout, text="", font=("arial", 13), fg='red', bg=mainColor.get())
incorrect_label.pack()

borderLogIn_Label = Label(logInLayout, height=1, bg="black")
borderLogIn_Label.pack(fill='x')

brLogin_labelThree = Label(logInLayout, height=2, bg=mainColor.get())
brLogin_labelThree.pack(fill='both',expand=True)

borderLogIn_Label = Label(logInLayout, height=1, bg="black")
borderLogIn_Label.pack(fill='x')

"""
 Menu Layout
"""
borderMenu_Label = Label(menuLayout, height=1, bg="black")
borderMenu_Label.pack(fill='x')

Menu_title = Label(menuLayout, text=('Bienvenido'),fg="white", bg=mainColor.get(), font=('arial', 45, 'bold'))
Menu_title.pack(pady=25)

borderMenu_Label = Label(menuLayout, height=1, bg="black")
borderMenu_Label.pack(fill='x')

''' BG Setting Color '''
leftSide_BG = Label(menuLayout, bg='#00c9c9')
leftSide_BG.pack(ipadx=100, ipady=25,fill='both',side='left')

middleSide_BG = Label(menuLayout, bg='#00dbdb')
middleSide_BG.pack(ipady=25, expand=True,fill='both',side='left')

rightSide_BG = Label(menuLayout, bg='#00c9c9')
rightSide_BG.pack(ipadx=100, ipady=25, fill='both',side='left')

''' Buttons '''
createRegisterLayout_btn = Button(menuLayout, text='Creacion de registro', command=lambda:[show_layout(createRegisterLayout), ], relief='raised', width=30, height=5)
createRegisterLayout_btn.place(x=240, y=240)

getAllDataLayout_btn = Button(menuLayout, text='Obten datos de todos los estudiantes', command=lambda:show_layout(getAllDataLayout), relief='raised', width=30, height=5)
getAllDataLayout_btn.place(x=540, y=240)

changeAllStudentDataLayout_btn = Button(menuLayout, text='Cambiar datos de todos los estudiantes', command=lambda:show_layout(changeAllStudentDataLayout), relief='raised', width=30, height=5)
changeAllStudentDataLayout_btn.place(x=240, y=380)

changeOneStudentDataLayout_btn = Button(menuLayout, text='Cambiar datos de un estudiante', command=lambda:show_layout(changeOneStudentDataLayout), relief='raised', width=30, height=5)
changeOneStudentDataLayout_btn.place(x=540, y=380)

saveData_btn = Button(menuLayout, text='Guardar cambios', relief='raised', width=30, height=5)
saveData_btn.place(x=240, y=520)

exit_btn = Button(menuLayout, text='Salir', command=app.destroy, relief='raised', width=30, height=5)
exit_btn.place(x=540, y=520)

"""
 Crear Registro Layout ----------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

borderRegister_Label = Label(createRegisterLayout, height=1, bg="black")
borderRegister_Label.pack(fill='x')

Register_title = Label(createRegisterLayout, text='Creando el registro',fg="white", bg=mainColor.get(), font=('arial', 45, 'bold'))
Register_title.pack(pady=25)

borderRegister_Label = Label(createRegisterLayout, height=1, bg="black")
borderRegister_Label.pack(fill='x')

''' Variables '''
global createFile
createFile = False

confFileNameVar = StringVar()
courseNameVar = StringVar()
studFileNameVar = StringVar()
evaluationVar = IntVar()

''' Label '''
confFileName_Label = Label(createRegisterLayout, text='Nombre del archivo de configuracion', font=('arial', 13), bg=mainColor.get(), fg='white')
confFileName_Label.place(x=110, y=200)

''' Entry '''
confFileName_entry = Entry(createRegisterLayout, textvariable=confFileNameVar, font=('arial', 12))
confFileName_entry.place(x=150, y=235)

''' Label '''
courseName_label = Label(createRegisterLayout, text='Nombre del curso', font=('arial', 13), bg=mainColor.get(), fg='white')
courseName_label.place(x=175, y=275)

''' Entry '''
courseName_entry = Entry(createRegisterLayout, textvariable=courseNameVar, font=('arial', 12))
courseName_entry.place(x=150, y=305)

''' Label '''
studFileName_label = Label(createRegisterLayout, text='Nombre del archivo de estudiantes', font=('arial', 13), bg=mainColor.get(), fg='white')
studFileName_label.place(x=110, y=345)

''' Entry '''
studFileName_entry = Entry(createRegisterLayout, textvariable=studFileNameVar, font=('arial', 12))
studFileName_entry.place(x=150, y=375)

''' Label '''
evaluations_label = Label(createRegisterLayout, text='Cantidad de evaluaciones', font=('arial', 13), bg=mainColor.get(), fg='white')
evaluations_label.place(x=148, y=415)

''' Entry '''
evaluations_entry = Entry(createRegisterLayout, textvariable=evaluationVar, font=('arial', 12))
evaluations_entry.place(x=150, y=445)

register = Register()

filesNamesList = []

courseNamesList = []

studentFilesList = []

fileDB = open("DB.txt", "r")
filesNamesList = fileDB.read().splitlines()
fileDB.close()

fileCourse = open("courses.txt", "r")
courseNamesList = fileCourse.read().splitlines()
fileCourse.close()

fileStudents = open("studentCourseFile.txt", "r")
studentFilesList = fileStudents.read().splitlines()
fileStudents.close()

def saveInformation():
    register.setConfigFileName(confFileNameVar.get())
    register.setCourseName(courseNameVar.get())
    register.setStudFileName(studFileNameVar.get())
    register.setEvaluationCount(evaluationVar.get())

    courseFile = open("courses.txt", 'a')
    courseFile.write(register.getCourseName() + '\n')
    courseFile.close()

    configFilesNames = open("DB.txt", 'a')
    configFilesNames.write(register.getConfigFileName() + "\n")
    configFilesNames.close()

    file=open(register.getConfigFileName(),"w")
    file.write(register.getCourseName() + "\n")
    file.write(register.getStudFileName() + "\n")
    file.write(str(register.getEvaluationCount()) + "\n")
    file.close()

    createFile = True

    saveInfo_btn['state'] = DISABLED

''' Button '''
saveInfo_btn = Button(createRegisterLayout, text='Guardar', command=saveInformation, state=ACTIVE, relief='raised', width=15, height=4)
saveInfo_btn.place(x=180, y=520)

''' Middle Division '''
borderRegisterV_Label = Label(createRegisterLayout, width=2, height=30, bg="black")
borderRegisterV_Label.pack(fill='y')

"""
'''Informacion de las notas 
"""
''' Variables '''
evaluationName = StringVar()
totalPoints = IntVar()
perContFinal = IntVar()

''' Label '''
evaluationName_Label = Label(createRegisterLayout, text='Nombre de la Evaluacion', font=('arial', 13), bg=mainColor.get(), fg='white')
evaluationName_Label.place(x=665, y=200)

''' Entry '''
evaluationName_entry = Entry(createRegisterLayout, textvariable=evaluationName, font=('arial', 12))
evaluationName_entry.place(x=670, y=235)

''' Label '''
totalPoints_label = Label(createRegisterLayout, text='Total de puntos del Parcial', font=('arial', 13), bg=mainColor.get(), fg='white')
totalPoints_label.place(x=665, y=275)

''' Entry '''
totalPoints_entry = Entry(createRegisterLayout, textvariable=totalPoints, font=('arial', 12))
totalPoints_entry.place(x=670, y=305)

''' Label '''
perContFinal_label = Label(createRegisterLayout, text='Por ciento de contribucion para el promedio final', font=('arial', 13), bg=mainColor.get(), fg='white')
perContFinal_label.place(x=580, y=345)

''' Entry '''
perContFinal_entry = Entry(createRegisterLayout, textvariable=perContFinal, font=('arial', 12))
perContFinal_entry.place(x=670, y=375)

global flag
flag = 0

def addEvaluation():

    global flag
    flag += 1

    if flag <= register.getEvaluationCount():
        file = open(register.getConfigFileName(), 'a')
        file.write(str(evaluationName.get()) + "\n")
        file.write(str(totalPoints.get()) + "\n")
        file.write(str(perContFinal.get()) + "\n")

        if flag == register.getEvaluationCount():
            saveEvaluation_btn['state'] = DISABLED

            fileTwo = open(register.getStudFileName(),'r')

            while (f := fileTwo.read()):

                file.write(f + "\n")

            fileTwo.close()
            file.close()

''' Button '''
saveEvaluation_btn = Button(createRegisterLayout, text='Guardar', command=lambda:addEvaluation(), state=ACTIVE, relief='raised',width=15, height=4)
saveEvaluation_btn.place(x=700, y=420)

""" '''Bottom Border''' """
borderRegisterB_Label = Label(createRegisterLayout, height=1, bg="black")
borderRegisterB_Label.pack(fill='x')

""" '''Footer''' """
def exitToMenu():
    show_layout(menuLayout)

    filesNamesList.append(register.getConfigFileName())

    courseNamesList.append(register.getCourseName())

    confFileNameVar.set('')
    courseNameVar.set('')
    studFileNameVar.set('')
    evaluationVar.set(0)

    evaluationName.set('')
    totalPoints.set(0)
    perContFinal.set(0)

    global flag
    flag = 0

    saveInfo_btn['state'] = ACTIVE
    saveEvaluation_btn['state'] = ACTIVE

''' Button '''
exitMenu_btn = Button(createRegisterLayout, text='Volver al menu', command=exitToMenu, state=ACTIVE, relief='raised', width=20, height=4)
exitMenu_btn.pack(pady=50)

"""
 All Data Layout ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
borderRegister_Label = Label(getAllDataLayout, height=1, bg="black")
borderRegister_Label.pack(fill='x')

Register_title = Label(getAllDataLayout, text='Datos de los estudiantes',fg="white", bg=mainColor.get(), font=('arial', 45, 'bold'))
Register_title.pack(pady=25)

borderRegister_Label = Label(getAllDataLayout, height=1, bg="black")
borderRegister_Label.pack(fill='x')

text_scroll = Scrollbar(getAllDataLayout)
text_scroll.pack(side=RIGHT,fill=Y)

''' Variables '''
fileNameVar = StringVar()
fileNameVar.set('')


def update_option_menu():
    dropdownMenu = OptionMenu(getAllDataLayout, fileNameVar, *filesNamesList, command=outputfile)
    dropdownMenu.place(x=50, y=420, width=200)


def outputfile(filename):
    outputInfo.delete('1.0', END)
    with open(filename) as f:
        outputInfo.insert(INSERT, f.read())


dropdownMenu = OptionMenu(getAllDataLayout, fileNameVar, *filesNamesList, command=outputfile)
dropdownMenu.place(x=50, y=420,width=200)

dropdownMenuTWO = OptionMenu(getAllDataLayout, fileNameVar, *filesNamesList, command=outputfile)
dropdownMenuTWO.place(x=50, y=420,width=200)

update_button = Button(getAllDataLayout, text='Actualizar', command=lambda:[update_option_menu(),dropdownMenu.destroy()])
update_button.place(x=50, y=460,width=200)

text_output = Label(getAllDataLayout, text='',fg="white", bg=mainColor.get(), font=('arial', 15))
text_output.pack(padx=30)

outputInfo = Text(getAllDataLayout, height=25, width=40, bg=secondColor.get(), borderwidth=10, font=('arial', 12), fg='white', yscrollcommand=text_scroll.set, wrap="none")
outputInfo.pack(pady=20)

if createFile:
    if fileNameVar.get() != "":
        outputfile()

""" Bottom Border """
borderRegisterB_Label = Label(getAllDataLayout, height=1, bg="black")
borderRegisterB_Label.pack(fill='x')

""" Footer """
def exitToM():
    show_layout(menuLayout)

''' Button '''
exitMenu_btn = Button(getAllDataLayout, text='Volver al menu', command=exitToM, state=ACTIVE, relief='raised', width=20, height=4)
exitMenu_btn.pack(pady=20)

"""
     Change Data all student Layout ----------------------------------------------------------------------------------------------------------------------------------------------
"""
borderRegister_Label = Label(changeAllStudentDataLayout, height=1, bg="black")
borderRegister_Label.pack(fill='x')

Register_title = Label(changeAllStudentDataLayout, text='Modificacion de actividad de todo el grupo',fg="white", bg=mainColor.get(), font=('arial', 30, 'bold'))
Register_title.pack(pady=25)

borderRegister_Label = Label(changeAllStudentDataLayout, height=1, bg="black")
borderRegister_Label.pack(fill='x')

''' BG Setting Color '''
leftSide_BG = Label(changeAllStudentDataLayout, bg=secondColor.get())
leftSide_BG.pack(ipadx=10,ipady=10,expand=True,fill='both',side='left')

middleSide_BG = Label(changeAllStudentDataLayout, bg=mainColor.get())
middleSide_BG.pack(ipadx=10,ipady=10,expand=True,fill='both',side='left')

rightSide_BG = Label(changeAllStudentDataLayout, bg=secondColor.get())
rightSide_BG.pack(ipadx=10,ipady=10,expand=True,fill='both',side='left')

''' Variables '''
courseVar = StringVar()
courseVar.set('')

actividadVar = StringVar()
actividadVar.set('')

pointsVar = IntVar()

global actividadList
actividadList = []

global eCount

def handleTwo(self):
    getActividad()
    deleteDrop()

def getActividad():
    actividadList = []
    eCount = 0

    actList = ['']
    for course_Name in courseNamesList:
        data = course_Name
        if courseVar.get() == data:
            for file_Name in filesNamesList:
                if data in file_Name:
                    f = open(file_Name, 'r')
                    for i, line in enumerate(f):
                        if i == 1:
                            for c in f:
                                print(c)
                                eCount = c
                                eCount = int(eCount) * 3
                                break

                            actList = f.read().splitlines()
                            for a in range(0,int(eCount),3):
                                actividadList.append(actList[a])
                    f.close()
    actividad_dropdown = OptionMenu(changeAllStudentDataLayout, actividadVar, *actividadList)
    actividad_dropdown.place(x=400, y=320, width=200)

''' Labels '''
course_Label = Label(changeAllStudentDataLayout, text='Escoger el curso', font=('arial', 13), bg=mainColor.get(), fg='white')
course_Label.place(x=430, y=200)
''' Dropdown '''
course_dropdown = OptionMenu(changeAllStudentDataLayout, courseVar, *courseNamesList, command=handleTwo)
course_dropdown.place(x=400, y=230, width=200)

''' Labels '''
actividad_Label = Label(changeAllStudentDataLayout, text='Escoger la actividad', font=('arial', 13), bg=mainColor.get(), fg='white')
actividad_Label.place(x=425, y=290)

actividad_dropdown = OptionMenu(changeAllStudentDataLayout, actividadVar, value='')
actividad_dropdown.place(x=400, y=320, width=200)

''' Labels '''
points_Label = Label(changeAllStudentDataLayout, text='Escribir la puntuacion', font=('arial', 13), bg=mainColor.get(), fg='white')
points_Label.place(x=420, y=380)
''' Entry '''
points_entry = Entry(changeAllStudentDataLayout, textvariable=pointsVar, font=('arial', 12))
points_entry.place(x=400, y=410, width=200)

def deleteDrop():
    actividad_dropdown.destroy()


global evcount

def savePoints():
    evcount = 0
    arr = []
    arrValue = [str(pointsVar.get())]

    for course_Name in courseNamesList:
        data = course_Name
        if courseVar.get() == data:
            for file_Name in filesNamesList:
                if data in file_Name:
                    configFile = open(file_Name, 'r')
                    limit = len(configFile.readlines())
                    print('Total lines:', limit)
                    configFile.close()

                    with open(file_Name, 'r') as f:
                        arr = f.read().splitlines()

                    print(arr)

                    configFile = open(file_Name, 'r')

                    for countInit, line in enumerate(configFile):
                        if countInit == 1:
                            for c in configFile:
                                evcount = c
                                evcount = int(evcount) * 3
                                break

                            insert_at = int(evcount) + 5

                            for a in range((int(evcount) + 3), (limit+2)):

                                i = int(a)

                                if insert_at == a:
                                    print("first value: " + str(insert_at))
                                    arr[insert_at:insert_at] = arrValue
                                    insert_at = insert_at + 3
                                    print("second value: " + str(insert_at))

                                if a == limit:
                                    arr.append(arrValue[0])
                    configFile.close()

                    file = open(file_Name, 'w')
                    for ind in arr:
                        file.write(ind + "\n")
                    file.close()

''' Button '''
saveInfo_btn = Button(changeAllStudentDataLayout, text='Guardar', command=savePoints, state=ACTIVE, width=15, height=2)
saveInfo_btn.place(x=445, y=460)

''' Button '''
exitMenu_btn = Button(changeAllStudentDataLayout, text='Volver al menu', command=exitToM, state=ACTIVE, relief='raised', width=20, height=4)
exitMenu_btn.place(x=400, y=600, width=200)

"""
     Change Data only one student Layout ----------------------------------------------------------------------------------------------------------------------------------------------
"""
borderRegister_Label = Label(changeOneStudentDataLayout, height=1, bg="black")
borderRegister_Label.pack(fill='x')

Register_title = Label(changeOneStudentDataLayout, text='Modificacion de actividad de un estudiante',fg="white", bg=mainColor.get(), font=('arial', 30, 'bold'))
Register_title.pack(pady=25)

borderRegister_Label = Label(changeOneStudentDataLayout, height=1, bg="black")
borderRegister_Label.pack(fill='x')

''' BG Setting Color '''
leftSide_BG = Label(changeOneStudentDataLayout, bg=secondColor.get())
leftSide_BG.pack(ipadx=10, ipady=10, expand=True, fill='both', side='left')

middleSide_BG = Label(changeOneStudentDataLayout, bg=mainColor.get())
middleSide_BG.pack(ipadx=10, ipady=10, expand=True, fill='both', side='left')

rightSide_BG = Label(changeOneStudentDataLayout, bg=secondColor.get())
rightSide_BG.pack(ipadx=10, ipady=10, expand=True, fill='both', side='left')

''' Variables '''
studentVar = StringVar()
studentVar.set('')


global studentList
studentList = []

global actividadStudList
actividadList = []

global stuCount
global actCount

global arrST
arrST = []

def handleTwoOne(self):
    getActividadStud()
    getStudent()
    deleteDrop()

def getActividadStud():
    actividadStudList = []
    actCount = 0

    actList = ['']
    for course_Name in courseNamesList:
        data = course_Name
        if courseVar.get() == data:
            for file_Name in filesNamesList:
                if data in file_Name:
                    f = open(file_Name, 'r')
                    for i, line in enumerate(f):
                        if i == 1:
                            for c in f:
                                actCount = c
                                actCount = int(actCount) * 3
                                break

                            actList = f.read().splitlines()
                            for a in range(0,int(actCount),3):
                                actividadStudList.append(actList[a])
                    f.close()

    actividadSTUD_dropdown = OptionMenu(changeOneStudentDataLayout, actividadVar, *actividadStudList)
    actividadSTUD_dropdown.place(x=400, y=320, width=200)

def getStudent():
    studentList = []
    stuCount = 0

    arrST = []
    actList = ['']
    for course_Name in courseNamesList:
        data = course_Name
        if courseVar.get() == data:
            for file_Name in studentFilesList:
                if data in file_Name:

                    fi = open(file_Name, 'r')
                    arrST = fi.read().splitlines()
                    fi.close()

                    check = 0

                    for i in arrST:
                        if 'a' in i:
                            print(i)
                            if check == 0:
                                studentList.append(i)
                                check = 1
                        elif 'e' in i:
                            if check == 0:
                                studentList.append(i)
                                check = 1
                        elif 'o' in i:
                            if check == 0:
                                studentList.append(i)
                                check = 1
                        check = 0

    student_dropdown = OptionMenu(changeOneStudentDataLayout, studentVar, *studentList)
    student_dropdown.place(x=400, y=410, width=200)


''' Labels '''
course_Label = Label(changeOneStudentDataLayout, text='Escoger el curso', font=('arial', 13), bg=mainColor.get(),
                     fg='white')
course_Label.place(x=430, y=200)
''' Dropdown '''
course_dropdown = OptionMenu(changeOneStudentDataLayout, courseVar, *courseNamesList, command=handleTwoOne)
course_dropdown.place(x=400, y=230, width=200)

''' Labels '''
actividad_Label = Label(changeOneStudentDataLayout, text='Escoger la actividad', font=('arial', 13), bg=mainColor.get(),
                        fg='white')
actividad_Label.place(x=425, y=290)
''' Dropdown '''
actividadSTUD_dropdown = OptionMenu(changeOneStudentDataLayout, actividadVar, value='')
actividadSTUD_dropdown.place(x=400, y=320, width=200)

''' Labels '''
student_Label = Label(changeOneStudentDataLayout, text='Escoger el estudiante', font=('arial', 13), bg=mainColor.get(),
                      fg='white')
student_Label.place(x=420, y=380)
''' Dropdown '''
student_dropdown = OptionMenu(changeOneStudentDataLayout, studentVar, value='')
student_dropdown.place(x=400, y=410, width=200)

''' Labels '''
points_Label = Label(changeOneStudentDataLayout, text='Escribir la puntuacion', font=('arial', 13), bg=mainColor.get(),
                     fg='white')
points_Label.place(x=420, y=470)
''' Entry '''
points_entry = Entry(changeOneStudentDataLayout, textvariable=pointsVar, font=('arial', 12))
points_entry.place(x=400, y=500, width=200)

def deleteDropEstud():
    student_dropdown.destroy()
    actividadSTUD_dropdown.destroy()

global evstudcount

def savePointOne():
    evstudcount = 0
    arr = []
    arrValue = [str(pointsVar.get())]

    for course_Name in courseNamesList:
        data = course_Name
        if courseVar.get() == data:
            for file_Name in filesNamesList:
                if data in file_Name:
                    configFile = open(file_Name, 'r')
                    limit = len(configFile.readlines())
                    print('Total lines:', limit)
                    configFile.close()

                    with open(file_Name, 'r') as f:
                        arr = f.read().splitlines()

                    name = studentVar.get()

                    for value in arr:
                        if value == name:
                            index = arr.index(name)

                            print(index)

                            index = index + 2

                            arr[index:index] = arrValue

                    print(arr)

                    file = open(file_Name, 'w')
                    for ind in arr:
                        file.write(ind + "\n")
                    file.close()

''' Button '''
saveInfo_btn = Button(changeOneStudentDataLayout, text='Guardar', command=savePointOne, state=ACTIVE, width=15,
                      height=2)
saveInfo_btn.place(x=445, y=550)

''' Button '''
exitMenu_btn = Button(changeOneStudentDataLayout, text='Volver al menu', command=exitToM, state=ACTIVE, relief='raised',
                      width=20, height=4)
exitMenu_btn.place(x=400, y=700, width=200)


show_layout(logInLayout)

app.mainloop()

