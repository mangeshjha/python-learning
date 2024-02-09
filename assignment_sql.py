import requests
import sqlite3

# Function to fetch data from the API
def fetch_api_data():
    url = 'https://api.example.com/data'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data from API")
        return None

# Function to insert data into the database
def insert_into_database(data):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS api_data 
                      (id INTEGER PRIMARY KEY, field1 TEXT, field2 TEXT)''')
    
    # Insert data into the table
    for item in data:
        cursor.execute("INSERT INTO api_data (field1, field2) VALUES (?, ?)",
                       (item['field1'], item['field2']))
    
    conn.commit()
    conn.close()

# Main function to orchestrate the process
def main():
    api_data = fetch_api_data()
    if api_data:
        insert_into_database(api_data)
        print("Data inserted into database successfully.")
    else:
        print("Failed to fetch data from API.")

if __name__ == "__main__":
    main()
