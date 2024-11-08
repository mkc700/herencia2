# profesores.py
from persona import Persona

class Profesores(Persona):
    def _init_(self):
        super()._init_()
        self._departamento = ""
        self._categoria = ""
        self._maxgradoestudios = ""

    # Getter y Setter
    def get_categoria(self):
        return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_MaxGradoEstudios(self):
        return self._maxgradoestudios

    def set_MaxGradoEstudios(self, maxgradoestudios):
        self._maxgradoestudios = maxgradoestudios

    def get_departamento(self):
        return self._departamento

    def set_departamento(self, departamento):
        self._departamento = departamento

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Departamento: {self._departamento}, Categoria: {self._categoria},\n Maximo Grado de Estudios: {self._maxgradoestudios}"