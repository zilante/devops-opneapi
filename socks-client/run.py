from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
configuration = None
api_instance = swagger_client.ControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.SockRequest(color="color", cotton_part="10", quantity="3") # SockRequest | 

try:
    api_response = api_instance.add_socks(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->add_socks: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ControllerApi(swagger_client.ApiClient(configuration))
color = "color" # str | 
operation = "lessThan" # str | 
cotton_part = 56 # int | 

try:
    api_response = api_instance.get_sock_quantity(color, operation, cotton_part)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->get_sock_quantity: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.ControllerApi(swagger_client.ApiClient(configuration)) 

try:
    api_response = api_instance.delete_socks(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->delete_socks: %s\n" % e)
