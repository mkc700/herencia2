# profesores.py
from persona import Persona

class Profesores(Persona):
    def _init_(self):
        super()._init_()
        self._departamento = ""

    # Getter y Setter
    def get_departamento(self):
        return self._departamento

    def set_departamento(self, departamento):
        self._departamento = departamento

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Departamento: {self._departamento}"