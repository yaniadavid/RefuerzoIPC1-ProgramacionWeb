class Pizza:
    def __init__(self, id, tamaño, precio, especialidad):
        self.id = id
        self.tamaño = tamaño
        self.precio = precio
        self.especialidad = especialidad


    #METODOS GET
    def getId(self):
        return self.id

    def getTamaño(self):
        return self.tamaño
    
    def getPrecio(self):
        return self.precio

    def getEspecialidad(self):
        return self.especialidad
    
    #METODOS SET
    def setId(self, id):
        self.id = id

    def setTamaño(self, tamaño):
        self.tamaño = tamaño
    
    def setPrecio(self, precio):
        self.precio = precio

    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad