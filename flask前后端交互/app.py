from flask import Flask, request, render_template, redirect
import Calculate as C

app = Flask(__name__)

result = []
inputData = []


@app.route('/', methods=['get', 'post'])
def index():
    if request.method == "POST":
        data = request.form.get('input')
        inputData.append(data)
        res = C.loadData(data)
        result.append(res)
        return redirect('/res')
    return render_template("index.html")


@app.route('/res', methods=['get', 'post'])
def admin():
    return render_template("indexResult.html", result=result, inputData=inputData,i=len(result)-1)


if __name__ == '__main__':
    app.run()
