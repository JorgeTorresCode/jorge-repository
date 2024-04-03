from termcolor import colored

class Personaje:
    # Constructor para inicializar las propiedades del personaje
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    # Método para representar el objeto como una cadena
    def __repr__(self):
        nombre_color = colored(self.nombre.capitalize(),"light_yellow")
        return f'{nombre_color}, Fuerza: {self.fuerza}, Velocidad: {self.velocidad}'
    
    # Método para determinar como se va a comportar x operación entre personajes (en este caso suma)
    def __add__(self,otro):
        nuevo_nombre = f"{self.nombre[:2]}{otro.nombre[-4:]}".capitalize()
        nueva_fuerza = int(((self.fuerza + otro.fuerza)/2)**1.4)
        nueva_velocidad = int(((self.velocidad + otro.velocidad)/2)**1.4)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)


min_caracter = colored("Ingrese al menos un carácter","light_red")
no_personajes = colored("\nNo hay personajes creados","light_cyan")
no_encontrado = colored("No se encontró el personaje", "light_red")

characters = []
attempts = []

def clear():
    attempts.clear()


def counter():

    if len(attempts) >= 4:
        print(colored("Límite de intentos alcanzado, cerrando el programa", "light_magenta"))
        exit()
    else:
        attempts.append(1)
        

def crear_personaje():
    
    while True:
        nombre = input("\nNombre del personaje: ")
        
        if any(str(personaje.nombre).lower() == str(nombre).lower() for personaje in characters):
            
            counter()
            print(colored("Nombre en uso, elija otro","light_red"))
            continue
        
        nombrerep = nombre.replace(" ","")
        if len(nombrerep) > 0:
            clear()
            break
        
        else:
            counter()
            print(min_caracter)
                   
    while True:
        fuerza = input("Fuerza del personaje (int): ")
        
        try:
            int(fuerza)
            clear()
            break
        
        except:
            counter()
            print(colored("Fuerza inválida\n","light_red"))

    while True:
        velocidad = input("Velocidad del personaje (int): ")
        
        try:
            int(velocidad)
            clear()
            break
        
        except:
            counter()
            print(colored("Velocidad inválida\n","light_red"))
        
    nuevo_personaje = Personaje(nombre, int(fuerza), int(velocidad))
    characters.append(nuevo_personaje)
    print(colored("\n¡Personaje creado corectamente!","light_green"))
    return nuevo_personaje



def fusionar_personajes():
    if len(characters) >= 2:
        print(colored("\n\nPersonajes disponibles:\n","light_blue"))

        for i in characters:
            print(i)

        while True:
            while True:
                prj1 = input("\nPrimer personaje a fusionar: ")
                
                #Verifica y define que prj1 sea igual a su personaje en la lista
                personaje1 = next((p for p in characters if p.nombre.capitalize() == prj1.capitalize()), None)
            
                prj1rep = prj1.replace(" ","")
                if personaje1:
                    clear()
                    break
                
                elif len(prj1rep) == 0:
                    counter()
                    print(min_caracter)
                
                else:
                    counter()
                    print(no_encontrado)

            while True:
                prj2 = input("\nSegundo personaje a fusionar: ")

                if prj2.capitalize() == prj1.capitalize():
                    counter()
                    print(colored("No puedes fusionar al mismo personaje, escoge otro", "light_red"))
                    
                else:
                    personaje2 = next((i for i in characters if i.nombre.capitalize() == prj2.capitalize()), None)
                    
                    prj2rep = prj2.replace(" ","")
                    if personaje2:
                        clear()
                        characters.remove(personaje1)
                        characters.remove(personaje2)
                        break
                    
                    elif len(prj2rep) == 0:
                        counter()
                        print(min_caracter)
                    
                    else:
                        counter()
                        print(no_encontrado)

            break
    
    elif len(characters) == 1:
        print(colored("\nPersonajes insuficientes","light_cyan"))
        return
        
    else:
        print(no_personajes)
        return

    fusion = personaje1 + personaje2
    
    if fusion.nombre.lower() in (str(character.nombre).lower() for character in characters):
        
        counter()
        print(colored("\nFusión ya realizada anteriormente o personaje existente con el mismo nombre resultante","light_red"))
        return
    
    else:
        clear()
        characters.append(fusion)
        colored_nombre_creado = colored(f"\nTu nuevo personaje se llama ¡{fusion.nombre.capitalize()}!","light_cyan")
        colored_creado = colored(f"\n¡Personaje creado correctamente!","light_green")
        
        return print(f"{colored_nombre_creado}{colored_creado}")



def enfrentar_personajes():
    if len(characters) >= 2:
        print(colored("\n\nPersonajes disponibles:\n","light_blue"))

        for i in characters:
            print(i)

        while True:
            while True:
                prj1 = input("\nPrimer personaje a enfrentar: ")
                
                #Verifica y define que prj1 sea igual a su personaje en la lista
                personaje1 = next((p for p in characters if p.nombre.capitalize() == prj1.capitalize()), None)

                prj1rep = prj1.replace(" ","")
                if personaje1:
                    clear()
                    break
                
                elif len(prj1rep) == 0:
                    counter()
                    print(min_caracter)
                
                else:
                    counter()
                    print(no_encontrado)

            while True:
                prj2 = input("\nSegundo personaje a enfrentar: ")

                if prj2.capitalize() == prj1.capitalize():
                    counter()
                    print(colored("No puedes enfrentar al mismo personaje, escoge otro", "light_red"))
                    
                else:
                    #Verifica y define que prj2 sea igual a su personaje en la lista
                    personaje2 = next((i for i in characters if i.nombre.capitalize() == prj2.capitalize()), None)

                    prj2rep = prj2.replace(" ","")
                    if personaje2:
                        clear()
                        break
                
                    elif len(prj2rep) == 0:
                        counter()
                        print(min_caracter)
                    
                    else:
                        counter()
                        print(no_encontrado)
              
            break
    
    elif len(characters) == 1:
        print(colored("\nPersonajes insuficientes","light_cyan"))
        return
        
    else:
        print(no_personajes)
        return 
    
    per1 = personaje1.fuerza + personaje1.velocidad
    per2 = personaje2.fuerza + personaje2.velocidad
    
    if per1 > per2:
        print(colored(f"\n¡{personaje1.nombre.capitalize()} ha salido victorioso/a!","light_cyan"))
        print(colored(f" {personaje2.nombre.capitalize()} ha sido eliminado/a","light_red"))
        characters.remove(personaje2)
        
    elif per2 > per1:
        print(colored(f"\n¡{personaje2.nombre.capitalize()} ha salido victorioso/a!","light_cyan"))
        print(colored(f" {personaje1.nombre.capitalize()} ha sido eliminado/a","light_red"))
        characters.remove(personaje1)
        
    else:
        print(colored(f"\n¡{personaje1.nombre.capitalize()} ha empatado con {personaje2.nombre.capitalize()}!","light_cyan"))



def mostrar_personajes():
    if len(characters) == 0:
        print(no_personajes)
        
    else:
        print(colored("\n\nPersonajes:\n","light_blue"))
        for i in characters:
            print(i)



def eliminar_personaje():
    if len(characters) > 0:
        print(colored("\n\nSelecciona a quien quieres eliminar:\n","light_blue"))
        
        for i in characters:
            print(i)
            
        while True:
            eliminar = input("\nEliminar a: ")
            
            #Verifica y define que personaje sea igual a su personaje en la lista
            personaje = next((p for p in characters if p.nombre.capitalize() == eliminar.capitalize()), None)
            
            eliminarep = eliminar.replace(" ","")
            if personaje:
                clear()
                characters.remove(personaje)
                print(colored(f"\nSe eliminó a {personaje.nombre.capitalize()} correctamente", "green"))
                break
            
            elif len(eliminarep) == 0:
                counter()
                print(min_caracter)
            
            else:
                counter()
                print(no_encontrado)
                    
    else:
        print(no_personajes)



def eliminar_lista():
    if len(characters) == 0:
        print(no_personajes)

    else:
        Y = colored("Y","light_green")
        N = colored("N","light_red")
        
        selection = input(f"\n¿Estas seguro? ({Y}/{N}): ")
        
        selectionrep = selection.replace(" ","")
        
        if selection.lower() == "y":
            clear()
            characters.clear()
            print(colored("\n¡Todos los personajes fueros eliminados!","light_green"))
            
        elif selection.lower() == "n":
            clear()
            print(colored("\nNingún personaje ha sido eliminado","light_cyan"))
        
        elif len(selectionrep) == 0:
            counter()
            print(min_caracter)
        
        else:
            counter()
            print(colored("Respuesta inválida","light_red"))


#Bucle juego

while True:
    x = "-"
    print(f"""\n{x*30}
1. Crear personaje
2. Fusionar personajes
3. Enfrentar personajes
4. Mostrar personajes
5. Eliminar un personaje
6. Eliminar todos los personajes
7. Salir\n""")
    
    selection = input("Seleccione una opción: ")
    if selection.isdigit() and int(selection) in range(1,8):
        clear()
        pass
    
    else:
        counter()
        print(colored("\nOpción inexistente, ingrese una opción válida","light_red"))
        continue


    if selection == "1":
        crear_personaje()

    elif selection == "2":
        fusionar_personajes()
        
    elif selection == "3":
        enfrentar_personajes()

    elif selection == "4":
        mostrar_personajes()

    elif selection == "5":
        eliminar_personaje()

    elif selection == "6":
        eliminar_lista()

    elif selection == "7":
        print(colored("\n¡Juego terminado!","light_blue"))
        break