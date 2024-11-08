from flask import Flask, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost/ALPHA_WEB"
mongo = PyMongo(app)

@app.route("/users", methods=["POST"])
def create_users():
    # Recibir datos
    username = request.json["username"]
    password = request.json["password"]
    email = request.json["email"]
    
    if username and email and password:
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert_one(
            {"username": username,
            "email": email,
            "password": hashed_password}
        ).inserted_id
        response = {
            "id": str(id),
            "username": username,
            "password": password,
            "email": email
        }
        
        return response
    
    else:
        return {"message": "received"}

# Conexión a MongoDB
if __name__ == "__main__":
    app.run(debug=True)

