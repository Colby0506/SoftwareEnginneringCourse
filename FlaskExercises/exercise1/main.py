from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def current_time():
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return f"Current Date and Time: {formatted_time}"

if __name__ == '__main__':
    app.run(debug=True)
