-- Capstone 1 - Satria Dirgantara Nuryaman
-- SQL Script untuk membuat database dan table

-- Membuat database
CREATE DATABASE IF NOT EXISTS gudang_stok;

-- Menggunakan database
USE gudang_stok;

-- Membuat table Products
CREATE TABLE IF NOT EXISTS Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kode VARCHAR(10) UNIQUE NOT NULL,
    nama VARCHAR(25) NOT NULL,
    jumlah INT NOT NULL
);

-- Tampilkan struktur table
DESCRIBE Products;

-- Tampilkan data
SELECT * FROM Products;
