

def route(app):
    @app.route("/")
    def hello():
        return "Hello, World!"