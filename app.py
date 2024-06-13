from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Function to read tasks from JSON file
def read_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks

# Function to write tasks to JSON file
def write_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

# Endpoint to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    tasks = read_tasks()
    data = request.get_json()

    new_task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data['description']
    }

    tasks.append(new_task)
    write_tasks(tasks)  # Save updated tasks to JSON file

    return jsonify(new_task), 201

# Endpoint to retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = read_tasks()
    return jsonify(tasks), 200

if __name__ == '__main__':
    app.run(debug=True)
