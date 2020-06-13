from flask import Flask, render_template, request

from script.healthservicehandler import HandleService


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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')