import requests
import config  # Import the config module to get the API key
import time

# Set the OpenAI API key
API_KEY = config.config["api_key"]

def check_file_status(file_id, max_retries=2, delay=5):
    for _ in range(max_retries):
        response = requests.get(
            f"https://api.openai.com/v1/files/{file_id}",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        file_status = response.json().get("status")
        print(f"File status on retry {_ + 1}: {file_status}")
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
        print("Fine-tuning Job Error Response:", response.content)
        raise Exception("Failed to create the fine-tuning job.")
    
    
    return response.json()

def main():
    file_id = input("file-rKlX84WCO6CdU7GjU7n1tU9u")
    
    # Check file status
    if not check_file_status(file_id):
        print("File is not ready after multiple retries. Exiting.")
        return

    job_response = create_fine_tuning_job(file_id)
    fine_tuned_model_id = job_response["model"]  # Retrieve the fine-tuned model ID
    print(f"Fine-tuned model ID: {fine_tuned_model_id}")

if __name__ == "__main__":
    main()
