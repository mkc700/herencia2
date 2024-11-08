# main.py
from estudiantes import Estudiantes
from profesores import Profesores
from administrativos import Administrativos
from empleado_limpieza import EmpleadoLimpieza

def main():



    # Crear objetos

    estudiante = Estudiantes()
    estudiante.set_nombre("Juan")
    estudiante.set_apellido("Pérez")
    estudiante.set_edad(20)
    estudiante.set_matricula("123456")
    estudiante.set_carrera("programacion")
    estudiante.set_semestre(5)


    profesor = Profesores()
    profesor.set_nombre("Manuel")
    profesor.set_apellido("López")
    profesor.set_edad(40)
    profesor.set_departamento("Matemáticas")
    profesor.set_MaxGradoEstudios("Licenciatura")
    profesor.set_categoria("docente")


    administrativo = Administrativos()
    administrativo.set_nombre("Carlos")
    administrativo.set_apellido("González")
    administrativo.set_edad(35)
    administrativo.set_cargo("Secretario")
    administrativo.set_area("Recursos Humanos")



    empresa = EmpleadoLimpieza()
    empresa.set_nombre("Iñigo")
    empresa.set_apellido("Martínez")
    empresa.set_edad(45)
    empresa.set_numero_empleado("E1234")
    empresa.set_turno("mañana")
    empresa.set_nombre_empresa("Limpieza S.A.")
    empresa.set_direccion("Calle Ficticia 123")

    # Mostrar información

    print("\nProfesor:")
    print(profesor.mostrar_informacion())


    print("Estudiante:")
    print(estudiante.mostrar_informacion())

    print("\nAdministrativo:")
    print(administrativo.mostrar_informacion())


    print("\nEmpleado de Limpieza:")
    print(empresa.mostrar_informacion())


main()