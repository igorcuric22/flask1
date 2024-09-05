from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
   print("hello")
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   print("hello python")
   return 'Hello Python'

if __name__ == '__main__':
   app.run()