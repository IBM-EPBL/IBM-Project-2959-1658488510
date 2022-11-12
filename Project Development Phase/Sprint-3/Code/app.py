from flask import * 
import os
import ibm_db
import bcrypt
from functools import partial,wraps
from flask_mail import Mail, Message
conn = ibm_db.connect("DATABASE=;HOSTNAME=;PORT=;SECURITY=;SSLServerCertificate=;PROTOCOL=;UID=;PWD=",'','')

#-----------FLASK MAIL IS USED IN login() Function-------------------
app = Flask(__name__) 
app.secret_key = ''
PEOPLE_FOLDER = os.path.join('static', 'people_photo')


mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'spdineshwaran4@gmail.com'
app.config['MAIL_PASSWORD'] = 'wowcfyoaajduxvha'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/") 
@app.route("/home")

def home():
    return render_template("home.html")


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    return redirect(url_for('home'))


@app.route("/register",methods=['GET','POST'])
#---------------SPRINT-1--------------------------


@app.route("/orgregister",methods=['GET','POST'])
#---------------SPRINT-1--------------------------


@app.route("/login",methods=['GET','POST'])
def login():
  if request.method == 'POST':
      if(request.form['logval']=="recruiter"):
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
          return render_template('login.html',error='Please fill all fields')
        query = "SELECT * FROM RECRUITER WHERE email=?"
        stmt = ibm_db.prepare(conn, query)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        dictionary = ibm_db.fetch_assoc(stmt)
        if not dictionary:
          return render_template('login.html',error='Invalid Credentials')
      
        isPasswordMatch = bcrypt.checkpw(password.encode('utf-8'),dictionary['PASSWORD'].encode('utf-8'))

        if not isPasswordMatch:
          return render_template('login.html',error='Invalid Credentials')
        session['loggedin'] = True
        session['id'] = dictionary['EMAIL']
        f=session['id']
        # Redirect to home page
        session['active']="jobseeker"
        msg = Message('New Login Found Just Now!!!', sender = 'spdineshwaran4@gmail.com', recipients = [session['id']])
        msg.body = "Hello User\nWe had came to know that you have logged in our jobby portal just now."
        mail.send(msg)
        return org_det(f)

      elif(request.form['logval']=="jobseeker"):
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
          return render_template('login.html',error='Please fill all fields')
        query = "SELECT * FROM JOBSEEKER3 WHERE email=?"
        stmt = ibm_db.prepare(conn, query)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        dictionary = ibm_db.fetch_assoc(stmt)
        if not dictionary:
          return render_template('login.html',error='Invalid Credentials')
      
        isPasswordMatch = bcrypt.checkpw(password.encode('utf-8'),dictionary['PASSWORD'].encode('utf-8'))

        if not isPasswordMatch:
          return render_template('login.html',error='Invalid Credentials')
        session['loggedin'] = True
        session['id'] = dictionary['EMAIL']
        f=session['id']
        session['active']="recruiter"
        msg = Message('New Login Found Just Now!!!', sender = 'spdineshwaran4@gmail.com', recipients = [session['id']])
        msg.body = "Hello User\nWe had came to know that you have logged in our jobby portal just now."
        mail.send(msg)
        # Redirect to home page
        return user_det(f)

  return render_template('login.html',name='Home')

@app.route('/browse')
def addMarker():
  if 'loggedin' in session:
    #------------------SPRINT-2-----------
  return render_template("browse.html",result=a)


@app.route('/companies')
def companies():
  #-----------------SPRINT-2--------
  return render_template("companies.html",result=a)


@app.route("/jobdiscription",methods=['GET','POST'])
def jobdiscription():
#---------------SPRINT-3--------------------------
    if request.method=='POST':
      jobid=request.form['jobid']
      print(jobid)
      return jd(jobid)
    return render_template('jobdiscription.html')

def jd(id1):
    query="SELECT * FROM JOBPOST WHERE JOB_ID = " + id1
    print(query)
    stmt = ibm_db.prepare(conn, query)
    ibm_db.execute(stmt)
    dictionary = ibm_db.fetch_assoc(stmt)
    jobtitle=dictionary["JOBTITLE"]
    jobtype=dictionary["JOBTYPE"]
    exp=dictionary["EXPERIENCE"]
    keyskills=dictionary["KEYSKILL"]
    location=dictionary["LOCATION"]
    salary=dictionary["SALARY"]
    discription=dictionary["DISCRIPTION"]
    return render_template('jobdiscription.html', jobid=id1, jobtitle=jobtitle, jobtype=jobtype, exp=exp, keyskills=keyskills, location=location, salary=salary, discription=discription)


@app.route("/applyjob",methods=['GET','POST'])
def applyjob():
#---------------SPRINT-3--------------------------
  if request.method=='POST':
    cand_id=request.form['cand_id']
    jobid=request.form['jobid']
    query="INSERT INTO APPLYJOB (CANDIDATE_ID, JOB_ID) VALUES(?,?)"
    prep_stmt=ibm_db.prepare(conn, query)
    ibm_db.bind_param(prep_stmt, 1, cand_id)
    ibm_db.bind_param(prep_stmt, 2, jobid)
    ibm_db.execute(prep_stmt)
    msg = Message('Application Submitted', sender = 'spdineshwaran4@gmail.com', recipients = [session['id']])
    msg.body = "Hello User,\nCongratulations!!!,You have successfully applied for the job.If you are shortlisted the recruiter will communicate with you\n\n\nWith regards,\nJobby."
    mail.send(msg)
  return render_template('browse.html')




@app.route("/browse/searchjob",methods=['GET','POST'])
def searchjob():
    if request.method=='POST':
        searchopt=request.form['searchopt']
        srctitle=request.form['srctitle']
        query = "SELECT * FROM JOBPOST WHERE "+searchopt+"="+chr(39)+srctitle+chr(39)
        stmt = ibm_db.prepare(conn, query)
        ibm_db.execute(stmt)
        a=[]
        isUser = ibm_db.fetch_assoc(stmt)
    
        while(isUser!=False):
          a.append(isUser)
          isUser = ibm_db.fetch_assoc(stmt)
    return render_template('browse.html',result=a)

if __name__ == "__main__": #checking if __name__'s value is '__main__'. __name__ is an python environment variable who's value will always be '__main__' till this is the first instatnce of app.py running
    app.run(debug=True,port=8080,host= '192.168.43.233') #running flask (Initalised on line 4)
