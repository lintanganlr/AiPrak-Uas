from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    try:
        bg_url = url_for('static', filename='img/gallery/hero-bg.png')
        return render_template('main.html', bg_url=bg_url)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
