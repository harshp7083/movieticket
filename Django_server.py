from flask import Flask, send_file

app = Flask(__name__)

@app.route('/data/<path:path>')
def get_image(path):
    image_path = 'data/{}'.format(path)

    return send_file(image_path, mimetype='image/gif')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7501)
