import mysql.connector

# Buat koneksi
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Bagas150902',
    database='gudang_stok'
)

print('\nDatabase Terkoneksi ke MySQL!')
cursor = db.cursor()

# Fungsi untuk membuat table 
# def create_table():
#     cursor.execute('''
#                CREATE TABLE IF NOT EXISTS Products(
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 kode VARCHAR (10) UNIQUE NOT NULL,
#                 nama VARCHAR (25) NOT NULL,
#                 jumlah INT NOT NULL
#                )
#                ''')
#     db.commit()
#     print('Tabel Products siap digunakan!')

# # Menjalankan fungsi create_table
# if __name__ == "__main__":
#     create_table()