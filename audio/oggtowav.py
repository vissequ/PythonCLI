import os
import soundfile as sf

def convert_ogg_to_wav(input_path, output_path):
    """Converts ogg file to wav using soundfile."""
    try:
        # Read the ogg file
        data, samplerate = sf.read(input_path)
        # Write the data to a wav file
        sf.write(output_path, data, samplerate)
        print(f"Conversion completed: {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def find_and_convert_ogg_to_wav(root_folder):
    """Searches for ogg files in the root folder and converts them to wav."""
    for filename in os.listdir(root_folder):
        if filename.endswith('.ogg'):
            input_path = os.path.join(root_folder, filename)
            output_path = os.path.join(root_folder, filename.replace('.ogg', '.wav'))
            
            print(f"Converting {filename} to wav...")
            convert_ogg_to_wav(input_path, output_path)

if __name__ == "__main__":
    root_folder = os.getcwd()  # Use current working directory as root
    find_and_convert_ogg_to_wav(root_folder)
