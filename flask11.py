from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello1/<int:score>')
def hello_name(score):
   print("Score ",score)
   return render_template('hello1.html', marks = score)



if __name__ == '__main__':
   app.run(host='192.168.1.114', port=8001)

