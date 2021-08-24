from flask import Flask, render_template, request
import requests
import smtplib


app = Flask(__name__)

API_ENDPOINT = 'my_api_endpoint'
all_posts = requests.get(API_ENDPOINT).json()

@app.route('/')
def home():
    return render_template('index.html', all_posts=all_posts)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/post/<int:num>')
def indv_post(num):
    post = None
    for obj in all_posts:
        print(obj)
        if obj['id'] == num:
            post = obj
    return render_template('post.html', post=post)

@app.route('/contact/', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        remetente = 'remetente@gmail.com'
        senha = 'senhadoremetente'

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(remetente, senha)
            connection.sendmail(remetente, 'destinatário@gmail.com',
                                msg=f'Subject:[BLOG] New Message\n\n'
                                    f'Nome: {name}\n'
                                    f'Telefone: {phone}\n'
                                    f'E-mail: {email}\n'
                                    f'Mensagem:\n'
                                    f'{message}'.encode('utf8'))

        return render_template('contact.html', success=True)
    return render_template('contact.html', success=False)


if __name__ == "__main__":
    app.run(debug=True)
