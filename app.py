from flask import Flask

app = Flask(__name__)  # Create a Flask web app

@app.route('/')  # Define a route (URL) for the home page
def home():
    return "Hello, World!"  # This is what the page will show

if __name__ == '__main__':
    app.run(debug=True)  # Start the web server
