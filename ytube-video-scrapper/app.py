from flask import Flask

# Import api routes
from src.scrapper import scrapper_blueprint

app = Flask(__name__)
# Register blueprint
app.register_blueprint(scrapper_blueprint)

@app.route('/')
def home():
    return 'Silence is Gold!'

if __name__ == "__main__":
    app.run()