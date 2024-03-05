from flask import Flask, render_template, request, url_for

app = Flask(__name__)

info_rahasia = "Berikut adalah KTM Anda."
nilai = "Andreas Latumahina"
nilai2 = 4623210019  # Ganti dengan operasi atau nilai yang sesuai
jumlah_percobaan = 0
maksimum_percobaan = 3

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_input():
    global jumlah_percobaan

    try:
        input_nilai = request.form['nilai']
        nilai_input = input_nilai  # Tidak perlu konversi ke int
    except ValueError:
        return render_template('index.html', error="Masukkan Nama berupa huruf saja.")

    if nilai_input == nilai:
        input_dua = request.form['nilai_dua']

        # Memastikan input_dua hanya berupa angka
        if not input_dua.isdigit():
            return render_template('index.html', error="Masukkan NPM harus berupa angka saja.")

        nilai_dua = int(input_dua)

        if nilai_dua == nilai2:
            image_url = url_for('static', filename='images/result.jpg')  # Sesuaikan path
            return render_template('result.html', info=info_rahasia, image_url=image_url)
        else:
            return render_template('index.html', error='Yah, NPM salah nih. Cek lagi, ya.')
    else:
        # Menampilkan pesan kesalahan jika nama dan NPM tidak sesuai
        if request.form.get('nilai') or request.form.get('nilai_dua'):
            jumlah_percobaan += 1
            if jumlah_percobaan == maksimum_percobaan:
                return render_template('blocked.html')
            else:
                return render_template('index.html', error='Yah, nama atau NPM salah nih. Cek lagi, ya.')
        else:
            return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)