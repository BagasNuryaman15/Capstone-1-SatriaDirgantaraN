from crud import list_products, add_product, sub_product, edit_product, hapus_product

def show_menu():
    try:
        products = list_products()
        print('=' * 60)
        print(' 📦 DAFTAR BARANG DI GUDANG 📦 '.center(60))
        print('=' * 60)
        
        if not products:
            print('Gudang masih kosong, belum ada barang.'.center(60))
        else:
            print(f"{'Kode':<15} {'Nama':<30} {'Jumlah':<15}")
            print('-' * 60)
            for p in products:
                print(f"{p.kode:<15} {p.nama:<30} {p.jumlah:<15}")
        
        print('=' * 60)
        print()
    except Exception as e:
        print(f'Error saat menampilkan daftar barang: {e}')

def validate_nama(nama):
    """
    Fungsi untuk memvalidasi nama agar tidak ada angka
    """

    if any(char.isdigit() for char in nama):
        return False
    return True

def validate_kode(kode):
    """
    Fungsi untuk memvalidasi Kode Barang harus diisi dan tidak boleh kosong
    """

    if not kode or not kode.replace(" ", ""):
        return False
    return True

def display_menu():
    while True:
        try:
            print('=' * 60)
            print(' 🛒 SISTEM MANAJEMEN GUDANG STOK 🛒 '.center(60))
            print('=' * 60)
            print('1. Lihat Daftar Barang')
            print('2. Tambahkan Barang')
            print('3. Keluarkan Barang')
            print('4. Hapus Barang')
            print('5. Keluar')
            print('=' * 60)
            
            menu_selected = input('\nPilih menu (1-5): ').strip()
            
            if menu_selected == '1':
                show_menu()
                input('Tekan Enter untuk kembali ke menu utama ...')
                
            elif menu_selected == '2':
                try:
                    print('\n' + '=' * 60)
                    print(' ➕ TAMBAH BARANG KE GUDANG ➕ '.center(60))
                    print('=' * 60)
                    
                    show_menu()
                    
                    # Memvalidasi Kode Barang
                    while True:
                        kode = input('🏷️  Masukkan kode barang: ').strip().upper()
                        if validate_kode(kode):
                            break
                        else:
                            print('❌ Error: Kode barang tidak boleh kosong!\n')
                    
                    # Memvalidasi Nama Barang
                    while True:
                        nama = input('📝 Masukkan nama barang: ').strip().title()
                        if not nama:
                            print('❌ Error: Nama barang tidak boleh kosong!\n')
                        elif not validate_nama(nama):
                            print('❌ Error: Nama barang tidak boleh mengandung angka!\n')
                        else:
                            break
                    
                    # Memvalidasi Jumlah Barang
                    while True:
                        try:
                            jumlah_input = input('🔢 Masukkan jumlah barang: ').strip()
                            jumlah = int(jumlah_input)
                            if jumlah <= 0:
                                print('❌ Error: Jumlah barang harus lebih dari 0!\n')
                            else:
                                break
                        except ValueError:
                            print('❌ Error: Jumlah barang harus berupa angka!\n')
                    
                    print('\n' + '-' * 60)
                    print('🔄 Memproses penambahan barang')
                    
                    # Tambah produk
                    if add_product(kode, nama, jumlah):
                        print('\n✅ BERHASIL!')
                        print(f'   Barang "{nama}" (Kode: {kode}) telah ditambahkan!')
                        print(f'   Jumlah: {jumlah} unit')
                    else:
                        print('\n❌ GAGAL!')
                        print('   Barang tidak dapat ditambahkan!')
                    
                    print('-' * 60)
                    input("\nTekan Enter untuk kembali ke menu utama ...")
                        
                except KeyboardInterrupt:
                    print('\n\n⚠️  Operasi dibatalkan oleh user!')
                    print('-' * 60)
                    input('Tekan Enter untuk kembali ke menu utama ...')
                except Exception as e:
                    print(f'\n❌ Error saat menambah barang: {e}')
                    print('-' * 60)
                    input('Tekan Enter untuk kembali ke menu utama ...')

            elif menu_selected == '3':
                try:
                    print('\n' + '=' * 60)
                    print(' 📤 KELUARKAN BARANG DARI GUDANG 📤 '.center(60))
                    print('=' * 60)
                    
                    show_menu()
                    products = list_products()
                    
                    if not products:
                        print('❌ Tidak ada barang di gudang!')
                        print('-' * 60)
                        input('Tekan Enter untuk kembali ke menu utama ...')
                        continue
                    
                    # Validasi kode barang
                    while True:
                        kode = input('🏷️  Masukkan kode barang yang akan dikeluarkan: ').strip().upper()
                        if validate_kode(kode):
                            break
                        else:
                            print('❌ Error: Kode barang tidak boleh kosong!\n')
                    
                    # Cari produk
                    product = next((p for p in products if p.kode == kode), None)
                    if not product:
                        print(f'\n❌ Barang dengan kode "{kode}" tidak ditemukan!')
                        print('-' * 60)
                        input('Tekan Enter untuk kembali ke menu utama ...')
                        continue
                    
                    print(f'\n📦 Barang ditemukan: {product.nama}')
                    print(f'📊 Stok tersedia: {product.jumlah} unit')
                    
                    # Validasi jumlah yang akan dikeluarkan
                    while True:
                        try:
                            jumlah_input = input('\n🔢 Masukkan jumlah yang akan dikeluarkan: ').strip()
                            jumlah = int(jumlah_input)
                            if jumlah <= 0:
                                print('❌ Error: Jumlah yang dikeluarkan harus lebih dari 0!\n')
                            elif jumlah > product.jumlah:
                                print(f'❌ Error: Jumlah yang diminta ({jumlah}) melebihi stok tersedia ({product.jumlah})!\n')
                            else:
                                break
                        except ValueError:
                            print('❌ Error: Jumlah harus berupa angka!\n')
                    
                    print('\n' + '-' * 60)
                    print('🔄 Memproses pengeluaran barang')
                    
                    # Proses pengeluaran barang
                    if jumlah == product.jumlah:
                        if sub_product(kode):
                            print('\n✅ BERHASIL!')
                            print(f'   Seluruh stok barang "{product.nama}" telah dikeluarkan')
                            print('   Barang dihapus dari daftar gudang')
                        else:
                            print('\n❌ GAGAL!')
                            print('   Tidak dapat menghapus barang dari gudang')
                    else:
                        if edit_product(kode, product.jumlah - jumlah):
                            print('\n✅ BERHASIL!')
                            print(f'   {jumlah} unit "{product.nama}" telah dikeluarkan')
                            print(f'   Sisa stok: {product.jumlah - jumlah} unit')
                        else:
                            print('\n❌ GAGAL!')
                            print('   Tidak dapat mengurangi stok barang')
                    
                    print('-' * 60)
                    input('\nTekan Enter untuk kembali ke menu utama ...')
                            
                except KeyboardInterrupt:
                    print('\n\n⚠️  Operasi dibatalkan oleh user!')
                    print('-' * 60)
                    input('Tekan Enter untuk kembali ke menu utama ...')
                except Exception as e:
                    print(f'\n❌ Error saat mengeluarkan barang: {e}')
                    print('-' * 60)
                    input('Tekan Enter untuk kembali ke menu utama ...')

            elif menu_selected == '4':
                try:
                    print('\n' + '=' * 60)
                    print(' 🗑️ HAPUS BARANG DARI GUDANG 🗑️ '.center(60))
                    print('=' * 60)
                    
                    show_menu()
                    products = list_products()
                    
                    if not products:
                        print('❌ Tidak ada barang di gudang!')
                        print('-' * 60)
                        input('Tekan Enter untuk kembali ke menu utama ...')
                        continue
                    
                    # Validasi kode barang
                    while True:
                        kode = input('🏷️  Masukkan kode barang yang akan dihapus: ').strip().upper()
                        if validate_kode(kode):
                            break
                        else:
                            print('❌ Error: Kode barang tidak boleh kosong!\n')
                    
                    # Cari produk
                    product = next((p for p in products if p.kode == kode), None)
                    if not product:
                        print(f'\n❌ Barang dengan kode "{kode}" tidak ditemukan!')
                        print('-' * 60)
                        input('Tekan Enter untuk kembali ke menu utama ...')
                        continue
                    
                    print(f'\n📦 Barang yang akan dihapus:')
                    print(f'   🏷️  Kode: {product.kode}')
                    print(f'   📝 Nama: {product.nama}')
                    print(f'   📊 Stok: {product.jumlah} unit')
                    
                    # Konfirmasi penghapusan
                    while True:
                        konfirmasi = input('\n⚠️  Apakah Anda yakin ingin menghapus barang ini? (y/n): ').strip().lower()
                        if konfirmasi in ['y', 'yes', 'ya']:
                            break
                        elif konfirmasi in ['n', 'no', 'tidak']:
                            print('\n🚫 Penghapusan dibatalkan!')
                            print('-' * 60)
                            input('Tekan Enter untuk kembali ke menu utama ...')
                            continue
                        else:
                            print('❌ Input tidak valid! Masukkan "y" untuk ya atau "n" untuk tidak.')
                    
                    print('\n' + '-' * 60)
                    print('🔄 Memproses penghapusan barang')
                    
                    # Hapus produk
                    if hapus_product(kode):
                        print('\n✅ BERHASIL!')
                        print(f'   Barang "{product.nama}" (Kode: {kode}) telah dihapus!')
                        print('   Seluruh data barang telah dihapus dari sistem')
                    else:
                        print('\n❌ GAGAL!')
                        print('   Barang tidak dapat dihapus dari sistem')
                    
                    print('-' * 60)
                    input('\nTekan Enter untuk kembali ke menu utama ...')
                            
                except KeyboardInterrupt:
                    print('\n\n⚠️  Operasi dibatalkan oleh user!')
                    print('-' * 60)
                    input('Tekan Enter untuk kembali ke menu utama ...')
                except Exception as e:
                    print(f'\n❌ Error saat menghapus barang: {e}')
                    print('-' * 60)
                    input('Tekan Enter untuk kembali ke menu utama ...')

            elif menu_selected == '5':
                print('\n' + '=' * 60)
                print('👋 Terima kasih telah menggunakan Sistem Gudang Stok!')
                print('=' * 60)
                break
                
            else:
                print('\n❌ Menu tidak valid! Silakan pilih menu 1-5.')
                input('Tekan Enter untuk mencoba lagi')
        except KeyboardInterrupt:
            print('\n\n👋 Terima kasih telah menggunakan Sistem Gudang Stok!')
            break