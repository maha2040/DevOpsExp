from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        return render_template('success.html', name=name, email=email)
    
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
