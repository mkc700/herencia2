# estudiantes.py
from persona import Persona

class Estudiantes(Persona):
    def _init_(self):
        super()._init_()
        self._matricula = ""


    # Getter y Setter
    def get_matricula(self):
        return self._matricula

    def set_matricula(self, matricula):
        self._matricula = matricula



    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Matrícula: {self._matricula}"