from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global dictionary to store registered users
registered_users = {}

# List of valid organizations
valid_organizations = ["Organization A", "Organization B", "Organization C", "Organization D", "Organization E"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    organization = request.form.get('organization')

    # Backend validation
    if not name or not organization or organization not in valid_organizations:
        return "Invalid input. Please fill out all fields and select a valid organization."

    # Store user registration in the global dictionary
    registered_users[name] = organization

    return redirect('/registered')

@app.route('/registered')
def registered():
    return render_template('registered.html', users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)
