from flask import Flask,  jsonify, request

app = Flask(__name__)

# dummy data
todos = [
    { "label": "My first task", "done": False, "id": 1 },
    { "label": "My second task", "done": False, "id": 2 },
]


@app.route('/', methods=['GET'])
def hello_world():
    return '<h1>Hello Rick!</h1>'


@app.route('/todos', methods=['GET'])
def get_todos():

    response = {
        'message': 'Sending you list of todos!',
        'todos': todos,
    }
    return jsonify(response), 200


@app.route('/todos', methods=['POST'])
def add_todo():
    request_body = request.json
    todos.append(request_body)

    response = {
        'message': 'Received new POST request!',
        'todos': todos,
    }

    return jsonify(response), 200


@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    
    for todo in todos:
        if todo.get('id') == id:
            todos.remove(todo)
            break

    response = {
        'message': f'Received request to DELETE for id {id}',
        'todos': todos,
    }

    return jsonify(response), 200

# create a route to UPDATE (PUT) a todo



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)