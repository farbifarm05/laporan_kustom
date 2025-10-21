Modul ini adalah add-on untuk Odoo yang menambahkan opsi cetak faktur baru, yang dirancang khusus untuk dicetak pada printer **Dot Matrix** dengan ukuran kertas **Half Letter (8.5 x 5.5 inch)**.

## Fitur Utama

* **Template Khusus Dot Matrix**: Menambahkan template QWeb baru yang menggunakan font `monospace` (Courier) untuk memastikan semua kolom dan angka lurus (rata kanan) saat dicetak di printer dot matrix.
* **Opsi Print Baru**: Menambahkan item "Faktur Dot Matrix" di bawah menu "Print" pada Customer Invoices.
* **Format Kertas Kustom**: Menciptakan `paperformat` baru "Half Letter Dot Matrix" (216mm x 140mm) dengan orientasi **Landscape**.
* **Layout Sesuai Referensi**: Tata letak informasi (kop surat, detail bank, tanda tangan) disesuaikan dengan referensi visual yang spesifik, termasuk:
    * Info bank (PERHATIAN) di sisi kiri bawah.
    * Area tanda tangan "Penerima" (kiri) dan "Hormat kami" (kanan).

---

## Instalasi

1.  Salin atau kloning folder `laporan_kustom` ini ke dalam direktori `addons` pada instalasi Odoo Anda.
2.  Restart service Odoo Anda.
3.  Aktifkan **Mode Developer** di Odoo (Settings > Activate the developer mode).
4.  Pergi ke menu **Apps** > **Update Apps List** (Klik "Update").
5.  Cari modul `laporan_kustom` atau "Laporan Kustom Invoice" dan klik **Install**.

---

## ⚠️ Konfigurasi Server (WAJIB DILAKUKAN)

Modul ini **TIDAK AKAN BERFUNGSI DENGAN BENAR** tanpa konfigurasi server yang tepat. Laporan akan tampak salah (misalnya, menjadi Portrait atau layout berantakan) jika langkah-langkah ini tidak diikuti.

### 1. Instalasi `wkhtmltopdf` yang Benar

Masalah orientasi `Landscape` yang diabaikan disebabkan oleh bug pada versi `wkhtmltopdf` standar. Anda harus menggunakan versi `0.12.6 (with patched qt)`.

1.  Pastikan Anda telah menginstal versi yang benar di server Anda. Cek dengan perintah:
    ```bash
    wkhtmltopdf --version
    ```
2.  Hasilnya **harus** menunjukkan `wkhtmltopdf 0.12.6 (with patched qt)`.
3.  Jika tidak, unduh dan instal versi yang benar dari [halaman download resmi wkhtmltopdf](https://wkhtmltopdf.org/downloads.html). **Jangan** gunakan `apt-get install wkhtmltopdf` biasa.

### 2. Arahkan Odoo ke `wkhtmltopdf` yang Benar

Setelah versi yang benar terinstal (biasanya di `/usr/local/bin/`), Anda harus memberitahu Odoo di mana menemukannya.

1.  Temukan file konfigurasi Odoo Anda (biasanya di `/etc/odoo/odoo.conf`).
2.  Tambahkan atau edit baris `bin_path` untuk menunjuk ke lokasi instalasi baru:
    ```ini
    bin_path = /usr/local/bin
    ```
3.  **Restart service Odoo Anda** agar perubahan ini dibaca.

### 3. Konfigurasi Database Odoo (System Parameters)

`wkhtmltopdf` perlu mengambil file CSS Odoo untuk menata layout. Ini membutuhkan URL yang valid.

1.  Di Odoo, aktifkan **Mode Developer**.
2.  Pergi ke **Settings > Technical > System Parameters**.
3.  Cari parameter dengan Key `web.base.url`.
4.  Pastikan nilainya adalah alamat IP publik atau domain server Odoo Anda yang valid (misalnya, `http://erp.domainanda.com:8069`), **bukan** `http://localhost:8069`.
5.  (Sangat disarankan) Buat parameter baru:
    * Key: `web.base.url.freeze`
    * Value: `True`

---

## Cara Penggunaan

1.  Buka Customer Invoice yang sudah di-Validate (Posted).
2.  Klik tombol **Print** di bagian atas.
3.  Pilih opsi **Faktur Dot Matrix**.
4.  PDF akan dihasilkan dalam format Half Letter Landscape, siap dikirim ke printer dot matrix Anda.

---

## Penulis

Fakhrul R
