from flask import render_template, request, flash,redirect
from flask.helpers import url_for
from uispage import app, mail
from uispage.forms import GradesForm, ContactForm
from uispage.config import email
import base64
from io import BytesIO
from matplotlib.figure import Figure
from flask_mail import Message

@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/grades', methods=['GET', 'POST'])
def grades():
    form = GradesForm()
    gradesfinal,check = 0,False
    if request.method == 'POST':
        if form.validate_on_submit():
            #Suma y creacion de listas con el promedio
            gradesfinal =([float(request.form[f"grade{i}"]) * float(request.form[f"percentage{i}"]) / 100 for i in range(1, 7) if request.form[f"grade{i}"] != '0.00' and request.form[f"percentage{i}"] != '0.00'
            and request.form[f"grade{i}"] != '0.0' and request.form[f"percentage{i}"] != '0.0' and request.form[f"grade{i}"] != '0' and request.form[f"percentage{i}"] != '0'])
            gradesfinalsum = sum([float(request.form[f"grade{i}"]) * float(request.form[f"percentage{i}"]) / 100 for i in range(1, 7) if request.form[f"grade{i}"] != '0.00' and request.form[f"percentage{i}"] != '0.00'
            and request.form[f"grade{i}"] != '0.0' and request.form[f"percentage{i}"] != '0.0' and request.form[f"grade{i}"] != '0' and request.form[f"percentage{i}"] != '0'])
            sumpercentages = sum([float(request.form[f"percentage{i}"]) for i in range(1, 7) if request.form[f"grade{i}"] != '0.00' and request.form[f"percentage{i}"] != '0.00'
            and request.form[f"grade{i}"] != '0.0' and request.form[f"percentage{i}"] != '0.0' and request.form[f"grade{i}"] != '0' and request.form[f"percentage{i}"] != '0'])
            check = True
        else:
            flash('Error in the forms, please check ur information again', category='danger')

        if gradesfinal != 0 and len(gradesfinal) >=1 and sumpercentages <= 100:
            flash(('Su nota final es ' + str(gradesfinalsum)), category='success')
            normalgrades = [3.0,1.5,0.9998999999999999,0.75,0.6,0.5000100000000001]
            superiorgrades = [4.3,2.15,1.43319,1.075,0.86,0.7166810000000001]
            fig = Figure()
            ax = fig.subplots(2)
            columns = ['Grade 1']
            for i in range(2,7):
                if len(gradesfinal) > len(columns):
                    columns.append(f'Grade {i}')
                else:
                    break
            for i in range(1,7):
                if len(gradesfinal) == i:
                    line = normalgrades[i-1]
                    print(line,i)
            for i in range(1,7):
                if len(gradesfinal) == i:
                    line2 = superiorgrades[i-1]
                    print(line,i)
            ax[1].bar('Final Grade',gradesfinalsum, color='blue', edgecolor='blue')
            ax[0].bar(columns,gradesfinal, color='red', edgecolor='red')
            ax[0].set_ylabel('Grades with the % applied')
            ax[1].set_xlabel('Your final grade is '+str(gradesfinalsum))
            ax[1].axhline(y = 3.0, color = 'r', linestyle = '--', label= 'Basic Grade(3.0) ')
            ax[1].axhline(y = 4.4, color = 'g', linestyle = '--', label= 'Superior Grade(4.4) ')
            ax[1].legend()
            # Save it to a temporary buffer.    
            buf = BytesIO() 
            fig.savefig(buf, format="png")
            # Embed the result in the html output.
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            return render_template('grades.html',data=data,form=form)
        else:
            if check and sumpercentages <= 100:
                flash('Error in the forms, Your grades cant be all 0', category='danger')
            else:
                flash('The sum of the percentages can be upper than 100%', category='danger')

    return render_template('grades.html',form=form)


@app.route('/about', methods=['GET', 'POST'])
def about():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            msg = Message(subject=request.form['subject'],sender='noreply@demo.com', recipients=[email])
            msg.body = 'Nombre: ' + request.form['name'] + ' Email: ' + request.form['email'] +' -- Mensaje: ' + request.form['information']
            mail.send(msg)
            flash('An email has been sent , thank you.',category='success')
        else:
            flash('Incorrect', category='danger')
            return render_template('about.html', form=form)
    return render_template('about.html', form=form)

@app.route('/circuits', methods=['GET', 'POST'])
def circuits():
    return render_template('circuits.html')