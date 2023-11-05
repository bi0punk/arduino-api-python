from flask import Flask, request, render_template
from flask import jsonify

app = Flask(__name__)

sensor_data = []  # Lista para almacenar los datos recibidos

@app.route('/api', methods=['POST'])
def receive_sensor_data():
    data = request.get_json()
    temperature = data.get('temperature')
    humidity = data.get('humidity')

    # Almacena los datos en la lista sensor_data
    sensor_data.append({"temperature": temperature, "humidity": humidity})

    return jsonify({"message": "Datos recibidos con éxito"})

@app.route('/data', methods=['GET'])
def get_sensor_data():
    return jsonify(sensor_data)

@app.route('/view', methods=['GET'])
def view_sensor_data():
    return render_template('data.html', sensor_data=sensor_data)

if __name__ == '__main__':
    app.run(host='192.168.33.237', port=5000)
