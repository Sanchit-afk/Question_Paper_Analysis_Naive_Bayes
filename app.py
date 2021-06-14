from flask import Flask,render_template
import detector
import detectorcoa
import os
from os.path import join, dirname, realpath
from flask import Flask, flash, request, redirect, url_for,send_from_directory,render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'D:\\PBL_DATA\\web_design\\web_design\\static\\uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg','txt'}
ALLOWED_EXTENSIONS_TEXT = {'txt'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@app.route('/')
def index():
    return render_template('index.html')



modDict , modules = detector.classify()
values = list(modDict.values())
names = [k for k in modules]
modNo = list(modDict.keys())

modDictt , modulescoa = detectorcoa.classify()
valuess = list(modDictt.values())
namess = [k for k in modulescoa]
moddNo = list(modDictt.keys())
@app.route('/aoaanalysis', methods=['GET', 'POST'])
def aoaanalysis():
    custom_values = []
    custom_names = []
    if request.method == 'POST':
        if request.form['submit'] == 'Upload Text':
            # check if the post request has the file part
            if 'text_only' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['text_only']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                custom_modDict , custom_modules = detector.custom_classify('static/uploads/'+filename)
                custom_values = list(custom_modDict.values())
                custom_names = [k for k in custom_modules]
        if request.form['submit'] == 'Upload Image':
            # check if the post request has the file part
            if 'image_only' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['image_only']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('uploaded_file',filename=filename))
    return render_template('aoa_analysis.html',names=names,values=values,custom_names=custom_names,custom_values=custom_values)


@app.route('/coaanalysis', methods=['GET', 'POST'])
def coaanalysis():
    custom_valuess = []
    custom_namess = []
    if request.method == 'POST':
        if request.form['submit'] == 'Upload Text':
            # check if the post request has the file part
            if 'text_only' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['text_only']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                custom_modDict , custom_modules = detectorcoa.custom_classify('static/uploads/'+filename)
                custom_valuess = list(custom_modDict.values())
                custom_namess = [k for k in custom_modules]
        # if request.form['submit'] == 'Upload Image':
        #     # check if the post request has the file part
        #     if 'image_only' not in request.files:
        #         flash('No file part')
        #         return redirect(request.url)
        #     file = request.files['image_only']
        #     # if user does not select file, browser also
        #     # submit an empty part without filename
        #     if file.filename == '':
        #         flash('No selected file')
        #         return redirect(request.url)
        #     if file and allowed_file(file.filename):
        #         filename = secure_filename(file.filename)
        #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #         return redirect(url_for('uploaded_file',filename=filename))
    return render_template('coa_analysis.html',namess=namess,valuess=valuess,custom_namess=custom_namess,custom_valuess=custom_valuess)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

app.run(debug=True)