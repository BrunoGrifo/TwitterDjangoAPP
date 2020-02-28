from django.http import JsonResponse

class JsonResponseAjaxSuccess(JsonResponse):
    def __init__(self):
        super().__init__({"success": True})

class JsonResponseBadRequest(JsonResponse):
    status_code = 400
    def __init__(self, content=''):
        super().__init__({"error": content})