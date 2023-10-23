from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def get_info():
    try:
        if request.method == "GET":
            return "Hello Backend", 200
    except Exception as e:
        print(f"error {e}")
        return "Cant get info", 404

@main.route('/about_me', methods=['POST'])
def about_me():
    try:
        if request.method == "POST":
            info = {
                "Name": "CHRISTOPHER TAN",
                "Course": "COMPUTER SCIENCE",
                "Year": 1,
                "List all your CCA's": "RHDevs, Tech Crew, Commotion, RHVoices"
            }
            print("info sent")
            return jsonify(info), 201
    except Exception as e:
        print(f"error {e}")
        return "Can't send info", 404