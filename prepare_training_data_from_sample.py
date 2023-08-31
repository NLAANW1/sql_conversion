import os
import json

SAMPLE_DIR = "samples"
JSONL_FILENAME = "training_data.jsonl"

def prepare_data():
    # List all files in the sample directory
    files = os.listdir(SAMPLE_DIR)
    input_files = [f for f in files if "input" in f]
    output_files = [f for f in files if "output" in f]

    with open(JSONL_FILENAME, 'w') as jsonl_file:
        for input_file, output_file in zip(sorted(input_files), sorted(output_files)):
            with open(os.path.join(SAMPLE_DIR, input_file), 'r') as infile, open(os.path.join(SAMPLE_DIR, output_file), 'r') as outfile:
                source = infile.read().strip()
                target = outfile.read().strip()
                
                # Create a JSON object and write it to the .jsonl file
                data = {"source": source, "target": target}
                jsonl_file.write(json.dumps(data) + '\n')

    print(f"Data prepared and saved to {JSONL_FILENAME}")

prepare_data()
