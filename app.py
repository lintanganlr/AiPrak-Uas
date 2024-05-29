from flask import Flask, render_template, url_for

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, render_template

# app=Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# app.run(debug=True)