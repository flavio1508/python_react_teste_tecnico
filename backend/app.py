from flask import Flask, request, jsonify, send_file, Response
from flask_cors import CORS
import os
import uuid

app = Flask(__name__)
CORS(app, expose_headers=["Content-Range", "Accept-Ranges"])

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def is_pdf(file):
    return file.filename.lower().endswith('.pdf')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Arquivo não enviado'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'Nome inválido'}), 400

    if not is_pdf(file):
        return jsonify({'error': 'Somente PDF permitido'}), 400

    filename = f"{uuid.uuid4()}.pdf"
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    return jsonify({
        'fileUrl': f'http://localhost:5000/pdf/{filename}'
    })


@app.route('/pdf/<filename>')
def stream_pdf(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(filepath):
        return jsonify({'error': 'Arquivo não encontrado'}), 404

    file_size = os.path.getsize(filepath)
    range_header = request.headers.get('Range', None)

    if range_header:
        byte1, byte2 = 0, None
        match = range_header.replace('bytes=', '').split('-')

        if match[0]:
            byte1 = int(match[0])
        if len(match) > 1 and match[1]:
            byte2 = int(match[1])

        length = file_size - byte1
        if byte2:
            length = byte2 - byte1 + 1

        with open(filepath, 'rb') as f:
            f.seek(byte1)
            data = f.read(length)

        resp = Response(data, 206, mimetype='application/pdf')
        resp.headers.add('Content-Range', f'bytes {byte1}-{byte1 + length - 1}/{file_size}')
        resp.headers.add('Accept-Ranges', 'bytes')
        resp.headers.add('Content-Length', str(length))

        return resp

    return send_file(filepath, mimetype='application/pdf')


if __name__ == '__main__':
    app.run(debug=True)