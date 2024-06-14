import soundfile as sf

def calculate_derivative(derivative, sr, output_path):
    sf.write(output_path, derivative, sr)
