from flask import Flask
from routes.recommend import recommend_bp
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(recommend_bp)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
