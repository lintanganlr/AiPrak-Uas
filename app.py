from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Data gejala dan hubungan data seperti sebelumnya
gejala_data = {
    "G01": "Kesulitan Bernafas (Sesak Nafas)",
    "G02": "Sering Batuk (Kering, Berdahak)",
    "G03": "Suara Nafas (Mengi, Bengi)",
    "G04": "Dada Terasa Sesak (Dada Sakit)",
    "G05": "Lesu dan Lelah",
    "G06": "Susah Tidur (Karena sering batuk)",
    "G07": "Mengalami masalah pernafasan (Aktivitas Fisik)",
    "G08": "Penurunan Fungsi Paru-Paru sebagai jalan masuk oksigen",
    "G09": "Lebih Sensitif terhadap Alergi",
    "G10": "Memburuk di malam hari",
    "G11": "Infeksi Pernapasan (pemicu iritasi)",
    "G12": "Panas"
}

penyakit_data = {
    "P01": "Asma Alergi",
    "P02": "Asma Non Alergi",
    "P03": "Asma Nokturnal",
    "P04": "Asma pada Anak",
    "P05": "Asma pada Orang Dewasa",
    "P06": "Asma Batuk",
    "P07": "Asma Akibat Pekerjaan(Oksional)",
    "P08": "Asma Musiman",
    "P09": "Asma Campuran",
    "P10": "Asma Eksersais(OlahRaga)"
}

hubungan_data = {
    ("G01", "P01"): {"MB": 0.8, "MD": 0.2},
    ("G02", "P01"): {"MB": 0.7, "MD": 0.2},
    ("G02", "P02"): {"MB": 0.8, "MD": 0.3},
    ("G02", "P03"): {"MB": 0.9, "MD": 0.1},
    ("G02", "P04"): {"MB": 0.5, "MD": 0.2},
    ("G02", "P05"): {"MB": 0.6, "MD": 0.1},
    ("G02", "P06"): {"MB": 0.7, "MD": 0.3},
    ("G02", "P09"): {"MB": 1.0, "MD": 0.4},
    ("G03", "P09"): {"MB": 0.6, "MD": 0.1},
    ("G04", "P01"): {"MB": 0.5, "MD": 0.2},
    ("G04", "P02"): {"MB": 0.8, "MD": 0.3},
    ("G04", "P03"): {"MB": 0.4, "MD": 0.2},
    ("G04", "P05"): {"MB": 0.6, "MD": 0.4},
    ("G04", "P09"): {"MB": 0.5, "MD": 0.1},
    ("G05", "P01"): {"MB": 0.4, "MD": 0.2},
    ("G05", "P03"): {"MB": 0.6, "MD": 0.3},
    ("G05", "P05"): {"MB": 0.7, "MD": 0.4},
    ("G05", "P07"): {"MB": 0.7, "MD": 0.2},
    ("G05", "P08"): {"MB": 0.9, "MD": 0.1},
    ("G05", "P09"): {"MB": 0.8, "MD": 0.4},
    ("G05", "P10"): {"MB": 0.7, "MD": 0.2},
    ("G06", "P03"): {"MB": 0.8, "MD": 0.1},
    ("G06", "P04"): {"MB": 0.9, "MD": 0.3},
    ("G06", "P05"): {"MB": 0.9, "MD": 0.4},
    ("G06", "P09"): {"MB": 0.8, "MD": 0.2},
    ("G07", "P07"): {"MB": 0.7, "MD": 0.3},
    ("G08", "P10"): {"MB": 0.6, "MD": 0.4},
    ("G09", "P04"): {"MB": 0.5, "MD": 0.1},
    ("G09", "P05"): {"MB": 0.7, "MD": 0.2},
    ("G09", "P08"): {"MB": 0.8, "MD": 0.4},
    ("G09", "P09"): {"MB": 0.9, "MD": 0.3},
    ("G09", "P10"): {"MB": 1.0, "MD": 0.2},
    ("G10", "P09"): {"MB": 0.7, "MD": 0.1},
    ("G11", "P09"): {"MB": 0.9, "MD": 0.3},
    ("G12", "P04"): {"MB": 0.6, "MD": 0.1},
}

def combine_cf(cf1, cf2):
    if cf1 >= 0 and cf2 >= 0:
        return cf1 + cf2 * (1 - cf1)
    elif cf1 < 0 and cf2 < 0:
        return cf1 + cf2 * (1 + cf1)
    else:
        return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))

@app.route('/')
def index():
    try:
        bg_url = url_for('static', filename='img/gallery/hero-bg.png')
        depart_url = url_for('static', filename='img/gallery/bg-departments.png')
        eyecare_url = url_for('static', filename='img/gallery/bg-eye-care.png')
        aboutUs_url = url_for('static', filename='img/gallery/about-us.png')
        about_url = url_for('static', filename='img/gallery/about-bg.png')
        doctorsUs_url = url_for('static', filename='img/gallery/doctors-us.png')
        doctors_url = url_for('static', filename='img/gallery/doctors-bg.png')
        people_url = url_for('static', filename='img/gallery/people.png')
        people1_url = url_for('static', filename='img/gallery/people-bg-1.png')
        dotbg_url = url_for('static', filename='img/gallery/dot-bg.png')
        blog_url = url_for('static', filename='img/gallery/blog-post.png')
        ctabg_url = url_for('static', filename='img/gallery/cta-bg.png')
        return render_template('main.html', bg_url=bg_url, depart_url=depart_url, eyecare_url=eyecare_url, aboutUs_url=aboutUs_url, about_url=about_url,
                               doctorsUs_url=doctorsUs_url, doctors_url=doctors_url, people_url=people_url, people1_url=people1_url, dotbg_url=dotbg_url,
                               blog_url=blog_url, ctabg_url=ctabg_url, gejala_data=gejala_data)
    except Exception as e:
        return str(e)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    try:
        gejala_input = request.form.getlist('inputGejala')  # Mendapatkan semua gejala yang dipilih
        
        CF_dict = {}
        penyakit_terkait_dict = {}

        # Proses untuk menghitung CF berdasarkan hubungan data
        for (gejala, penyakit), nilai in hubungan_data.items():
            MB = nilai["MB"]
            MD = nilai["MD"]
            CF = MB - MD
            
            if gejala in gejala_input:
                if penyakit not in CF_dict:
                    CF_dict[penyakit] = CF
                else:
                    CF_dict[penyakit] = combine_cf(CF_dict[penyakit], CF)
            
            if penyakit not in penyakit_terkait_dict:
                penyakit_terkait_dict[penyakit] = []
            penyakit_terkait_dict[penyakit].append(gejala)

        # Mengurutkan CF_dict berdasarkan nilai CF secara menurun dan memilih 2 teratas
        sorted_CF_dict = dict(sorted(CF_dict.items(), key=lambda item: item[1], reverse=True)[:2])
        
        hasil_diagnosis = []
        for penyakit, CF in sorted_CF_dict.items():
            if CF > 0:
                hasil_diagnosis.append({
                    "penyakit": penyakit_data[penyakit],
                    "cf": f"{CF * 100:.2f}%",
                    "gejala": [gejala_data[g] for g in penyakit_terkait_dict[penyakit] if g in gejala_input]
                })

        if not hasil_diagnosis:
            hasil_diagnosis.append({
                "penyakit": "Tidak ada penyakit yang terdeteksi berdasarkan gejala yang Anda masukkan.",
                "cf": "",
                "gejala": []
            })
        
        return render_template('result.html', hasil_diagnosis=hasil_diagnosis, gejala_input=gejala_input, gejala_data=gejala_data)
    
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)