from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')

def hello():
    return "Hello, World! Updated Version: New feature added successfully!"

@app.route('/health')
def health():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", "appdb"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "password"),
            host=os.getenv("DB_HOST", "database")
        )
        conn.close()
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)