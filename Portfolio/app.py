from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Here you would typically save to database or send email
    return jsonify({'status': 'success', 'message': f'Thank you, {name}. Your message has been received!'})

if __name__ == '__main__':
    app.run(debug=True)