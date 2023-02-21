from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    users = [ 'Rosalia','Adrianna','Victoria' ]
    return render_template('index.html', title='Welcome', members=users)

# @app.route("/")
# def index():
#   return "<h1>Hello, Flask!</h1>"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
