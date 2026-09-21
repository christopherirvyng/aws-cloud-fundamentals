from flask import Flask
import pymysql

app = Flask(__name__)

# Konfigurasi Database RDS
DB_HOST = 'db-flask-app.czqswyb2w2yl.us-east-1.rds.amazonaws.com'
DB_USER = 'admin'
DB_PASSWORD = 'Success123!'
DB_NAME = 'mydb'

def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Simpan timestamp kunjungan baru ke RDS
    cursor.execute("INSERT INTO visitors () VALUES ()")
    conn.commit()
    
    # Hitung total kunjungan dari RDS
    cursor.execute("SELECT COUNT(*) AS total FROM visitors")
    result = cursor.fetchone()
    total_visits = result['total']
    
    cursor.close()
    conn.close()
    
    return f"<h1>Halo dari AWS EC2 + RDS MySQL!</h1><p>Aplikasi ini telah dikunjungi sebanyak <b>{total_visits}</b> kali dari database RDS.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
