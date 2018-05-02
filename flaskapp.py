from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import xkdc
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def init():
    return render_template('index.html')

@app.route('/getdata', methods = ["POST"])
def getdata():
    minWordLen = int(request.form['minWordLen'])
    maxWordLen = int(request.form['maxWordLen'])
    maxOverLen = int(request.form['maxOverLen'])
    if request.form.get('numSub'):
        numSub = True
    else:
        numSub = False
    obj = xkdc.XKDC(maxWordLen,minWordLen,maxOverLen,numSub)
    wordlist = obj.createPasswords()
    return render_template('xkdcpass.html', wlist=wordlist)


if __name__ == "__main__":
    app.run(debug=True)