from healthchecks.services.users import UserService
from healthchecks.services.sms_notifications import SmsService
from healthchecks.services.manage_pages import ManagePageService
from healthchecks.services.email_notifications import EmailService
from healthchecks.services.company_settings import CompanySettingsService
from healthchecks.services.auth import AuthService
from controller.healthservicehandler import HandleService
import threading

checker = HandleService()

def healthChecktimer():
    #threading.Timer(600.0, healthChecktimer).start()

    # Authentication Microservices Health Check
    AuthHandler = AuthService()
    AuthHandlerHealthCheck = checker.process_service_check(AuthHandler.create_service_url())

    # Managing Users Microservices Health Check
    Userhandler = UserService()
    UserhandlerHealthCheck = checker.process_service_check(Userhandler.create_service_url())

    # SMS Notifications Microservices Health Check
    SmsNotificationHandler = SmsService()
    SmsNotificationHandlerHealthCheck = checker.process_service_check(SmsNotificationHandler.create_service_url())

    # Managing Static and External Pages Microservices Health Check
    ManagePageHandler = ManagePageService()
    ManagePageHandlerHealthCheck = checker.process_service_check(ManagePageHandler.create_service_url())

    # Email Notifications Microservices Health Check
    EmailHandler = EmailService()
    EmailHandlerHealthCheck = checker.process_service_check(EmailHandler.create_service_url())

    # Managing Company Settings Microservices Health Check
    CompanyHandler = CompanySettingsService()
    CompanyHandlerHealthCheck = checker.process_service_check(CompanyHandler.create_service_url())
    
    print(UserhandlerHealthCheck, SmsNotificationHandlerHealthCheck, ManagePageHandlerHealthCheck, EmailHandlerHealthCheck, CompanyHandlerHealthCheck, AuthHandlerHealthCheck)
    
    #print(AuthHandlerHealthCheck)

healthChecktimer()

"""
def healthChecktimer():
    threading.Timer(600.0, healthChecktimer).start()
    # Managing Users Microservices Health Check
    Userhandler = UserService()
    Userhandler.create_service_url()
    UserhandlerHealthCheck = Userhandler.process_services(Userhandler.services)

    # SMS Notifications Microservices Health Check
    SmsNotificationHandler = SmsService()
    SmsNotificationHandler.create_service_url()
    SmsNotificationHandlerHealthCheck = SmsNotificationHandler.process_services(SmsNotificationHandler.services)

    # Managing Static and External Pages Microservices Health Check
    ManagePageHandler = ManagePageService()
    ManagePageHandler.create_service_url()
    ManagePageHandlerHealthCheck = ManagePageHandler.process_services(ManagePageHandler.services)

    # Email Notifications Microservices Health Check
    EmailHandler = EmailService()
    EmailHandler.create_service_url()
    EmailHandlerHealthCheck = EmailHandler.process_services(EmailHandler.services)

    # Managing Company Settings Microservices Health Check
    CompanyHandler = CompanySettingsService()
    CompanyHandler.create_service_url()
    CompanyHandlerHealthCheck = CompanyHandler.process_services(CompanyHandler.services)

    # Authentication Microservices Health Check
    AuthHandler = AuthService()
    AuthHandler.create_service_url()
    AuthHandlerHealthCheck = AuthHandler.process_services(AuthHandler.services)

    print(UserhandlerHealthCheck, SmsNotificationHandlerHealthCheck, ManagePageHandlerHealthCheck, EmailHandlerHealthCheck, CompanyHandlerHealthCheck, AuthHandlerHealthCheck)


healthChecktimer()
"""