#!flask/bin/python
# run with flask
from flask import Flask, jsonify, request, Response, make_response, abort
import gopigo
import time

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


@app.route('/car/api/v1.0/task', methods=['POST'])
@crossdomain(origin='*')
def add_tasks():
    json = request.json
    description = json['description']
    command = json['command']
    period = int(json['time'])

    process_command(command, period)
    return jsonify(json)


@app.route('/car/api/v1.0/tasks', methods=['GET'])
@crossdomain(origin='*')
def get_tasks():
    return jsonify({'hello': 'kitty'})


@app.route('/car/api/v1.0/tasks/<int:task_id>', methods=['GET'])
@crossdomain(origin='*')
def get_task(task_id):
    print task_id
    return jsonify({'hello': 'kitty'})


def process_command(_command, _time):
    data = _command
    if not data:
        print "received data:", data

    if len(data) != 1:
        print ("Invalid command")
        return "Invalid command"
    elif data == 'w':
        gopigo.fwd()
        return "Moving forward"
    elif data == 'x':
        gopigo.stop()
        return "Stopping"
    elif data == 's':
        gopigo.bwd()
        return "Moving back"
    elif data == 'a':
        gopigo.left()
        return "Turning left"
    elif data == 'd':
        gopigo.right()
        return "Turning right"
    elif data == 't':
        gopigo.increase_speed()
        return "Increase speed"
    elif data == 'g':
        gopigo.decrease_speed()
        return "Decrease speed"
    elif data == 'v':
        # print gopigo.volt(), 'V'
        return str(gopigo.volt())
    elif data == 'l':
        gopigo.led_on(0)
        gopigo.led_on(1)
        time.sleep(1)
        gopigo.led_off(0)
        gopigo.led_off(1)
        return "Flash LED"
    else:
        print ("Invalid command")
        return "Invalid command"  # run as a app

    if _time:
        time.sleep(_time)
    gopigo.stop()


if __name__ == '__main__':
    app.run(host='10.154.176.25', debug=True)