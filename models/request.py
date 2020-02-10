import uuid
from fields import R_CUST_ID, R_INIT_TIME, R_ID, R_STATUS, R_DR_ID, R_PICK_TIME, R_COMPL_TIME


def load_request(request_doc):
    request = Request(request_doc[R_CUST_ID], request_doc[R_INIT_TIME], request_doc[R_ID], request_doc[R_STATUS],
                      request_doc[R_DR_ID], request_doc[R_PICK_TIME], request_doc[R_COMPL_TIME])
    return request


class Request:
    def __init__(self, customer_id, request_time,
                 request_id=None, status=None, driver_id=None, picked_up=None, completed=None):
        self.customer_id = customer_id
        self.request_time = request_time
        self.request_id = uuid.uuid4().hex if request_id is None else request_id
        # self.status = R_ST_WAITING if status is None else status
        self.driver_id = driver_id
        self.picked_up = picked_up
        self.completed = completed

    def json(self):
        return {
            R_CUST_ID: self.customer_id,
            R_INIT_TIME: self.request_time,
            R_ID: self.request_id,
            # R_STATUS: self.status,
            R_DR_ID: self.driver_id,
            R_PICK_TIME: self.picked_up,
            R_COMPL_TIME: self.completed
        }
