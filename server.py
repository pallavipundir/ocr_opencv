#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os , datetime , logging
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

from libs.ocr import ocr_main

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'storage/files/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set([ 'png', 'jpg', 'jpeg' ])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@app.route('/images', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):

        timez = datetime.datetime.now()
        itsnow = timez.strftime('%I.%M.%S.%p_%d.%b.%Y')

        # Make the filename safe, remove unsupported chars
        filename = itsnow+'_'+secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        #return redirect(url_for('uploaded_file',
        #                        filename=filename))

        files = app.config['UPLOAD_FOLDER']+'/'+filename
        text = ocr_main(files,"thresh").encode('utf-8')

        imgo = {
            'src': 'images/'+filename,
            'text': text,
            'type': 'Image'
        }

        return render_template('index.html',img=imgo)
# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload

@app.route('/images/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

# Logging Debugs & Info to LogFile #
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
