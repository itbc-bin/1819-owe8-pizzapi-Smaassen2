from flask import Flask, jsonify, request

app = Flask(__name__)

pizzaDB = [
            {'name': 'tonno', 'price': 5.25, 'ingredients': ['cheese', "tuna"]},
            {'name': 'salami', 'price': 5.55, 'ingredients': ['cheese', 'salami']},
            {'name': 'hawaii', 'price': 6.25, 'ingredients': ['cheese', 'pineapple']}
          ]

@app.route("/", methods=['GET'])
def getPizza():
    return jsonify({'pizzaDB':pizzaDB})

@app.route("/<string:name>", methods=['GET'])
def getOnePizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(pizza)
    return jsonify({'pizzaDB':resultPizza})

@app.route("/", methods=['POST'])
def addOnePizza():
    print(request.values.to_dict())
    pizza = {'name' : request.values.to_dict()['name'], 'price' : request.values.to_dict()['price'], 'ingredients' : request.values.to_dict()['ingredients']}
    pizzaDB.append(pizza)
    return jsonify({'pizzaDB' : pizzaDB})

@app.route("/<string:name>", methods=['PUT'])
def putPizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            print("test")
            resultPizza.append(pizza)
    print(request.values.to_dict())
    if 'ingredients' in request.values.to_dict().keys():
        print(request.values.to_dict())
        resultPizza[0]['ingredients'].append(request.values.to_dict()['ingredients'])

    if 'name' in request.values.to_dict().keys():
        resultPizza[0]['name'] = request.values.to_dict()['name']


    return jsonify({'pizzaDB': pizzaDB})


@app.route("/<string:name>", methods=['DELETE'])
def delPizza(name):
    resultPizza = []
    for pizza in pizzaDB:
        if pizza['name'] == name:
            resultPizza.append(pizza)
    pizzaDB.remove(resultPizza[0])
    return jsonify({'pizzaDB': pizzaDB})

if __name__ == "__main__":
    app.run(debug=True, port=8080)
