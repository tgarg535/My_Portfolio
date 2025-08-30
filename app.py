from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
import secrets

app = Flask(__name__, static_folder='assets', template_folder='templates')
app.secret_key = 'your_generated_secret_key_here'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/data/<path:filename>')
def download_file(filename):
    return send_from_directory('data', filename)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('contact_name')
    email = request.form.get('contact_email')
    message = request.form.get('contact_message')

    # Email setup
    sender = 'tanushgarg26jul@gmail.com'
    receiver = 'tanushgarg26jul@gmail.com'
    password = 'wtwz tonh uvpi cpvg'

    subject = f"New Contact Message from {name}"
    body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['Reply-To'] = email
    msg['To'] = receiver

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        flash('Thank you for considering me!', 'success')
    except Exception as e:
        flash('Sorry, there was an error sending your message.', 'danger')

    return redirect(url_for('home') + '#contact')

if __name__ == '__main__':
    app.run(debug=True)

print(secrets.token_hex(16))