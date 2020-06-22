from flask import Blueprint
from flask import jsonify
from flask import request

from src.application.use_cases.consumer import ConsumerUse

consumer = Blueprint("consumer", __name__)


@consumer.route("/", methods=["GET"])
def start_consumer():
    if request.method == "GET":
        data = request.get_json()
        ConsumerUse.receiver(data)
        return jsonify({"message": "it works"}), 200
