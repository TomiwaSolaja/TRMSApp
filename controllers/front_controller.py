import imp
import employee_controller, request_controller, home_contoller

def route(app):
    employee_controller.route(app)
    home_contoller.route(app)
    request_controller.route(app)