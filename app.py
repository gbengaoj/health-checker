from flask import Flask, render_template, request
#from flask_restful import Resource, Api
#from json import dumps
import requests

from controller.healthservicehandler import HandleService

#from healthchecks.services.users import UserService
#from healthchecks.services.sms_notifications import SmsService
#from healthchecks.services.manage_pages import ManagePageService
#from healthchecks.services.email_notifications import EmailService
#from healthchecks.services.company_settings import CompanySettingsService
#from healthchecks.services.auth import AuthService
#import threading


app = Flask(__name__)


@app.route("/", methods=['GET','POST'])

def healthChecktimer():
    #threading.Timer(600.0, healthChecktimer).start()


    if request.method == 'POST':
        checker = HandleService()
        
        microservice = request.form.get('idon')

        return '''  <!DOCTYPE html>
                    <html lang="en" dir="ltr">
                        <head>
                            <meta charset="utf-8">
                            <title>Health Check Service</title>
                        </head>
                        <body style="text-align:center;">
                            <div style='background-color:black;'>
                                <h1 style='color:white; padding-top:10px; padding-bottom:10px'>DASHBOARD FOR MONITORING API HEALTH</h1>
                            </div>
                                <h1>{}</h1>
                        </body>
                    </html>'''.format(checker.process_service_check(microservice))

    return      '''<!DOCTYPE html>
                <html lang="en" dir="ltr">
                    <head>
                        <meta charset="utf-8">
                        <title>Health Check Service</title>
                    </head>
                    <body style="text-align:center;">
                        <div style='background-color:black'>
                            <h1 style='color:white; padding-top:10px; padding-bottom:10px'>DASHBOARD FOR MONITORING API HEALTH</h1>
                        </div>
                        <form method="POST" style='padding-top:20px'>
                            Service Url: <input type="url" name="idon"><br>
                            <div style='padding-top:40px; padding-left:70px;'>
                            <input type="submit" value="Submit"><br>
                            </div>
                        </form>
                    </body>
                </html>'''




        
        #return '''<h1>The language value is: {}</h1>
                  #<h1>The framework value is: {}</h1>'''.format(language, framework)



    
    """
    #print(AuthHandlerHealthCheck, UserhandlerHealthCheck)

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
    
    services_status = (UserhandlerHealthCheck, SmsNotificationHandlerHealthCheck, ManagePageHandlerHealthCheck, EmailHandlerHealthCheck, CompanyHandlerHealthCheck, AuthHandlerHealthCheck)
    for services in services_status:
        print(services)
    #print(AuthHandlerHealthCheck, UserhandlerHealthCheck)

    healthChecktimer()
    """


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')