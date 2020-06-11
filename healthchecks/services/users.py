#######################################
##### Managing Users Microservices ####
#######################################

import settings
from controller.healthservicehandler import HandleService

# Microservice URL
service_url = settings.server_name

class UserService(HandleService):

    def __init__(self):
        self.create_service_url
    
    # List services
    services = [
        'add_user',
        'remove_user',
        'set_user_first_name',
        'set_user_last_name',
        'change_user_email',
        'set_user_phone',
        'get_user_first_name'
    ]

    
    def create_service_url(self):
        count = 0
        total_service_list = len(self.services)
        while count < total_service_list:
            self.services[count] = service_url + self.services[count]
            count += 1
        return self.services



