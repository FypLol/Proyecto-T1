
class Puesto: 
    def __init__(self,codigo,descripcion,areaSolicitante,plazaRequeridas,sueldo):
        self.codigo=codigo
        self.descripcion=descripcion
        self.areaSolicitante=areaSolicitante
        self.plazaRequeridas=plazaRequeridas
        self.sueldo=sueldo

    def __str__(self):
        return f"Codigo: {self.codigo}, Descripcion :  {self.descripcion}, Area: {self.areaSolicitante}, Plazas: {self.plazaRequeridas}, Sueldo: {self.sueldo}"

    listaPuestos=[]
     
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
        
        