from flask import Flask, render_template, url_for

app = Flask(__name__)

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
                               blog_url=blog_url, ctabg_url=ctabg_url)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
