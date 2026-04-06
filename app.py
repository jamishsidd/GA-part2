from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "Hey I'm printing from inside the runner!!"

if __name__ == '__main__':
  app.run(debug=True)
