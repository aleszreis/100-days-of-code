from bs4 import BeautifulSoup
import requests
import smtplib

URL = 'https://www.amazon.com.br/OProdutoAqui'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')


title = soup.find(name='span', id='productTitle').getText().strip()
print(title)

price = soup.find(name='span', id='priceblock_ourprice')
float_price = float(price.getText()[2:].replace(",", "."))
print(float_price)


if float_price <= 400:
    email = 'emaildeorigem@gmail.com'
    senha = 'senha'

    email_message = f"{title} está por R$ {float_price}.\n{URL}"

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(email, senha)
        connection.sendmail(email, 'emaildedestino@gmail.com',
                            msg=f'Subject:Abaixou o preço!\n\n{email_message}'.encode('utf8'))
