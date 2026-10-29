## UI Automation Testing

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green?logo=playwright)
![Pytest](https://img.shields.io/badge/Pytest-Testing-blue?logo=pytest)
![Testing](https://img.shields.io/badge/Testing-UI-orange)
![Status](https://img.shields.io/badge/Project-QA%20Automation-purple)

## 📌 Deskripsi Proyek

- Repository ini berisi proyek Quality Assurance (QA) UI Automation Testing pada aplikasi OrangeHRM menggunakan Python, Playwright, Pytest, dan Allure Report.

- Proyek ini dibuat untuk mengotomatisasi pengujian fungsional aplikasi web, memvalidasi hasil pengujian, serta mendukung proses analisis kegagalan melalui dokumentasi hasil eksekusi dan rekaman video browser.

- Framework menggunakan pendekatan Page Object Model (POM) melalui folder Pages, fixture pengujian melalui conftest.py, dan konfigurasi dependency melalui requirements.txt.

- Repository juga menyediakan Jenkinsfile untuk mendukung konfigurasi pipeline CI/CD. https://github.com/fayakunilham/orangehrm-playwright-python-allure_report/tree/automation_playwright

## Tujuan Proyek
- Mengimplementasikan UI Automation Testing menggunakan Playwright dan Python.
- Mengotomatisasi pengujian fungsional aplikasi OrangeHRM.
- Menggunakan Pytest untuk menjalankan test case dan melakukan assertion.
- Menerapkan Page Object Model agar kode lebih terstruktur dan mudah dipelihara.
- Menggunakan fixture untuk mengelola browser dan halaman pengujian.
- Merekam video selama eksekusi pengujian untuk membantu proses debugging.
- Menghasilkan laporan pengujian menggunakan Allure Report.
- Mendukung integrasi automation testing melalui Jenkins.

## 🌐 Aplikasi yang Diuji
### OrangeHRM — UI Automation Testing

URL: https://opensource-demo.orangehrmlive.com/

OrangeHRM merupakan aplikasi Human Resource Management System (HRMS) yang menyediakan fitur pengelolaan sumber daya manusia.

Cakupan skenario pengujian meliputi:

- Login menggunakan kredensial yang valid.
- Validasi login menggunakan kredensial yang tidak valid.
- Validasi akses halaman setelah login.
- Pengujian fungsi administrasi pengguna.
  Pengujian pengelolaan data karyawan sesuai test case.
- Validasi navigasi dan interaksi elemen antarmuka.
Catatan: Skenario di atas merupakan gambaran cakupan pengujian. Pastikan setiap skenario sudah diimplementasikan dalam test script sebelum dianggap sebagai hasil pengujian aktual.

## 🛠️ Teknologi yang Digunakan
| Teknologi |	Fungsi |
|---|---|
| Python | Bahasa pemrograman untuk automation testing |
| Playwright | Otomatisasi browser dan interaksi UI |
| Pytest | Test runner dan assertion |
| Allure Report | Visualisasi hasil pengujian |
| Page Object Model (POM) | Mengorganisasi interaksi halaman |
| Jenkins | Mendukung otomasi pipeline CI/CD |
| python-dotenv | Membaca konfigurasi dan kredensial dari file .env |
| Git & GitHub | Version control dan penyimpanan source code |

## 📁 Struktur Proyek
```
orangehrm-playwright-python-allure_report/
│
├── Pages/                  # Page Object Model
│   └── login_page.py       # Interaksi halaman login
│
├── Utils/                  # Helper dan utility functions
├── assets/                 # Resource pendukung proyek
├── tests/                  # Test cases automation
├── videos/                 # Rekaman video browser saat testing
├── allure-results/         # Hasil mentah Allure, jika dibuat
├── allure-report/          # Laporan HTML Allure, jika dibuat
│
├── conftest.py             # Pytest fixtures dan konfigurasi browser
├── requirements.txt        # Dependency Python
├── Jenkinsfile             # Konfigurasi pipeline Jenkins
├── .env                    # Kredensial lokal, tidak di-commit
├── .gitignore              # File yang diabaikan Git
└── README.md               # Dokumentasi proyek
```

Catatan: Nama dan isi file di dalam setiap folder dapat berbeda mengikuti kondisi branch terbaru.

### Penjelasan Folder dan File
- Pages/ — Menyimpan class Page Object untuk memisahkan interaksi UI dari test case.
- Utils/ — Menyimpan fungsi pendukung yang dapat digunakan kembali.
- assets/ — Menyimpan resource pendukung proyek.
- tests/ — Menyimpan script pengujian otomatis.
- videos/ — Menyimpan rekaman video browser yang dibuat selama eksekusi test.
- conftest.py — Mengatur fixture browser, konfigurasi timeout, dan fixture login.
- requirements.txt — Berisi dependency yang diperlukan.
- Jenkinsfile — Mendefinisikan pipeline Jenkins.
- .env — Menyimpan konfigurasi lokal, termasuk kredensial aplikasi.
  
## ⚙️ Persiapan dan Instalasi
### 1. Prasyarat

Pastikan perangkat sudah memiliki:

- Python 3.x
- pip
- Git, jika menggunakan metode clone
- IDE seperti Visual Studio Code
- Allure Commandline dan Java runtime yang kompatibel jika ingin membuat laporan Allure

#### Periksa instalasi Python:

```
bash
python --version
python -m pip --version
```
### 2. Clone Repository
```
bash
git clone https://github.com/fayakunilham/orangehrm-playwright-python-allure_report.git
```

### 3. Checkout Branch Automation
```
bash
cd orangehrm-playwright-python-allure_report
git checkout automation_playwright
```
### 4. Download Repository dalam Format ZIP

Jika tidak ingin menggunakan Git:

- Buka repository branch automation_playwright.
- Klik tombol Code.
- Pilih Download ZIP.
- Ekstrak file ZIP.
- Buka terminal pada folder hasil ekstraksi.

### 5. Membuat Virtual Environment
```
bash
python -m venv .venv
```

#### Aktifkan virtual environment di Windows PowerShell:
```
powershell
.\.venv\Scripts\Activate.ps1
```

#### Untuk Windows Command Prompt:
```
cmd
.venv\Scripts\activate.bat
```

#### Untuk Linux atau macOS:
```
bash
source .venv/bin/activate
```
### 6. Instal Dependency
```
bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
### 7. Instal Browser Playwright
```
bash
python -m playwright install chromium
```
## 🔐 Konfigurasi Environment

Berdasarkan konfigurasi conftest.py, proyek membaca kredensial OrangeHRM dari file .env melalui python-dotenv. Variabel yang diperlukan adalah ORANGEHRM_USERNAME dan ORANGEHRM_PASSWORD. https://github.com/fayakunilham/orangehrm-playwright-python-allure_report/blob/automation_playwright/conftest.py

#### Buat file .env pada root proyek:
```
dotenv
ORANGEHRM_USERNAME=your_username
ORANGEHRM_PASSWORD=your_password
```

Ganti nilai tersebut dengan kredensial yang sesuai untuk lingkungan pengujian.

Penting: Jangan mengunggah file .env atau kredensial ke repository publik. Pastikan file tersebut masuk ke .gitignore.

## ▶️ Cara Menjalankan Pengujian
#### Menjalankan Semua Test Case
```
bash
python -m pytest tests/ -v
```

#### Menjalankan Test dengan Output Detail
```
bash
python -m pytest tests/ -v -s
```

#### Menjalankan Test dengan Allure Results
```
bash
python -m pytest tests/ -v --alluredir=allure-results
```
#### Menjalankan Test File Tertentu
```
bash
python -m pytest tests/nama_file_test.py -v
```


Ganti nama_file_test.py dengan nama file yang benar-benar tersedia di folder tests/.

#### Keterangan Perintah
- pytest — Menjalankan test case.
- -v — Menampilkan nama test dan statusnya.
- -s — Menampilkan output print() di terminal.
- --alluredir=allure-results — Menyimpan hasil pengujian untuk Allure Report.
## 🎥 Test Execution Video

Framework pada conftest.py menggunakan Playwright Chromium dengan mode browser terlihat (headless=False) dan mengaktifkan perekaman video pada browser context. Video disimpan ke folder videos/ untuk membantu proses investigasi ketika terjadi kegagalan test. https://github.com/fayakunilham/orangehrm-playwright-python-allure_report/blob/automation_playwright/conftest.py

#### Manfaat rekaman video:

- Melihat kembali alur eksekusi pengujian.
- Membantu mengidentifikasi penyebab kegagalan.
- Mempermudah proses debugging.
- Menyediakan dokumentasi visual proses automation testing.

## 📊 Allure Report

Allure Report digunakan untuk menyajikan hasil pengujian dalam bentuk laporan HTML yang interaktif.

### 1. Jalankan Test dan Simpan Hasil
```
bash
python -m pytest tests/ -v --alluredir=allure-results
```
### 2. Generate HTML Report
```
bash
allure generate allure-results --clean -o allure-report
```
### 3. Buka Report
```
bash
allure open allure-report
```

#### Alternatif untuk menjalankan test dan langsung membuka laporan:
```
bash
allure serve allure-results
```

#### Fitur Allure Report
- Test Summary: Ringkasan hasil pengujian.
- Test Status: Status Passed, Failed, Broken, dan Skipped.
- Test Details: Detail masing-masing test case.
- Execution Duration: Durasi eksekusi test.
- Failure Analysis: Membantu analisis kegagalan pengujian.
#### Catatan
- Pastikan plugin allure-pytest tersedia dalam dependency proyek.
- Allure Commandline perlu diinstal secara terpisah.
- Hasil test harus tersedia sebelum laporan dibuat.
- Folder allure-results/ berisi hasil mentah pengujian.
- Folder allure-report/ berisi laporan HTML yang dihasilkan.
## 🔄 Jenkins CI/CD

Repository menyediakan file Jenkinsfile sebagai dasar konfigurasi pipeline Jenkins.

Integrasi CI/CD dapat digunakan untuk membantu menjalankan automation testing secara terjadwal atau sebagai bagian dari pipeline build.

Sebelum menjalankan pipeline, pastikan:

- Jenkins sudah dikonfigurasi dengan environment Python yang sesuai.
- Dependency proyek dapat diinstal.
- Browser Playwright tersedia pada environment agent.
- Kredensial OrangeHRM disimpan secara aman melalui konfigurasi credentials Jenkins.
- Hasil pengujian dan laporan disimpan sebagai artifacts jika diperlukan.

Perilaku pipeline aktual mengikuti isi Jenkinsfile yang terdapat di repository.

## ✅ Validasi Pengujian

Automation testing digunakan untuk memvalidasi:

- Hasil aktual dibandingkan dengan hasil yang diharapkan.
- Respons aplikasi terhadap kredensial valid dan tidak valid.
- Interaksi elemen dan navigasi UI.
- Keberhasilan assertion pada setiap test case.
- Rekaman video untuk mendukung investigasi kegagalan.
- Hasil eksekusi melalui Pytest dan Allure Report.

Status dan jumlah test yang berhasil atau gagal bergantung pada hasil eksekusi aktual.

## 📚 Referensi
- GitHub Repository: https://github.com/fayakunilham/orangehrm-playwright-python-allure_report
- Automation Branch: https://github.com/fayakunilham/orangehrm-playwright-python-allure_report/tree/automation_playwright
- OrangeHRM Demo: https://opensource-demo.orangehrmlive.com/
- Playwright Python: https://playwright.dev/python/
- Pytest Documentation: https://docs.pytest.org/
- Allure Report: https://allurereport.org/docs/
- Jenkins Documentation: https://www.jenkins.io/doc/

## 👨‍💻 Tentang Saya

**Fayakun Ilham Pradana**

Software Quality Assurance | QA Automation Testing

- GitHub: https://github.com/fayakunilham
- LinkedIn: https://www.linkedin.com/in/fayakun-ilham-pradana/

---
GitHub: https://github.com/fayakunilham

Project ini dibuat untuk mempelajari dan mempraktikkan UI & API Automation Testing menggunakan Python, Playwright, Pytest, dan Allure Report. Pengujian UI berfokus pada validasi fungsionalitas dan interaksi antarmuka aplikasi web OrangeHRM, sedangkan pengujian API berfokus pada validasi endpoint, HTTP status code, response, dan fungsionalitas layanan API. Hasil pengujian dapat dianalisis melalui Pytest dan Allure Report.
