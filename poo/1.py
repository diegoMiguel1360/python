#Escriba una clase Empleado que tenga como propiedades nombre, cargo, salario
class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario

#escriba metodos contructores, setters y getters
    def getNombre(self):
        return self.__nombre
    
    def getCargo(self):
        return self.__cargo
    
    def getSalario(self):
        return self.__salario
    
    def setNombre(self,nombre):
        self.__nombre=nombre

    def setCargo(self,cargo):
        self.__cargo=cargo

    def setSalario(self,salario):
        self.__salario=salario

#escriba un método que permita calcular cuanto gana el empleado en una hora
    def xhora(self):
        hora=self.__salario/240
        return round(hora,2)
    
#un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3%
    def ipc(self):
        minimo=1160000
        if self.__salario<minimo:
            return "el salario es menor al minimo"
        if self.__salario==minimo:
            self.__salario*=1.163
        else:
            self.__salario*=1.133
        return round(self.__salario,2)
    
#Un método que reciba una cantidad de horas extras y calcule el salario incementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide
    def extras(self,horas):
        hora=self.__salario/240
        if horas <= 10:
            hora*=horas
            self.__salario+=hora
        else:
            hora*=10
            self.__salario+=hora
        return round(self.__salario,2)


emp1=Empleado('Diego','Gerente',11600000)
emp2=Empleado('Miguel','Director',5000000)
print(emp1.getSalario())
print(emp1.xhora())
print(emp1.ipc())
print(emp1.extras(10))
print(emp2.getCont())