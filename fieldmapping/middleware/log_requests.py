import logging

logger = logging.getLogger(__name__)

class LogRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log request body if it's a POST request
        if request.method == "POST":
            logger.info(f'Request Body: {request.body.decode("utf-8")}')
        response = self.get_response(request)
        return response