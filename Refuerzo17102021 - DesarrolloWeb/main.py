#py -m pip install -U pip
#pip install flask


#Importamos Flask, jsonify, request y las clases que necesitemos
from flask import Flask, jsonify, request
from pizza import Pizza

#Crear listas de los Objetos que necesiten
Pizzas = []

#En este caso agregamos datos desde aquí, para pruebas
Pizzas.append(Pizza(10,'Grande', 155, 'Napolitana'))
Pizzas.append(Pizza(20,'Pequeña', 105, 'Pepperoni'))
Pizzas.append(Pizza(30,'Mediana', 115, 'Champiñones'))

#Iniciamos Flask
app = Flask(__name__)

#Ruta de prueba, ayuda a comprobar que está corriendo la API
@app.route('/prueba')
def prueba():
    return jsonify({"saludo": "hola"})

#Método GET, permite obtener y visualizar todos los datos, contiene una url general /Pizzas
@app.route('/Pizzas', methods=['GET'])
def getPizzas():
    global Pizzas
    Datos = []
    for pizza in Pizzas:
        objeto = {
            'id': pizza.getId(),
            'tamaño': pizza.getTamaño(),
            'precio': pizza.getPrecio(),
            'especialidad': pizza.getEspecialidad()
        }
        Datos.append(objeto)
    return(jsonify(Datos))


#Método Get, permite obtener y visualizar un solo dato según el id, desde la url enviamos el id /Pizza/id
@app.route('/Pizzas/<int:id>', methods=['GET'])
def ObtenerPizza(id):
    global Pizzas
    for pizza in Pizzas:
        if pizza.getId() == id:
            objeto = {
            'id': pizza.getId(),
            'tamaño': pizza.getTamaño(),
            'precio': pizza.getPrecio(),
            'especialidad': pizza.getEspecialidad()

            }
            return(jsonify(objeto))
    
    salida = {"Mensaje": "No existe la pizza con ese id"}
    return(jsonify(salida))


#Método PUT, permite actualizar un Objeto según el id que enviemos, igual con url /Pizzas/id
@app.route('/Pizzas/<int:id>' , methods=['PUT'])
def ActualizarPiza(id):
    global Pizzas
    for i in range (len(Pizzas)):
        if id == Pizzas[i].getId():
            Pizzas[i].setId(int(request.json['id']))
            Pizzas[i].setTamaño(request.json['tamaño'])
            Pizzas[i].setPrecio(float(request.json['precio']))
            Pizzas[i].setEspecialidad(request.json['especialidad'])

            return jsonify({'Mensaje': "se actualizo el dato correctamente"})
    
    return jsonify({'Mensaje': "no se encontro el dato para actualizar"})


#Permiten agregar objetos a nuestra lista de datos, aquí recibimos el .json que contiene los datos
@app.route('/Pizzas', methods=['POST'])
def AgregarPizzas():
    global Pizzas
    id = request.json['id']
    tamaño = request.json['tamaño']
    precio = request.json['precio']
    especialidad = request.json['especialidad']
    nuevo = Pizza(int(id), tamaño, float(precio), especialidad)
    Pizzas.append(nuevo)
    return jsonify({'mensaje':'Se agregó una pizza al inventario'})


#Permite eliminar algún dato, igual enviando el id dentro de la url
@app.route('/Pizzas/<int:id>', methods=['DELETE'])
def EliminarPizza(id):
    global Pizzas
    for i in range(len(Pizzas)):
        if id == Pizzas[i].getId():
            del Pizzas[i]
            return jsonify({'mensaje':'Se eliminó la pizza con id: ' + str(id)})
    return jsonify({'mensaje':'No se encontró el dato a eliminar'})





#Permite correr la aplicación, colocamos el puerto donde queremos trabajar. 
#Debug = True, permite que mientras guardemos cambios la api siga actualizandose, sin necesidad  de reiniciar el main
if __name__ == '__main__':
    app.run(host="localhost",debug=True, port=4000)