# REgistrar, consultar, actualizar, eliminar estudiantes
#ID, nombre, Edad, curso o programa, estado(activo/inactivo)

student={}

def menu ():
    opt = input("Write the option:\n 1.Add\n 2.Search\n 3.Ref\n 4.Remove\n 5.Exit\n")
    opt = opt.lower().strip()



def add():
    c = 0
    ve = False
    while not ve:
        try:
            id = int(input("Write the ID number: "))
            name = str(input("Write the full name: "))
            age = int(input("Wirte the age: "))
            course = str(input("Write name of the course or program: "))
            state = str(input("Write the student's status (active/inactive): "))
            c+=1
            student = {c:{"id":id, "name":name, "age":age, "course":course, "state":state}}
            print(student)
            ve = True
        except:
            print("INVALID INPUT!!!")
        
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