# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)
model = whisper.load_model("base")

@app.route('/', methods=['GET'])
def default():
    return "Status: OK"

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # Verifica se o arquivo foi enviado
    if 'audio' not in request.files:
        return jsonify({"error": "Nenhum arquivo de áudio enviado"}), 400

    # Processa o arquivo de áudio
    audio_file = request.files['audio']
    if audio_file:
        # Salva o arquivo temporariamente
        file_path = os.path.join("temp_audio", audio_file.filename)
        os.makedirs("temp_audio", exist_ok=True)
        audio_file.save(file_path)

        # Realiza a transcrição
        response = model.transcribe(file_path)

        # Remove o arquivo temporário
        os.remove(file_path)

        # Retorna a transcrição como resposta JSON
        return jsonify({"transcription": response['text']})

    return jsonify({"error": "Erro ao processar o arquivo"}), 500

if __name__ == '__main__':
    app.run(debug=True)
