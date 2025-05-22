from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todo_list = []

@app.route('/')
def index():
    return render_template('index.html', tasks=todo_list)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todo_list.append({'task': task, 'done': False})
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    if 0 <= task_id < len(todo_list):
        todo_list[task_id]['done'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(todo_list):
        todo_list.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
