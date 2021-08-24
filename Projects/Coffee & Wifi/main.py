from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MySecretKey'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    op_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    cof_rate = SelectField('Coffee Rating', choices=['⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'], validators=[DataRequired()])
    wil_rate = SelectField('Wifi Strength Rating', choices=['❌', '🔴', '🟠🟠', '🟡🟡🟡', '🟢🟢🟢🟢', '🟢🟢🟢🟢🟢'], validators=[DataRequired()])
    power_rate = SelectField('Power Socket Availability', choices=['❌', '🔴', '🟠🟠', '🟡🟡🟡', '🟢🟢🟢🟢', '🟢🟢🟢🟢🟢'], validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", "a", encoding='utf-8') as f:
            f.write(f"\n{form.cafe.data},{form.location.data},{form.op_time.data},{form.close_time.data},{form.cof_rate.data},{form.wil_rate.data},{form.power_rate.data}")
        return redirect(url_for('add_cafe'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
