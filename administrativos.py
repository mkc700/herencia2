# administrativos.py
from persona import Persona

class Administrativos(Persona):
    def _init_(self):
        super()._init_()
        self._cargo = ""

    # Getter y Setter
    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Cargo: {self._cargo}"