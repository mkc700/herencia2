# empleado_limpieza.py
from empresa import Empresa
from persona import Persona


class EmpleadoLimpieza(Persona,Empresa):
    def _init_(self):
        Persona._init_(self)
        Empresa._init_(self)
        self._numero_empleado = ""

    # Getter y Setter
    def get_numero_empleado(self):
        return self._numero_empleado

    def set_numero_empleado(self, numero_empleado):
        self._numero_empleado = numero_empleado

    def mostrar_informacion(self):
        base_info_persona = Persona.mostrar_informacion(self)
        base_info_empresa = Empresa.mostrar_informacion(self)
        return f"{base_info_persona}, Número de Empleado: {self._numero_empleado}, {base_info_empresa}"

'''



'''