from flask import Flask
app = Flask(__name__)
@app.route('/',methods=['GET', 'PUT', 'POST']) #GET,PUT,POST,DELETE
def heloworld():
      return "Hellow World!"
@app.route('/pricing')
def pricing():
    return "10000"
@app.route('/contactus')
def contactus():
    return "contactus"
if __name__ == "__main__":
      app.run()