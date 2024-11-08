# persona.py
class Persona:
    def __init__(self):
        self._nombre = None
        self._apellido = None

    def _init_(self):
        self._nombre = ""
        self._apellido = ""
        self._edad = 0

    # Getters y Setters
    def get_nombre(self):
        #if self._nombre == "" or self.nombre is None :
        #    print("Valor vacio")
        #else:
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre
       # if self._nombre == "":
       #     print("esto esta mal")
       # else:
       #     self._nombre = nombre


    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def mostrar_informacion(self):
        if self._nombre == "":
            return print("Valor erroneo: no hay nombre")
        else:
            return f"Nombre: {self._nombre} {self._apellido}, Edad: {self._edad}"

