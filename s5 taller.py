from datetime import date
import os
class User: #Clase
    def __init__(self,nombre,cedula,direccion,telefono,correo):
        self.nombre=nombre
        self.cedula=cedula
        self.direccion=direccion
        self.telefono=telefono
        self.correo=correo
class Persona(User):  #Clase que hereda de la clase User
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        super().__init__(nombre, cedula, direccion, telefono, correo)
    def mostrarEstudiante(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.telefono} {self.correo}")
class Administrador(User):   #Clase
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        super().__init__(nombre, cedula, direccion, telefono, correo)
    def mostrarDocente(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.telefono} {self.correo}")
from abc import ABC, abstractclassmethod
class Rol(ABC):  #Clase
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        super().__init__(nombre, cedula, direccion, telefono, correo)
    @abstractclassmethod
    def mostrarRol(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.telefono} {self.correo}")
class User:  #Clase
    def __init__(self,nombre,cedula,direccion,telefono,correo):
        self.nombre=nombre
        self.cedula=cedula
        self.direccion=direccion
        self.telefono=telefono
        self.correo=correo
class Estudiante(User): 
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        super().__init__(nombre, cedula, direccion, telefono, correo)
    def mostrarEstudiante(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.telefono} {self.correo}")
class Docente(User):
    def __init__(self, nombre, cedula, direccion, telefono, correo):
        super().__init__(nombre, cedula, direccion, telefono, correo)
    def mostrarDocente(self):
        print(f"{self.nombre} {self.cedula} {self.direccion} {self.telefono} {self.correo}")
class OpcSistema:   #Clase
    _registro=0
    def __init__(self,codigo,descripcion,record,nomb,rol,emp,ruc):
        self.codigo=codigo
        self.descripcion=descripcion
        self.consulta=record
        OpcSistema._registro+=1
        self._registro="#0"+str(OpcSistema._registro)
        self.date=date.today()
        self.nomb=nomb
        self.rol=rol
        self.emp=emp
        self.ruc=ruc
    def mostrarOpcSistemaPersona(self):
        print(f"Consulta: {self._registro:14} Empresa: {self.emp:14} Fecha: {self.date}")
        print(f"Nombre: {self.nomb:16} Ruc: {self.ruc:18} Rol: {self.rol}")
        print("*"*29,"Record crediticio","*"*29)
        print("Cedula              Estado        Record crediticio")
        print(f"{self.codigo:14} {self.descripcion:25} {self.consulta}")
    def mostrarOpcSistemaAdministrador(self):
        print()
        print(f"Consulta: {self._registro:20} Empresa: {self.emp:24} Fecha: {self.date}")
        print(f"Nombre: {self.nomb:22} Ruc: {self.ruc:29}Rol: {self.rol}")
        print("*"*45,"Record crediticio","*"*45)
        print("Codigo        Nombre       Record crediticio   Aumentar/disminuir record crediticio   Ultima modificacion")
        print("{:7} {:22} {:30} +{}-                  {} " .format(self.codigo,self.descripcion,self.consulta,OpcSistema._registro, self.date))
while True:
    
    print()
    print(" "*20,"Menu"," "*20)
    print("1.-Persona natural/juridica")
    print("2.-Administrador")
    print("3.-Salir")
    opc= int(input("Ingrese una opcion [1...3]: "))
    if opc ==1:
        os.system("cls")
        print(" "*20,"Opcion del sistema"," "*20)
        print("1.- Consultar buro crediticio ")
        print("2.- Volver al menu principal")
        print("3.- Presione cualquier tecla para salir")
        opc2=input("Ingrese una opcion [1...3]: ")
        if opc2 == '1':
            os.system("cls")
            notas = OpcSistema("0910001291","Central de riesgo","85","Allisson Astudillo","Personal natural","Consulta SA","0900012301001")
            notas.mostrarOpcSistemaPersona()
            opc3=input("Seleccione cualquier tecla para regresar al menu principal: ")
            if opc3 ==opc3:
                os.system("cls")
            else:
                os.system("cls")
                print("Opcion incorrecta")
        elif opc2 =='2':
            os.system("cls")
        elif opc2==opc2:
            os.system("cls")
            print("Gracias por utilizar nuestro servicio")
            break
        else:
            os.system("cls")
            print("Opcion incorrecta")
    elif opc ==2:
        os.system("cls")
        print(" "*20,"Opcion del sistema"," "*20)
        print("1.- Consultar buro crediticio: ")
        print("2.- Volver al menu principal")
        print("3.- Presione cualquier tecla para salir")
        opc4=input("Seleccione una opcion [1...3]: ")
        if opc4 == '1':
            os.system("cls")
            notas2= OpcSistema("0910001291","Allisson Astudillo","85","Lourdes","Administradora","Consulta SA","0900012301001")
            notas2.mostrarOpcSistemaAdministrador()
            print()
            opc5=input("Seleccione cualquier tecla para regresar al menu principal: ")
            if opc5 ==opc5:
                os.system("cls")
            else:
                os.system("cls")
                print("Opcion incorrecta")
        elif opc4 =='2':
            os.system("cls")
        elif opc4==opc4:
            os.system("cls")
            print("Gracias por utilizar nuestro servicio")
            break
        else:
            os.system("cls")
            print("Opcion incorrecta")
    elif opc ==3:
        os.system("cls")
        print("Gracias por utilizar nuestro servicio")
        break
    else:
        os.system("cls")
        print("Opcion incorrecta")