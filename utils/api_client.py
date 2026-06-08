class APIClient:

    def __init__(self, request_context):
        self.request = request_context

    def get(self, endpoint):
        return self.request.get(endpoint)

    def post(self, endpoint, payload):
        return self.request.post(endpoint, data=payload)