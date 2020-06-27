from flask import Blueprint
from flask import jsonify
from flask import request

from src.application.use_cases.consumer import ConsumerUse

consumer = Blueprint("consumer", __name__)


@consumer.route("/healthcheck", methods=["GET"])
def health_check():
    if request.method == "GET":
        return jsonify({"status": "up"}), 200


@consumer.route("/", methods=["POST"])
def start_consumer():
    if request.method == "POST":
        data = request.get_json()
        ConsumerUse.receiver(data)
        return jsonify({"message": "it works"}), 200
