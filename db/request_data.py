from db.mysqlconnection import execute_read_query, execute_modify_query
import datetime


def get_request_entry(request_id):
    query = """select * from requests where request_id={}""".format(request_id)
    result = execute_read_query(query)
    return result[0]


def create_request(customer_id):
    query = """insert into requests (customer_id) VALUES ({})""".format(customer_id)
    execute_modify_query(query)


def request_available(request_id):
    request = get_request_entry(request_id)
    if request[4] is None:
        return True
    else:
        return False


def accept_request(request_id, driver_id):
    now = datetime.datetime.now()
    complete = now + datetime.timedelta(minutes=5)
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    complete = complete.strftime('%Y-%m-%d %H:%M:%S')
    query = """update requests set driver_id={},picked_up="{}",completed="{}" where request_id={}""".\
        format(driver_id, now, complete, request_id)
    execute_modify_query(query)


def get_waiting_requests():
    query = """select * from requests where driver_id is NULL"""
    result = execute_read_query(query)
    return result


def get_all_requests():
    query = """select * from requests"""
    result = execute_read_query(query)
    return result


def get_ongoing_requests(driver_id):
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    query = """select * from requests where (driver_id={}) and ("{}" between picked_up and completed)""".\
        format(driver_id, now)
    result = execute_read_query(query)
    return result


def get_completed_requests(driver_id):
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    query = """select * from requests where (driver_id={}) and ("{}" > completed)""".\
        format(driver_id, now)
    result = execute_read_query(query)
    return result

