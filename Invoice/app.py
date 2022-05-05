from webbrowser import BackgroundBrowser
from flask import Flask,render_template,request,url_for
from werkzeug.utils import secure_filename
import send_email_invoicea
import os

ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
path = app.config["UPLOAD_FOLDER"] = "static/upload/"

@app.route('/')
def home():
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET','POST'])
def upload():
    result_upload = ''
    if request.method == 'POST':
        mail = request.form['email']
        name = request.form['name']
        tel = request.form['tel']
        description = request.form['description']
        f = request.files['file']
        path_file = path + secure_filename(f.filename)
        if f and allowed_file(f.filename):
            f.save(path_file)
            result_upload = 'Success'
            body = 'ส่งโดยคุณ '+ name\
                   +'<br> Email: '+mail + '</br>'\
                   +'<br> เบอร์โทรติดต่อ: '+ tel + '</br>'\
                   +'<br> รายละเอียดเพิ่มเติม: '+ description
            
            send_email_invoicea.sendEmail(body,path_file)
            os.remove(path_file)
            result_upload =  "Success"
            color_result = '10, 202, 94'
        else:
            result_upload = "File should be PDF"
            color_result = '255, 0, 46'
    return render_template('index.html',result_upload=result_upload,color_result=color_result)

if __name__ == "__main__":
    app.run(debug=False)