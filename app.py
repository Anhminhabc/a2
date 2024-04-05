from flask import Flask, render_template

app = Flask(__name__)

message = "hello"

@app.route('/')
def index():
    return render_template('index.html', message=message)

@app.route('/update')
def update_message():
    global message
    if message == "hello":
        message = "how are you?"
    else:
        message = "I'm fine thank you and you?"
    return message

if __name__ == '__main__':
    app.run(debug=True)