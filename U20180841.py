import abc

class Persona(abc.ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @abc.abstractmethod
    def descripcion(self):
        pass

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def descripcion(self):
        return f"Soy {self.nombre}, tengo {self.edad} años y estoy en {self.grado}er año en la carrera de Ingeniería en Desarrollo de Software en la UNIVO."

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia
    
    def descripcion(self):
        return f"Soy el profesor {self.nombre}, tengo {self.edad} años y enseño {self.materia} en la UNIVO."

class Administrativo(Persona):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad)
        self.cargo = cargo
    
    def descripcion(self):
        return f"Soy {self.nombre}, tengo {self.edad} años y trabajo como {self.cargo} en la UNIVO."

personas = [Estudiante("Juan", 15, 3), Profesor("W. Morales", 30, "POO"), Administrativo("Pedro", 38, "Secretario")]

for persona in personas:
    print(persona.descripcion())