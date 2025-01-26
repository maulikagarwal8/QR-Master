from flask import Flask,render_template,request,redirect,url_for
import requests

app=Flask(__name__)
url_c="http://api.qrserver.com/v1/create-qr-code/"
url_r="http://api.qrserver.com/v1/read-qr-code/"


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate_url',methods=['GET','POST'])
def generate_url():
    usertext=request.form["inputtext"]
    params={
        'data':usertext
    }
    qrimg=requests.get(url=url_c,params=params)
    print(qrimg)
    if qrimg.status_code == 200:
        with open("sample.jpg", 'wb') as f:
            f.write(qrimg.content)
    return render_template('qrimg.html',img=f)
    # return render_template('qrimg.html',url=url_c,usertext=usertext)

@app.route('/upload_qr',methods=['GET','POST'])
def upload_qr():
    userfile=request.files["file"]
    if userfile.filename == '':
        return redirect(url_for('home'))
    params={
        'file':userfile
    }
    qrdata=requests.post(url=url_r,files=params)
    return render_template('readqr.html',data=qrdata.json()[0]["symbol"][0]["data"])
    
if __name__=="__main__":
    app.run(debug=True)
