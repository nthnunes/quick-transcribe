import whisper
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import os

Tk().withdraw()

filenames = askopenfilenames(
    title='Selecione os arquivos de áudio',
    filetypes=[('Arquivos de áudio', '*.mp3 *.wav *.m4a *.aac *.ogg *.flac')]
)

model = whisper.load_model("base")

transcription_dir = 'transcriptions'
os.makedirs(transcription_dir, exist_ok=True)

for filename in filenames:
    response = model.transcribe(filename)
    
    base_name = os.path.basename(os.path.splitext(filename)[0] + '.txt')
    save_path = os.path.join(transcription_dir, base_name)
    with open(save_path, 'w') as file:
        file.write(response['text'])

print("\nTranscrição finalizada :)\n")