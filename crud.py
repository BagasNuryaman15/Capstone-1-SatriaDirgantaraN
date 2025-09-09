from database import db, cursor
import mysql.connector

class Product:
    def __init__(self, id, kode, nama, jumlah):
        self.id = id
        self.kode = kode
        self.nama = nama
        self.jumlah = jumlah

def list_products():
    """
    Fungsi untuk Menampilkan semua produk dalam bentuk list object
    """
    
    cursor.execute("SELECT * FROM Products")
    results = cursor.fetchall()
    products = []
    for row in results:
        product = Product(row[0], row[1], row[2], row[3])
        products.append(product)
    return products

def add_product(kode, nama, jumlah):
    """
    Fungsi untuk Menambah produk baru atau menambah stok jika sudah ada
    """

    try:
        # Mengecek apakah produk sudah ada
        cursor.execute("SELECT * FROM Products WHERE kode = %s", (kode,))
        existing_product = cursor.fetchone()
        
        if existing_product:
            # Jika produk sudah ada, tambahkan stok
            stok_sekarang = existing_product[3]
            stok_baru = stok_sekarang + jumlah
            query = "UPDATE Products SET jumlah = %s WHERE kode = %s"
            cursor.execute(query, (stok_baru, kode))
            db.commit()
            print(f"Stok produk '{nama}' bertambah {jumlah}. Total stok: {stok_baru}")
        else:
            # Jika produk belum ada, buat yang baru
            query = "INSERT INTO Products (kode, nama, jumlah) VALUES (%s, %s, %s)"
            values = (kode, nama, jumlah)
            cursor.execute(query, values)
            db.commit()
            print(f"Produk '{nama}' dengan kode '{kode}' berhasil ditambahkan")
        return True
    except mysql.connector.IntegrityError:
        print(f"Error: Kode '{kode}' sudah ada dengan nama berbeda!")
        return False

def sub_product(kode):
    """
    Fungsi untuk mengurangi stok produk berdasarkan kode
    """

    cursor.execute("DELETE FROM Products WHERE kode = %s", (kode,))
    db.commit()
    if cursor.rowcount > 0:
        print(f"Produk dengan kode '{kode}' berhasil dihapus")
        return True
    else:
        print(f"Produk dengan kode '{kode}' tidak ditemukan")
        return False

def edit_product(kode, jumlah_baru):
    """
    Fungsi untuk mengupdate jumlah stok produk berdasarkan kode
    """

    query = "UPDATE Products SET jumlah = %s WHERE kode = %s"
    cursor.execute(query, (jumlah_baru, kode))
    db.commit()
    if cursor.rowcount > 0:
        print(f"Stok produk dengan kode '{kode}' berhasil diupdate menjadi {jumlah_baru}")
        return True
    else:
        print(f"Produk dengan kode '{kode}' tidak ditemukan")
        return False
    
def hapus_product(kode):
    """
    Fungsi untuk menghapus produk secara permanen berdasarkan kode
    """
    cursor.execute("DELETE FROM Products WHERE kode = %s", (kode,))
    db.commit()
    if cursor.rowcount > 0:
        print(f"Produk dengan kode '{kode}' berhasil dihapus permanen")
        return True
    else:
        print(f"Produk dengan kode '{kode}' tidak ditemukan")
        return False