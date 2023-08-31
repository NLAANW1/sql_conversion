import os
import openai
import json
import config  # Import the config module to get the API key

# Set the OpenAI API key
openai.api_key = config.config["api_key"]

def convert_to_databricks_sql(standard_sql):
    """Convert standard SQL to Databricks SQL using GPT-3.5-turbo model."""
    # You can implement the logic for SQL conversion here
    # This is a placeholder function
    databricks_sql = f"SELECT * FROM {standard_sql}"
    return databricks_sql

def process_sql_files(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".sql"):
            with open(os.path.join(input_folder, filename), "r") as file:
                sql_query = file.read().strip()

            # Step 1: send the conversation and available functions to GPT
            messages = [
                {"role": "user", "content": f"Convert the following SQL to Databricks SQL:"},
                {"role": "assistant", "content": f"Convert the following standard SQL to Databricks SQL:"},
                {"role": "user", "content": sql_query}
            ]
            functions = [
                {
                    "name": "convert_to_databricks_sql",
                    "description": "Convert standard SQL to Databricks SQL",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "sql_query": {
                                "type": "string",
                                "description": "The standard SQL query to convert",
                            }
                        },
                        "required": ["sql_query"],
                    },
                }
            ]
            response = openai.ChatCompletion.create(
                model="gpt-4.0",  # Replace with the actual model name for GPT-4.0
                messages=messages,
                functions=functions,
                function_call="auto",  # auto is default, but we'll be explicit
            )
            response_message = response["choices"][0]["message"]

            # Rest of the code remains the same

if __name__ == "__main__":
    INPUT_FOLDER = "input"   # Change this to the correct input folder path if needed
    OUTPUT_FOLDER = "output" # Change this to the correct output folder path if needed
    process_sql_files(INPUT_FOLDER, OUTPUT_FOLDER)
