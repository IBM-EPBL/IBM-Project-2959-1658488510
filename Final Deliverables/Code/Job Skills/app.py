from flask import * #importing flask (Install it using python -m pip install flask)
import ibm_db
import bcrypt
import os
import random
import smtplib
from flask_mail import Mail, Message
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32733;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=phb43134;PWD=mTTnIE45Raj9A0rr",'','')

#import send_from_directory
app = Flask(__name__) #initialising flask
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
PEOPLE_FOLDER = os.path.join('static', 'people_photo')


mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'spdineshwaran4@gmail.com'
app.config['MAIL_PASSWORD'] = 'hmvzvqeoicwybaup'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/") #defining the routes for the home() funtion (Multiple routes can be used as seen here)
@app.route("/home")

def home():
    return render_template("home.html") #rendering our home.html contained within /templates

@app.route("/about")
def about():
  return render_template("about.html")


@app.route('/logout')
def logout():
     # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('active',None)
    session.pop('orgname',None)
    session.pop('otp',None)
    return redirect(url_for('home'))#rendering our login2.html contained within /templates



@app.route("/register",methods=['GET','POST'])
def register():
  if request.method == 'POST':
    email = request.form['email'] 
    password = request.form['password']
    firstname=request.form['firstname']
    middlename=request.form['middlename']
    lastname=request.form['lastname']
    dob=request.form['dob']
    age=request.form['age']
    drno=request.form['drno']
    landmark1=request.form['lnmk1']
    landmark2=request.form['lnmk2']
    village =request.form['village']
    district=request.form['district']
    pincode=request.form['pincode']
    country=request.form['country']
    country_code=request.form['countryCode']
    phone=request.form['phone']
    schlname10=request.form['schlname10']
    maxmark10=request.form['maxmark10'] 
    actmark10=request.form['actmark10']
    schlmark12=request.form['schlname212']
    maxmark12=request.form['maxmark212']
    actmark12=request.form['actmark212']
    clgname=request.form['clgname']
    clgmaxmark=request.form['clgmaxmark']
    clgactmark=request.form['clgactmark']
    stream=request.form['stream']
    graduation=request.form['graduation']
    grayear=request.form['grayear']
    branch=request.form['branch']
    skill=request.form['form[]']
    q1=request.form['Q1']
    q2=request.form['Q2']
    q3=request.form['Q3']
    q4=request.form['Q4']
    q5=request.form['Q5']
    position=request.form['position']
    expyears=request.form['expyears']
    designation=request.form['designation']
    pass   
    hash=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())


    query = "SELECT EMAIL FROM JOBSEEKER3 WHERE EMAIL=?"
    stmt = ibm_db.prepare(conn, query)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.execute(stmt)
    isUser = ibm_db.fetch_assoc(stmt)
    
    if not isUser:
      insert_sql = "INSERT INTO JOBSEEKER3 (EMAIL, PASSWORD, FIRSTNAME, MIDDLENAME, LASTNAME, DOB, AGE, DOOR_NO, LANDMARK1, LANDMARK2,VILLAGE, DISTRICT, PINCODE, COUNTRY, COUNTRY_CODE, PHONE, SCHOOL_NAME, SC_MAX_MARK, SC_ACT_MARK,HSC_SCHOOL_NAME,HSC_MAX_MARK, HSC_ACT_MARK,COLLEGE_NAME,COLLEGE_MAX,COLLEGE_ACT, STREAM, GRADUATION, GRADUATION_YEAR, BRANCH,SKILLS, PRESENTATION, HACKATHON, CODING, WON, PRIZE_WON, POSITION, EXPYEARS,DESIGNATION) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, email)
      ibm_db.bind_param(prep_stmt, 2, hash)
      ibm_db.bind_param(prep_stmt, 3, firstname)
      ibm_db.bind_param(prep_stmt, 4, middlename)
      ibm_db.bind_param(prep_stmt, 5, lastname)
      ibm_db.bind_param(prep_stmt, 6, dob)
      ibm_db.bind_param(prep_stmt, 7, age)
      ibm_db.bind_param(prep_stmt, 8, drno)
      ibm_db.bind_param(prep_stmt, 9, landmark1)
      ibm_db.bind_param(prep_stmt, 10, landmark2)
      ibm_db.bind_param(prep_stmt, 11, village)
      ibm_db.bind_param(prep_stmt, 12, district)
      ibm_db.bind_param(prep_stmt, 13, pincode)
      ibm_db.bind_param(prep_stmt, 14, country)
      ibm_db.bind_param(prep_stmt, 15, country_code)
      ibm_db.bind_param(prep_stmt, 16, phone)
      ibm_db.bind_param(prep_stmt, 17, schlname10)
      ibm_db.bind_param(prep_stmt, 18, maxmark10)
      ibm_db.bind_param(prep_stmt, 19, actmark10)
      ibm_db.bind_param(prep_stmt, 20, schlmark12)
      ibm_db.bind_param(prep_stmt, 21, maxmark12)
      ibm_db.bind_param(prep_stmt, 22, actmark12)
      ibm_db.bind_param(prep_stmt, 23, clgname)
      ibm_db.bind_param(prep_stmt, 24, clgmaxmark)
      ibm_db.bind_param(prep_stmt, 25, clgactmark)
      ibm_db.bind_param(prep_stmt, 26, stream)
      ibm_db.bind_param(prep_stmt, 27, graduation)
      ibm_db.bind_param(prep_stmt, 28, grayear)
      ibm_db.bind_param(prep_stmt, 29, branch)
      ibm_db.bind_param(prep_stmt, 30, skill)
      ibm_db.bind_param(prep_stmt, 31, q1)
      ibm_db.bind_param(prep_stmt, 32, q2)
      ibm_db.bind_param(prep_stmt, 33, q3)
      ibm_db.bind_param(prep_stmt, 34, q4)
      ibm_db.bind_param(prep_stmt, 35, q5)
      ibm_db.bind_param(prep_stmt, 36, position)
      ibm_db.bind_param(prep_stmt, 37, expyears)
      ibm_db. bind_param(prep_stmt, 38, designation)
      ibm_db.execute(prep_stmt)
      final_otp = ''
      for i in range(6):
        final_otp = final_otp + str(random.randint(0,9))
      msg = Message('Verification Code!!!', sender = 'spdineshwaran4@gmail.com', recipients = [email])
      msg.body = "OTP for Jobby Portal Verification "+final_otp
      mail.send(msg)
      session['id']=email
      session['active']="jobseeker"
      session['org']=firstname
      session['loggedin'] = True
      session['otp']=final_otp
      return redirect(url_for('vad'))
    else:
      return render_template('register.html',error1='Invalid Credentials')
  return render_template('register.html')

@app.route("/review",methods=['GET','POST'])
def review():
  if request.method == 'POST':
    email = request.form['cand_id'] 
    review = request.form['review']
    comment=request.form['comment']
    company=session['orgname']
    insert_sql="INSERT INTO REVIEW (CAND_ID, STAR, COMMENTS, COMPANY_NAME) VALUES(?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, email)
    ibm_db.bind_param(prep_stmt, 2, review)
    ibm_db.bind_param(prep_stmt, 3, comment)
    ibm_db.bind_param(prep_stmt,4, company)
    ibm_db.execute(prep_stmt)
    msg = Message('Review For You', sender ='spdineshwaran4@gmail.com', recipients = [email])
    msg.body = "Hello User,\nHurray!!!, Organisation named "+session['orgname']+". Give the review as\n"+"\nOut of 10 you scored "+review+"\nComment for you "+comment+"\n\n\nWith regards,\nJobby."
    mail.send(msg)
    return redirect(url_for('org_det'))
    
@app.route("/orgregister",methods=['GET','POST'])
def orgregister():
  if request.method == 'POST':
    email = request.form['email'] 
    password = request.form['password']
    orgname=request.form['orgname']
    ownername=request.form['ownername']
    doe=request.form['doe']
    empcount=request.form['empcount']
    drno=request.form['drno']
    landmark1=request.form['lnmk1']
    landmark2=request.form['lnmk2']
    village =request.form['village']
    district=request.form['district']
    pincode=request.form['pincode']
    country=request.form['country']
    country_code=request.form['countryCode']
    phone=request.form['phone']
    domain=request.form['form[]']
    q1=request.form['Q1']
    q2=request.form['Q2']
    q3=request.form['Q3']
    state=request.form['state']
    pass   
    hash=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

    query = "SELECT EMAIL FROM RECRUITER WHERE EMAIL=?"
    stmt = ibm_db.prepare(conn, query)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.execute(stmt)
    isUser = ibm_db.fetch_assoc(stmt)

    
    if not isUser:
      insert_sql = "INSERT INTO RECRUITER (EMAIL, PASSWORD, ORG_NAME, OWNER_NAME, DOE, EMPLOYEE_COUNT, DOOR_NO, LANDMARK1, LANDMARK2,VILLAGE, DISTRICT, PINCODE, COUNTRY, COUNTRY_CODE, PHONE, DOMAIN, MNC, TOP_POSITION, SALARY_HIKE, STATE) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, email)
      ibm_db.bind_param(prep_stmt, 2, hash)
      ibm_db.bind_param(prep_stmt, 3, orgname)
      ibm_db.bind_param(prep_stmt, 4, ownername)
      ibm_db.bind_param(prep_stmt, 5, doe)
      ibm_db.bind_param(prep_stmt, 6, empcount)
      ibm_db.bind_param(prep_stmt, 7, drno)
      ibm_db.bind_param(prep_stmt, 8, landmark1)
      ibm_db.bind_param(prep_stmt, 9, landmark2)
      ibm_db.bind_param(prep_stmt, 10, village)
      ibm_db.bind_param(prep_stmt, 11, district)
      ibm_db.bind_param(prep_stmt, 12, pincode)
      ibm_db.bind_param(prep_stmt, 13, country)
      ibm_db.bind_param(prep_stmt, 14, country_code)
      ibm_db.bind_param(prep_stmt, 15, phone)
      ibm_db.bind_param(prep_stmt, 16, domain)
      ibm_db.bind_param(prep_stmt, 17, q1)
      ibm_db.bind_param(prep_stmt, 18, q2)
      ibm_db.bind_param(prep_stmt, 19, q3)
      ibm_db. bind_param(prep_stmt,20, state)
      ibm_db.execute(prep_stmt)
      final_otp = ''
      for i in range(6):
        final_otp = final_otp + str(random.randint(0,9))
      msg = Message('Verification Code!!!', sender = 'spdineshwaran4@gmail.com', recipients = [email])
      msg.body = "OTP for Jobby Portal Verification "+final_otp
      mail.send(msg)
      session['id']=email
      session['orgname']=orgname
      session['active']="recruiter"
      session['loggedin'] = True
      session['otp']=final_otp
      return redirect(url_for('vad'))

    else:
      return render_template('orgregister.html',error1='Invalid Credentials')
  return render_template('orgregister.html')
  
@app.route('/vad')
def vad():
  return render_template('verify.html')

@app.route('/validate',methods=["POST","GET"])   
def validate(): 
  current_user_otp = session['otp']
  user_otp = request.form['otp'] 
  if int(current_user_otp) == int(user_otp):
      msg = Message('Account Activated', sender ='spdineshwaran4@gmail.com', recipients = [session['id']])
      msg.body = "Hello User,\nHurray!!!,Welcome to Jobby,\n Your account had been successfully created. Now keep updated on job vacancies and get hired.\n\n\nWith regards,\nJobby."
      mail.send(msg)  
      return redirect(url_for('home'))
  else:
      return render_template('verify.html',error="Invalid")   
  return render_template('verify.html')
  


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
        session['orgname']=dictionary['ORG_NAME']
        # Redirect to home page
        session['active']="recruiter"
        msg = Message('New Login Found Just Now!!!', sender = 'spdineshwaran4@gmail.com', recipients = [session['id']])
        msg.body = "Hello User\nWe had came to know that you have logged in our jobby portal just now."
        mail.send(msg)
        return redirect(url_for('org_det'))

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
        session['orgname']=dictionary['FIRSTNAME']
        session['active']="jobseeker"
        msg = Message('New Login Found Just Now!!!', sender = 'spdineshwaran4@gmail.com', recipients = [session['id']])
        msg.body = "Hello User\nWe had came to know that you have logged in our jobby portal just now."
        mail.send(msg)
        return redirect(url_for('user_det'))
  return render_template('login.html',name='Home')

@app.route('/browse')
def browse():
  if 'loggedin' in session:
    query = "SELECT * FROM jobpost;"
    stmt = ibm_db.prepare(conn, query)
    ibm_db.execute(stmt)
    a=[]
    isUser = ibm_db.fetch_assoc(stmt)
    
    while(isUser!=False):
      a.append(isUser)
      isUser = ibm_db.fetch_assoc(stmt)
  else:
    return redirect(url_for('login'))
  return render_template("browse.html",result=a)


@app.route('/companies')
def companies():
  if 'loggedin' in session:
    query = "SELECT * FROM RECRUITER"
    stmt = ibm_db.prepare(conn, query)
    ibm_db.execute(stmt)
    a=[]
    isUser = ibm_db.fetch_assoc(stmt)
    
    while(isUser!=False):
      a.append(isUser)
      isUser = ibm_db.fetch_assoc(stmt)
  else:
    return redirect(url_for('login'))
  return render_template("companies.html",result=a)


@app.route("/jobdiscription",methods=['GET','POST'])
def jobdiscription():
    if request.method=='POST':
      jobid=request.form['jobid']
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
    recruiter_id=dictionary["RECRUITER_ID"]
    return render_template('jobdiscription.html', jobid=id1, jobtitle=jobtitle, jobtype=jobtype, exp=exp, keyskills=keyskills, location=location, salary=salary, discription=discription,orgid=recruiter_id)
    #rendering our register.html contained within /templates
    #rendering our register.html contained within /templates

@app.route("/applyjob",methods=['GET','POST'])
def applyjob():
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
    return redirect(url_for('browse'))
  return redirect(url_for('browse'))

@app.route("/subscribe",methods=['GET','POST'])
def subscribe():
  if request.method=='POST':
    orgid=request.form['orgid']
    candidateid=request.form['candidateid']
    orgname=request.form['orgname']
    insert_sql="INSERT INTO SUBSCRIBE (RECRUITER_ID, CANDIDATE_ID, ORGANIZATION_NAME) VALUES (?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, orgid)
    ibm_db.bind_param(prep_stmt, 2, candidateid)
    ibm_db.bind_param(prep_stmt, 3, orgname)
    ibm_db.execute(prep_stmt)
    return redirect(url_for('companies'))
  return render_template('companies.html')

@app.route("/org_dashboard")
def org_det():
  query = "SELECT * FROM RECRUITER WHERE email="+chr(39)+session['id']+chr(39)
  stmt = ibm_db.prepare(conn, query)
  ibm_db.execute(stmt)
  dictionary = ibm_db.fetch_assoc(stmt)
  email=dictionary["EMAIL"]
  orgname=dictionary["ORG_NAME"]
  ownername=dictionary["OWNER_NAME"]
  doe=dictionary["DOE"]
  empcount=dictionary["EMPLOYEE_COUNT"]
  drno=dictionary["DOOR_NO"]
  landmark1=dictionary["LANDMARK1"]
  landmark2=dictionary["LANDMARK2"]
  village =dictionary["VILLAGE"]
  district=dictionary["DISTRICT"]
  pincode=dictionary["PINCODE"]
  country=dictionary["COUNTRY"]
  country_code=dictionary["COUNTRY_CODE"]
  phone=dictionary["PHONE"]
  domain=dictionary["DOMAIN"]
  q1=dictionary["MNC"]
  q2=dictionary["TOP_POSITION"]
  q3=dictionary["SALARY_HIKE"]
  state=dictionary["STATE"] 
  session['email'] = dictionary['EMAIL']
  query1 ="SELECT * FROM APPLYJOB WHERE RECRUITER_ID= "+chr(39)+session['id']+chr(39)
  print(query1)
  stmt2=ibm_db.prepare(conn, query1)
  ibm_db.execute(stmt2)
  a2=[]
  isUser = ibm_db.fetch_assoc(stmt2)
  while(isUser!=False):
    a2.append(isUser)
    isUser = ibm_db.fetch_assoc(stmt2)
  return render_template('org_dashboard.html',email=email, orgname=orgname, ownername=ownername,doe=doe,empcount=empcount,drno=drno,landmark1=landmark1, landmark2=landmark2, village=village, district=district,pincode=pincode,country=country,country_code=country_code,phone=phone,domain=domain,q1=q1,q2=q2,q3=q3,state=state,result=a2)

@app.route("/user_dashboard")
def user_det():
  query = "SELECT * FROM JOBSEEKER3 WHERE email="+chr(39)+session['id']+chr(39)
  stmt = ibm_db.prepare(conn, query)
  ibm_db.execute(stmt)
  dictionary = ibm_db.fetch_assoc(stmt)
  email1=dictionary["EMAIL"]
  firstname=dictionary["FIRSTNAME"]
  middlename=dictionary["MIDDLENAME"]
  lastname=dictionary["LASTNAME"]
  dob=dictionary["DOB"]
  age=dictionary["AGE"]
  drno=dictionary["DOOR_NO"]
  landmark1=dictionary["LANDMARK1"]
  landmark2=dictionary["LANDMARK2"]
  village =dictionary["VILLAGE"]
  district=dictionary["DISTRICT"]
  pincode=dictionary["PINCODE"]
  country=dictionary["COUNTRY"]
  country_code=dictionary["COUNTRY_CODE"]
  phone=dictionary["PHONE"]
  schlname10=dictionary["SCHOOL_NAME"]
  maxmark10=dictionary["SC_MAX_MARK"] 
  actmark10=dictionary["SC_ACT_MARK"]
  schlmark12=dictionary["HSC_SCHOOL_NAME"]
  maxmark12=dictionary["HSC_MAX_MARK"]
  actmark12=dictionary["HSC_ACT_MARK"]
  clgname=dictionary["COLLEGE_NAME"]
  clgmaxmark=dictionary["COLLEGE_MAX"]
  clgactmark=dictionary["COLLEGE_ACT"]
  stream=dictionary["STREAM"]
  graduation=dictionary["GRADUATION"]
  grayear=dictionary["GRADUATION_YEAR"]
  branch=dictionary["BRANCH"]
  skill=dictionary["SKILLS"]
  q1=dictionary["PRESENTATION"]
  q2=dictionary["HACKATHON"]
  q3=dictionary["CODING"]
  q4=dictionary["WON"]
  q5=dictionary["PRIZE_WON"]
  position=dictionary["POSITION"]
  expyears=dictionary["EXPYEARS"]
  designation=dictionary["DESIGNATION"]
  session['email'] = dictionary["EMAIL"]
  query1 ="SELECT * FROM APPLYJOB WHERE CANDIDATE_ID="+chr(39)+session['id']+chr(39)
  stmt2=ibm_db.prepare(conn, query1)
  ibm_db.execute(stmt2)
  a2=[]
  isUser = ibm_db.fetch_assoc(stmt2)
  while(isUser!=False):
    a2.append(isUser)
    isUser = ibm_db.fetch_assoc(stmt2)
  return render_template('user_dashboard.html',email=email1, name=firstname+middlename+lastname, dob=dob,age=age,drno=drno,landmark1=landmark1, landmark2=landmark2, village=village, district=district,pincode=pincode,country=country,country_code=country_code,phone=phone,schlname10=schlname10,maxmark10=maxmark10,actmark10=actmark10,schlname12=schlmark12,maxmark12=maxmark12,actmark12=actmark12,clgname=clgname,clgmaxmark=clgmaxmark,clgactmark=clgactmark, stream=stream,graduation=graduation,grayear=grayear,branch=branch,skill=skill,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,position=position,expyears=expyears,designation=designation,result=a2)

@app.route("/candidate_info",methods=['GET','POST'])
def candinfo():
  if request.method=="POST":
    candid=request.form['candid']
    query = "SELECT * FROM JOBSEEKER3 WHERE email="+chr(39)+candid+chr(39)
    stmt = ibm_db.prepare(conn, query)
    ibm_db.execute(stmt)
    dictionary = ibm_db.fetch_assoc(stmt)
    email1=dictionary["EMAIL"]
    firstname=dictionary["FIRSTNAME"]
    middlename=dictionary["MIDDLENAME"]
    lastname=dictionary["LASTNAME"]
    dob=dictionary["DOB"]
    age=dictionary["AGE"]
    drno=dictionary["DOOR_NO"]
    landmark1=dictionary["LANDMARK1"]
    landmark2=dictionary["LANDMARK2"]
    village =dictionary["VILLAGE"]
    district=dictionary["DISTRICT"]
    pincode=dictionary["PINCODE"]
    country=dictionary["COUNTRY"]
    country_code=dictionary["COUNTRY_CODE"]
    phone=dictionary["PHONE"]
    schlname10=dictionary["SCHOOL_NAME"]
    maxmark10=dictionary["SC_MAX_MARK"] 
    actmark10=dictionary["SC_ACT_MARK"]
    schlmark12=dictionary["HSC_SCHOOL_NAME"]
    maxmark12=dictionary["HSC_MAX_MARK"]
    actmark12=dictionary["HSC_ACT_MARK"]
    clgname=dictionary["COLLEGE_NAME"]
    clgmaxmark=dictionary["COLLEGE_MAX"]
    clgactmark=dictionary["COLLEGE_ACT"]
    stream=dictionary["STREAM"]
    graduation=dictionary["GRADUATION"]
    grayear=dictionary["GRADUATION_YEAR"]
    branch=dictionary["BRANCH"]
    skill=dictionary["SKILLS"]
    q1=dictionary["PRESENTATION"]
    q2=dictionary["HACKATHON"]
    q3=dictionary["CODING"]
    q4=dictionary["WON"]
    q5=dictionary["PRIZE_WON"]
    position=dictionary["POSITION"]
    expyears=dictionary["EXPYEARS"]
    designation=dictionary["DESIGNATION"]
    return render_template('candidate_info.html',email=candid, name=firstname+middlename+lastname, dob=dob,age=age,drno=drno,landmark1=landmark1, landmark2=landmark2, village=village, district=district,pincode=pincode,country=country,country_code=country_code,phone=phone,schlname10=schlname10,maxmark10=maxmark10,actmark10=actmark10,schlname12=schlmark12,maxmark12=maxmark12,actmark12=actmark12,clgname=clgname,clgmaxmark=clgmaxmark,clgactmark=clgactmark, stream=stream,graduation=graduation,grayear=grayear,branch=branch,skill=skill,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,position=position,expyears=expyears,designation=designation)
  return render_template('candidate_info.html')


@app.route("/jobpost",methods=['GET','POST'])
def jobpost():
  if 'loggedin' in session:
      if request.method == 'POST':
          recruiterid=request.form['recruiter_id']
          orgname=request.form['company_name']
          jobtitle = request.form['jobtitle'] 
          jobtype = request.form['jobtype']
          jobexp=request.form['jobexperience']
          keyskill=request.form['keyskills']
          location=request.form['location']
          salary=request.form['salary']
          discription=request.form['discription']
          insert_sql = "INSERT INTO JOBPOST (RECRUITER_ID,JOBTITLE, JOBTYPE, EXPERIENCE, KEYSKILL, LOCATION, SALARY, DISCRIPTION, COMPANY_NAME) VALUES (?,?,?,?,?,?,?,?,?)"
          prep_stmt = ibm_db.prepare(conn, insert_sql)
          ibm_db.bind_param(prep_stmt, 1, recruiterid)
          ibm_db.bind_param(prep_stmt, 2, jobtitle)
          ibm_db.bind_param(prep_stmt, 3, jobtype)
          ibm_db.bind_param(prep_stmt, 4, jobexp)
          ibm_db.bind_param(prep_stmt, 5, keyskill)
          ibm_db.bind_param(prep_stmt, 6, location)
          ibm_db.bind_param(prep_stmt, 7, salary)
          ibm_db.bind_param(prep_stmt, 8, discription)
          ibm_db.bind_param(prep_stmt, 9, orgname)
          ibm_db.execute(prep_stmt)
          query = "SELECT EMAIL FROM JOBSEEKER3"
          stmt = ibm_db.prepare(conn, query)
          ibm_db.execute(stmt)
          a=[]
          isUser = ibm_db.fetch_assoc(stmt)
          while(isUser!=False):
            a.append(isUser)
            isUser = ibm_db.fetch_assoc(stmt)
          print(a)
          for i in a:
            id1=str(i['EMAIL'])
            print(id1)
            msg = Message('New Job Posted', sender ='spdineshwaran4@gmail.com', recipients = [id1])
            msg.body = "Hello User,\nHurray!!!,New job vacancy had uploded by "+session['orgname']+". Let check the Jobby Portal and keep updated."+"\n\n\nWith regards,\nJobby."
            mail.send(msg)
          return redirect(url_for('jobpost'))
            

  else:
      return redirect(url_for('login'))
  return render_template("jobpost.html")


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
    app.run(debug=True) #running flask (Initalised on line 4)
