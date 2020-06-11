#######################################
##### Authentication Microservices ####
#######################################

import settings
from controller.healthservicehandler import HandleService

# Microservice URL
service_url = settings.auth_server_name

class AuthService(HandleService):

    def __init__(self):
        self.create_service_url
    
    # List services
    services = [
        'login',
        'logout',
        'reset_password',
        'login_with_google'
    ]

    
    def create_service_url(self):
        count = 0
        total_service_list = len(self.services)
        while count < total_service_list:
            self.services[count] = service_url + self.services[count]
            count += 1
        return self.services