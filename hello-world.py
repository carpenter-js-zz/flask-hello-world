from flask import Flask
from os import environ # for access to cloud9 env variables, which I'm not using...

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
  return "Hello World"

# @app.route("/hello/<name>")
# def hi_person(name):
#     return "Hello {}!".format(name.title())

@app.route("/hello/<name>")
def hi_person(name):
  html = """
    <h1>
        Hello {}!
    </h1>
    <p>
        Here's a picture of a kitten.  Awww...
     </p>
    <img src="http://placekitten.com/g/200/300">
  """
  return html.format(name.title())

# --- to tell app to listen to cloud9 --- 
# if __name__ == "__main__":
#   app.run(host=environ['IP'],
#   port=int(environ['PORT']))