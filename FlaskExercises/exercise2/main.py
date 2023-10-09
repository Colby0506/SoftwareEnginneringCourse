from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check_number():
    number = request.args.get('number', None)

    if number is not None:
        try:
            number = int(number)
            is_integer = True
            is_even = number % 2 == 0
        except ValueError:
            is_integer = False
            is_even = False
    else:
        is_integer = False
        is_even = False

    return render_template('result.html', number=number, is_integer=is_integer, is_even=is_even)

if __name__ == '__main__':
    app.run(debug=True)
