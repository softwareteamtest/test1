from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'POST':
        s = request.form.get('input')
        print(s)
        return s

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    s = index()

