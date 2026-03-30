# REgistrar, consultar, actualizar, eliminar estudiantes
#ID, nombre, Edad, curso o programa, estado(activo/inactivo)


student={
    1:{
        "id": 1001820882,
        "name": "Sharon Merino",
        "age": 25,
        "course": "engineering",
        "state": "active"
    }}

def menu ():
    c = 1
    opt = ""
    while opt !="exit":
        opt = input("Write the option:\n 1.Add\n 2.Search\n 3.Ref\n 4.Remove\n 5.Exit\n")
        opt = opt.lower().strip()
        if opt == "add":
            c=add(c)
        elif opt == "search":
            search()
        #elif opt == ""
        elif opt == "remove":
            remove()
        elif opt == "exit":
            print("Exit menu!")
        else:
            print("INVALID OPTION!!!\n")


def add():
    
    ve = False
    while not ve:
        try:
            id = int(input("Write the ID number: "))
            name = str(input("Write the full name: "))
            age = int(input("Wirte the age: "))
            course = str(input("Write name of the course or program: "))
            state = str(input("Write the student's status (active/inactive): "))
            contad+=1
            student[contad] ={"id":id, "name":name, "age":age, "course":course, "state":state}
            print(student)
            ve = True
        except:
            print("INVALID INPUT!!!")

    return contad
        
def search():
    
    search_id = int(input("Write the ID to search: "))
    found = "The ID does not exit\n"
    for tiro,coda in student.items():
        if coda["id"] ==search_id:
            found = coda
    print(found)

#def actualizar

def remove():
    rem = int(input("Write the number of the registry you want to remove"))
    del(student[rem])


menu()
