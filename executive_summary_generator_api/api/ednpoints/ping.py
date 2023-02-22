from executive_summary_generator_api.service import app


@app.get("/ping")
def ping():
    """ A test endpoint that returns a test response to check if app is alive """
    return {"message": "pong"}
