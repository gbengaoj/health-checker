###########################################################
##### Managing Static and External Pages Microservices ####
###########################################################

import settings
from controller.healthservicehandler import HandleService

# Microservice URL
service_url = settings.pages_server_name

class ManagePageService(HandleService):

    def __init__(self):
        self.create_service_url
    
    # List services
    services = [
        'add_page',
        'retrieve_page_html',
        'set_page_markdown',
        'list_pages'
    ]

    
    def create_service_url(self):
        count = 0
        total_service_list = len(self.services)
        while count < total_service_list:
            self.services[count] = service_url + self.services[count]
            count += 1
        return self.services