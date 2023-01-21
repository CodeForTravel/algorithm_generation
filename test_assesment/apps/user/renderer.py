from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class ApiRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response: Response = renderer_context["response"]
        is_success = status.is_success(response.status_code)
        if is_success:
            response_data = {
                "success": status.is_success(response.status_code),
                "data": data
            }
        else:
            response_data = {
                "success": status.is_success(response.status_code),
                "error": data
            }
        return super().render(response_data, accepted_media_type, renderer_context)
