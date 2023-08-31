import os
import openai
import config  # Import the config module to get the API key

# Set the OpenAI API key
openai.api_key = config.config["api_key"]

def convert_to_databricks_sql(standard_sql):
    """Convert standard SQL to Databricks SQL using GPT-4.0 model."""
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Convert the following SQL to Databricks SQL:\n{standard_sql}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Replace with the actual model name for GPT-4.0
        messages=conversation
    )
    return response.choices[0].message["content"].strip()

def process_sql_files(input_folder, output_folder):
    """Process all SQL files in the input folder and save converted SQL to the output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_directory, input_folder)

    for filename in os.listdir(input_path):
        if filename.endswith(".sql"):
            with open(os.path.join(input_path, filename), 'r') as file:
                standard_sql = file.read()
                
                try:
                    databricks_sql = convert_to_databricks_sql(standard_sql)
                    
                    # Save the converted SQL to a new file in the output folder
                    # Adding "_converted" to the filename for easy identification
                    output_filename = f"{filename.split('.')[0]}_converted.sql"
                    output_path = os.path.join(script_directory, output_folder, output_filename)
                    
                    # If the output file exists, replace it with the new content
                    if os.path.exists(output_path):
                        os.remove(output_path)
                    
                    with open(output_path, 'w') as output_file:
                        output_file.write(databricks_sql)
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    INPUT_FOLDER = "input"
    OUTPUT_FOLDER = "output"
    process_sql_files(INPUT_FOLDER, OUTPUT_FOLDER)
