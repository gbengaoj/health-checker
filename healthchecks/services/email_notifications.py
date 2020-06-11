############################################
##### Email Notifications Microservices ####
############################################

import settings
from controller.healthservicehandler import HandleService

# Microservice URL
service_url = settings.server_name

class EmailService(HandleService):

    def __init__(self):
        self.create_service_url
    
    # List services
    services = [
        'send_email',
        'send_email_with_template'
    ]

    
    def create_service_url(self):
        count = 0
        total_service_list = len(self.services)
        while count < total_service_list:
            self.services[count] = service_url + self.services[count]
            count += 1
        return self.services