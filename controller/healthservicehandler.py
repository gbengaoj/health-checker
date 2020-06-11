import os
import requests, urllib.request, json
import datetime

class HandleService:
    """Class To Handle Request passed"""


    # Result Gotten from each service health check
    # This would be appended to the all_services list
    output = {
        'Service Url': None,
        'Health-Check Status': None,
        'Last Update Time': None,
        }

    result = [] 

    def process_service_check(self, service):
        self.result = []
        microservice = 0
        microservices = len(service)
        while microservice < microservices:
            self.check_service_health(service[microservice])
            microservice += 1
        return self.result

    # Check the service status and availabilty
    def check_service_health(self, service):
        try:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            harmless_status = range(200, 308)
            client_error_status = range(400, 499)
            server_error_status = range(500, 599)
            self.output['Service Url'] = service
            self.result.append(self.output['Service Url'])
            response = requests.head(service) # request url
            response_status = response.status_code # response status code
            for x in harmless_status:
                if response_status == x : # The http response is harmless to the functionality of the service
                    self.output['Health-Check Status'] = "Online"
                    self.result.append(self.output['Health-Check Status'])
            for y in client_error_status:
                if response_status == y: # The server cannot find anything matching the request
                    self.output['Health-Check Status'] = "Client Issue"
                    self.result.append(self.output['Health-Check Status'])
            for z in server_error_status:
                if response_status == z: # The request cannot be fulfilled due to bad syntax e.g domain validation error, missing data etc.
                    self.output['Health-Check Status'] = "Server Issue"
                    self.result.append(self.output['Health-Check Status'])
        except requests.ConnectionError: # The server encountered an unexpected condition which prevents it from fulfilling the request
            self.output['Health-Check Status'] = "Offline"
            self.result.append(self.output['Health-Check Status'])
        self.output['Last Update Time'] = now
        self.result.append(self.output['Last Update Time'])

"""
web = [
        'https://google.com',
        'https://facebook.com',
        'https://games.com',
        'https://microapi.dev',
        'https://auth.microapi.dev'
        ]


a = HandleService()
print(a.process_service_check(web))
"""