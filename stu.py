# REgistrar, consultar, actualizar, eliminar estudiantes
#ID, nombre, Edad, curso o programa, estado(activo/inactivo)

c=1
student={
    1:{
        "id": 1001820882,
        "name": "Sharon Merino",
        "age": 25,
        "course": "engineering",
        "state": "active"
    }}

def menu (): 
    opt = ""
    while opt !="exit":
        opt = str(input("Write the option:\n 1.Add\n 2.Search\n 3.Update\n 4.Remove\n 5.Exit\n"))
        opt = opt.lower().strip()
        if opt == "add":
            add(c)
        elif opt == "search":
            search()
        elif opt == "update":
            update()
        elif opt == "remove":
            remove()
        elif opt == "exit":
            print("Exit menu!")
        else:
            print("INVALID OPTION!!!\n")


def add(cont):
    ve = False
    cont = 1
    while not ve:
        try:
            id = int(input("Write the ID number: "))
            if id < 0:
                add()
            name = str(input("Write the full name: "))
            age = int(input("Wirte the age: "))
            if age < 0:
                add()
            course = str(input("Write name of the course or program: "))
            state = str(input("Write the student's status (active/inactive): "))
            if state != "active" and state !="inactive":
                add()
            cont = cont + 1
            student[cont] ={"id":id, "name":name, "age":age, "course":course, "state":state}
            print(student)
            ve = True
        except:
            print("INVALID INPUT!!!\n")
    return cont
    
        
def search():
    ve = False
    while not ve:
        try:
            search_id = int(input("Write the ID to search: "))
            found = "The ID does not exit\n"
            for tiro,coda in student.items():
                if coda["id"] ==search_id:
                    found = coda
            print(found)
            ve = True
        except:
            print("INVALID INPUT!!!")


def update():
        ve = False
        while not ve:
            try:
                confi_student={}
                nn = int(input("Write the number of the registry: "))
                id = int(input("Write the ID number: "))
                if id < 0:
                    add()
                name = str(input("Write the full name: "))
                age = int(input("Wirte the age: "))
                if age < 0:
                    add()
                course = str(input("Write name of the course or program: "))
                state = str(input("Write the student's status (active/inactive): "))
                if state != "active" and state !="inactive":
                    add()
                confi_student [nn]= {"id":id, "name":name, "age":age, "course":course, "state":state}
                student.update(confi_student)
                print(student)
            except:
                print("INVALID INPUT!!!")

    

def remove():
    ve = False
    while not ve:
        try:
            rem = int(input("Write the number of the registry you want to remove: "))
            del(student[rem])
            ve = True
            print(student)
        except:
            print("INVALID INPUT!!!\n")


menu()
