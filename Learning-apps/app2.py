from flask import Flask, request
app = Flask(__name__)
@app.route('/',methods=['GET', 'PUT', 'POST']) #GET,PUT,POST,DELETE
def heloworld():
      num1 = int(request.args.get('num1'))
      num2 = int(request.args.get('num2'))
      num3 = int(request.args.get('num3'))
      return str(num1+num2_num3)
@app.route('/pricing')
def pricing():
    return "10000"
@app.route('/contactus')
def contactus():
    return "contactus"
if __name__ == "__main__":
      app.run()