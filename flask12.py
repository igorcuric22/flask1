from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70,'eng':90}
   return render_template('result.html', result = dict)

if __name__ == '__main__':
    app.run(host='192.168.1.114',port=4567)