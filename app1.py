from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy Groceries',
        'description': u'Milk, Cheese, Pizza, Fruit',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'good resources for python',
        'done': False
    }
]

@app.route("/add-data", methods = ["POST"])

def addTask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data"
        }, 400)

    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "task added successfully"
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        "data": tasks
    })

if(__name__ == "_main_"):
    app.run(debug = True)

print("Hi")