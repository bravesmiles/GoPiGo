#!flask/bin/python
# run with flask
from flask import Flask, jsonify, request, Response, make_response, abort

from crosutil import crossdomain

app = Flask(__name__)

# default handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/car/api/v1.0/test', methods=['GET'])
@crossdomain(origin='*')
def test():
    return jsonify({'tasks': 'kitty'})

@app.route('/car/api/v1.0/tasks', methods=['GET'])
@crossdomain(origin='*')
def get_tasks():
    return jsonify({'hello': 'kitty'})

@app.route('/car/api/v1.0/tasks/<int:task_id>', methods=['GET'])
@crossdomain(origin='*')
def get_task(task_id):
    print task_id
    return jsonify({'hello': 'kitty'})


# run as a app
if __name__ == '__main__':
    app.run(host='10.154.176.25', debug=True)