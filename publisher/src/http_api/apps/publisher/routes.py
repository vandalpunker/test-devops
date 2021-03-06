from flask import Blueprint
from flask import jsonify
from flask import request

from src.application.use_cases.publisher import PublisherUse

publisher = Blueprint("publisher", __name__)


@publisher.route("/", methods=["POST"])
def start_publisher():
    if request.method == "POST":
        data = request.get_json()
        PublisherUse.send(data)
        return jsonify(data), 200
