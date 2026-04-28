
class Puesto: 
    def __init__(self,codigo,descripcion,areaSolicitante,plazaRequeridas,sueldo):
        self.codigo=codigo
        self.descripcion=descripcion
        self.areaSolicitante=areaSolicitante
        self.plazaRequeridas=plazaRequeridas
        self.sueldo=sueldo

    def __str__(self):
        return f"Codigo: {self.codigo}, Descripcion :  {self.descripcion}, Area: {self.areaSolicitante}, Plazas: {self.plazaRequeridas}, Sueldo: {self.sueldo}"

listaPuestos= []
def AgregarPuesto():
        codigo=int(input("Codigo: "))
        descripcion=input("Descripcion: ")
        area=input("Area: ")
        plazas=int(input("Plazas: "))
        sueldo=int(input("Sueldo: "))
        
        if len(descripcion) < 3 or len(area)< 3:
            print("Debe tener por lo menos 3 letras")
            
        if codigo < 0 or plazas < 0 or sueldo <0:
            print("codigo, plazaz o precio son menores que 0")
        
        for p in listaPuestos:
            if p.codigo == codigo or p.descripcion == descripcion or p.areaSolicitante ==area:
             print("Puesto ya ocupado")   
             return
        nuevo=Puesto(codigo,descripcion,area,plazas,sueldo)
        listaPuestos.append(nuevo)

def MostrarTodo():
        if len(listaPuestos) == 0:
            print("la lista esta vacia")
            return
        for p in listaPuestos:
            print(p)
    
def BorrarPuesto():
        codigo=int(input("Ingreese el codigo a eliminar: "))
        n=len(listaPuestos)
        for pasada in range(n - 1):
            for izqpar in range(n - 1 - pasada):
                derpar = izqpar + 1
                if listaPuestos[izqpar].codigo < listaPuestos[derpar].codigo:
                    listaPuestos[izqpar], listaPuestos[derpar] = listaPuestos[derpar], listaPuestos[izqpar]

        pos =-1
        for i in range(len(listaPuestos)):
            if listaPuestos[i].codigo==codigo:
                pos = i 
                break
        
        if pos !=-1:
            for i in range(pos,len(listaPuestos)-1):
                listaPuestos[i]=listaPuestos[i+1]
            listaPuestos.pop()

def BuscarSueldo():
    for i in range(1, len(listaPuestos)):
        aux = listaPuestos[i]
        j = i - 1
        while j >= 0 and listaPuestos[j].sueldo < aux.sueldo:
            listaPuestos[j + 1] = listaPuestos[j]
            j -= 1
        listaPuestos[j + 1] = aux

    sueldo = float(input("Sueldo a buscar: "))

    lower = 0
    higher = len(listaPuestos)
    middle = 0

    while lower + 1 < higher:
        middle = (lower + higher)//2
        if listaPuestos[middle].sueldo == sueldo:
            break
        elif listaPuestos[middle].sueldo < sueldo:
            higher = middle
        else:
            lower = middle

    if len(listaPuestos) > 0 and listaPuestos[middle].sueldo == sueldo:
        print(f"Encontrado en la posicion {middle+1}")

        i = middle
        while i >= 0 and listaPuestos[i].sueldo == sueldo:
            print(listaPuestos[i])
            i -= 1

        i = middle + 1
        while i < len(listaPuestos) and listaPuestos[i].sueldo == sueldo:
            print(listaPuestos[i])
            i += 1
    else:
        print("NO Encontrado")
    
    
def PuestosAContratar():
    presupuesto = float(input("Presupuesto total: "))

    n = len(listaPuestos)

    # SELECCION (mayor a menor)
    for i in range(n - 1):
        posmayor = i
        for j in range(i + 1, n):
            total_j = listaPuestos[j].plazaRequeridas * listaPuestos[j].sueldo
            total_mayor = listaPuestos[posmayor].plazaRequeridas * listaPuestos[posmayor].sueldo
            if total_j > total_mayor:
                posmayor = j

        aux = listaPuestos[i]
        listaPuestos[i] = listaPuestos[posmayor]
        listaPuestos[posmayor] = aux

    total_acumulado = 0

    for i in range(len(listaPuestos)):
        costo = listaPuestos[i].plazaRequeridas * listaPuestos[i].sueldo
        if total_acumulado + costo <= presupuesto:
            print(listaPuestos[i], "Costo total:", costo)
            total_acumulado += costo

    print("Total usado:", total_acumulado)

while True:
    print("--- MENU ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Borrar")
    print("4. Buscar sueldo")
    print("5. Puestos a contratar")
    print("6. Salir")

    op = input("Opcion: ")

    if op == "1":
        AgregarPuesto()
    elif op == "2":
        MostrarTodo()
    elif op == "3":
        BorrarPuesto()
    elif op == "4":
        BuscarSueldo()
    elif op == "5":
        PuestosAContratar()
    elif op == "6":
        break
    else:
        print("Opcion invalida")
        