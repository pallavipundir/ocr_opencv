#!/usr/bin/env python
# -*- coding: UTF-8 -*- #

import os , datetime , logging
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from libs.main_code import ocr_default
# Initialize the Flask application
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'storage/files/'
app.config['ALLOWED_EXTENSIONS'] = set([ 'png', 'jpg', 'jpeg','PNG','JPG','JPEG' ])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
 #]]
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/images', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        timez = datetime.datetime.now()
        itsnow = timez.strftime('%I.%M.%S.%p_%d.%b.%Y')
        filename = itsnow+'_'+file.filename    # remove unsupported chars

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        files = app.config['UPLOAD_FOLDER']+'/'+filename
        #text = ocr_default(files,"thresh").encode('utf-8')
        text = ocr_default(files,"thresh")
        
        imgo = {
            'src': 'images/'+filename,
            'text': text,
            'type': 'Image'
        }
    return render_template('index.html',img=imgo)

@app.route('/images/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

timez = datetime.datetime.now()
logfile = timez.strftime('%d.%b.%Y')

logging.basicConfig(filename='logs/'+logfile+'.log', filemode='w', level=logging.DEBUG)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("50001"),
        debug=True,
        threaded=True
    )
