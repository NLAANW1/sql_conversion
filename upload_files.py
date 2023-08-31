import os
import json
import requests
import config  # Import the config module to get the API key
import tempfile
import time

# Set the OpenAI API key
API_KEY = config.config["api_key"]
SAMPLES_DIR = "samples"

def prepare_data():
    data = {"messages": []}
    for filename in os.listdir(SAMPLES_DIR):
        if filename.endswith("_input.sql"):
            with open(os.path.join(SAMPLES_DIR, filename), 'r') as f:
                user_content = f.read()
            with open(os.path.join(SAMPLES_DIR, filename.replace("_input", "_output")), 'r') as f:
                assistant_content = f.read()
            data["messages"].append({"role": "user", "content": user_content})
            data["messages"].append({"role": "assistant", "content": assistant_content})
    return data

def upload_file(data):
    # Save the data to a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as tmp:
        json.dump(data, tmp)
        tmp_path = tmp.name

    # Upload the file
    with open(tmp_path, 'rb') as f:
        response = requests.post(
            "https://api.openai.com/v1/files",
            headers={"Authorization": f"Bearer {API_KEY}"},
            files={"file": f},
            data={"purpose": "fine-tune"}
        )
    
    # Delete the temporary file
    os.remove(tmp_path)
    
    if response.status_code != 200:
        print("Upload Error Response:", response.content)  # Print the error response for debugging
        raise Exception("Failed to upload the file.")
    
    return response.json().get("id")

def check_file_status(file_id, max_retries=20, delay=60):
    """
    Poll the status of the file until it's ready or max_retries is reached.
    """
    for _ in range(max_retries):
        response = requests.get(
            f"https://api.openai.com/v1/files/{file_id}",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        file_status = response.json().get("status")
        print(f"File status on retry {_ + 1}: {file_status}")  # Log the file status
        if file_status == "uploaded":
            return True
        print(f"Waiting for file {file_id} to be ready. Retry {_ + 1}/{max_retries}...")
        time.sleep(delay)
    return False



def create_fine_tuning_job(file_id):
    data = {
        "training_file": file_id,
        "model": "gpt-3.5-turbo-0613"
    }
    response = requests.post(
        "https://api.openai.com/v1/fine_tuning/jobs",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json=data
    )
    
    if response.status_code != 200:
        print("Fine-tuning Job Error Response:", response.content)  # Print the error response for debugging
        raise Exception("Failed to create the fine-tuning job.")
    
    return response.json()


def main():
    data = prepare_data()
    print(f"Total messages prepared: {len(data['messages'])}")  # Print the total number of messages
    file_id = upload_file(data)
    print("File ID:", file_id)
    
    # Add a delay after uploading the file
    print("Waiting for 4 minutes to give OpenAI servers time to process the file...")
    time.sleep(240)

if __name__ == "__main__":
    main()
