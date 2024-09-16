import whisper
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

Tk().withdraw()
filename = askopenfilename(
    title='Selecione o arquivo de áudio',
    filetypes=[('Arquivos de áudio', '*.mp3 *.wav *.m4a *.aac *.ogg *.flac')]
)

model = whisper.load_model("base")
response = model.transcribe(filename)

save_path = asksaveasfilename(
    title='Salvar arquivo de transcrição',
    filetypes=[('Arquivos de texto', '*.txt')],
    defaultextension='.txt'
)

with open(save_path, 'w') as file:
    file.write(response['text'])