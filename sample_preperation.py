import os
import openai
import config  # Import the config module to get the API key

# Set the OpenAI API key
openai.api_key = config.config["api_key"]

SAMPLE_COUNT = 10
SAMPLE_DIR = "samples"

def generate_sql_sample():
    """Generate a standard SQL query using GPT-4 model."""
    conversation = [
        {"role": "system", "content": "You are an SQL expert. Write a standard SQL query:"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation
    )
    return response.choices[0].message["content"].strip()

def convert_to_databricks_sql(standard_sql):
    """Convert standard SQL to Databricks SQL using GPT-4 model."""
    conversation = [
        {"role": "system", "content": "You are an SQL conversion expert. Convert the following standard SQL to Databricks SQL:"},
        {"role": "user", "content": standard_sql}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation
    )
    return response.choices[0].message["content"].strip()

def main():
    # Create the samples directory if it doesn't exist
    if not os.path.exists(SAMPLE_DIR):
        os.makedirs(SAMPLE_DIR)

    for i in range(1, SAMPLE_COUNT + 1):
        # Generate SQL sample
        sql_query = generate_sql_sample()

        # Save the query to sampleX_input.sql
        input_filename = os.path.join(SAMPLE_DIR, f"sample{i}_input.sql")
        with open(input_filename, 'w') as file:
            file.write(sql_query)

        # Convert the SQL to Databricks SQL
        databricks_sql = convert_to_databricks_sql(sql_query)

        # Save the Databricks SQL to sampleX_output.sql
        output_filename = os.path.join(SAMPLE_DIR, f"sample{i}_output.sql")
        with open(output_filename, 'w') as file:
            file.write(databricks_sql)

        print(f"Generated sample{i}_input.sql and sample{i}_output.sql")

if __name__ == "__main__":
    main()
