import os
from pydub import AudioSegment

# Updated paths for the Codespaces Linux file system environment
source_dir = "./input_files"
output_dir = "./fixed_music"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Track progress count
count = 0

for filename in os.listdir(source_dir):
    if filename.lower().endswith(".mp3"):
        file_path = os.path.join(source_dir, filename)
        print(f"Converting: {filename}")
        
        try:
            # Load the audio file
            audio = AudioSegment.from_mp3(file_path)
            
            # Force the sample rate down to 44100 Hz for the HMD phone
            audio = audio.set_frame_rate(44100)
            
            # Export with standard CBR 192k 
            output_path = os.path.join(output_dir, filename)
            audio.export(output_path, format="mp3", bitrate="192k")
            count += 1
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(f"\nSuccess! {count} files successfully converted and saved in './fixed_music'!")