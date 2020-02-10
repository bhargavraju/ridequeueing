from flask import Flask, request
from db import request_data
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Welcome to the Queueing App"


@app.route('/customer/request', methods=['POST'])
def create_request():
    """
    Creates a new ride request by a customer
    :param: customer_id: str
    :return: Success Message
    """
    inputs = request.get_json(force=True)
    customer_id = inputs['customer_id']
    request_data.create_request(customer_id)
    return "Request for a ride created successfully", 201


@app.route('/request/waiting', methods=['POST'])
def waiting_requests():
    """
    Lists all waiting requests
    :return: Requests in the 'waiting' state
    """
    return {'requests': request_data.get_waiting_requests()}, 200


@app.route('/driver/request/ongoing', methods=['POST'])
def ongoing_requests():
    """
    Lists requests being served by a driver
    :param: driver_id: str
    :return: Requests in the ongoing state served by a driver
    """
    inputs = request.get_json(force=True)
    driver_id = inputs['driver_id']
    return {'requests': request_data.get_ongoing_requests(driver_id)}, 200


@app.route('/driver/request/completed', methods=['POST'])
def completed_requests():
    """
    Lists requests completed by a driver
    :param: driver_id: str
    :return: Requests completed by a driver
    """
    inputs = request.get_json(force=True)
    driver_id = inputs['driver_id']
    return {'requests': request_data.get_completed_requests(driver_id)}, 200


@app.route('/driver/request', methods=['POST'])
def select_request():
    """
    Driver selects a request to serve
    :param: request_id: str
    :param: driver_id: str
    :return: Appropriate action message
    """
    inputs = request.get_json(force=True)
    request_id = inputs['request_id']
    driver_id = inputs['driver_id']
    if request_data.get_request_entry(request_id) is None:
        return "Request with specified id doesn't exist", 400
    elif not request_data.request_available(request_id):
        return "Request no longer available", 409
    else:
        request_data.accept_request(request_id, driver_id)
        return "Request accepted", 200


@app.route('/request', methods=['POST'])
def waiting_requests():
    """
    Lists all waiting requests
    :return: Requests in the 'waiting' state
    """
    return {'requests': request_data.get_all_requests()}, 200
