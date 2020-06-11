##################################################
##### Managing Company Settings Microservices ####
##################################################

import settings
from controller.healthservicehandler import HandleService

# Microservice URL
service_url = settings.company_server_name

class CompanySettingsService(HandleService):

    def __init__(self):
        self.create_service_url
    
    # List services
    services = [
        'set_company_name',
        'add_company',
        'delete_company'
    ]

    
    def create_service_url(self):
        count = 0
        total_service_list = len(self.services)
        while count < total_service_list:
            self.services[count] = service_url + self.services[count]
            count += 1
        return self.services