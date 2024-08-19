class BaseResponse:
    def get_response(self, query):
        raise NotImplementedError("Subclasses should implement this method.")
