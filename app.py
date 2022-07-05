# FLASK tutorials:
# https://www.youtube.com/watch?v=jgAVGtkk03Q&list=PL0lO_mIqDDFXiIQYjLbncE9Lb6sx8elKA&index=2


from flask import Flask, render_template, url_for

app = Flask(__name__)


service_port = 7777


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def index_about():
    return render_template("about.html")


@app.route('/alive')
def index_alive():
    return f'<center><h1>Json2Json</h1><h2>Service is Alive!<br>Send requests to <b><i>&ltthis host&gt:{service_port}/convert</b></i><h2></center>'


if __name__ == "__main__":
    app.run(debug=True)
