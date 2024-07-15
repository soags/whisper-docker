import os
import whisper
import sys

AUDIO_EXTENSIONS = ['.mp3', '.wav', '.m4a', '.flac', '.ogg']

def transcribe_audio(file_path):
    model = whisper.load_model("medium")
    result = model.transcribe(file_path, fp16=False)
    return result["text"]

if __name__ == "__main__":
    input_dir = "/app/audio"
    output_dir = "/app/text"

    if not os.path.exists(input_dir):
        print(f"Error: Directory {input_dir} does not exist.")
        sys.exit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    print(f"Searching for audio files in: {input_dir}")
    print(f"Files in directory: {os.listdir(input_dir)}")
    
    files_processed = 0
    for filename in os.listdir(input_dir):
        
        print(f"Checking file: {filename}")
        input_file = os.path.join(input_dir, filename)
        file_extension = os.path.splitext(filename)[1].lower()

        if os.path.isfile(input_file) and file_extension in AUDIO_EXTENSIONS:
            output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".txt")

            try:
                print(f"Start transcribe: {input_file}")
                transcription = transcribe_audio(input_file)

                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(transcription)
            
                print(f"Transcription saved to {output_file}")
                files_processed += 1
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
        else:
            print(f"Skipping {filename}: Not a supported audio file.")

    print(f"Processed {files_processed} files.")