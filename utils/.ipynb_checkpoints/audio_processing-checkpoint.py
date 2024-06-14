import librosa
import numpy as np

def process_audio(file_path):
    y, sr = librosa.load(file_path)
    # Compute the derivative of the waveform
    derivative = np.diff(y)
    return derivative, sr
