from flask import Blueprint, request, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename
from utils.audio_processing import process_audio
from utils.derivative import calculate_derivative

main = Blueprint('main', __name__)

@main.route('/')
def upload_file():
    return '''
    <!doctype html>
    <title>Upload a Song</title>
    <h1>Upload a Song File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@main.route('/', methods=['POST'])
def upload_file_post():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('app/static/uploaded_files', filename)
        file.save(file_path)
        
        derivative, sr = process_audio(file_path)
        output_path = os.path.join('app/static/uploaded_files', 'output_song.wav')
        calculate_derivative(derivative, sr, output_path)
        
        return send_from_directory('static/uploaded_files', 'output_song.wav')
