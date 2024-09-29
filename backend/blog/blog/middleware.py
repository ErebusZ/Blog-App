from django.http import HttpResponseBadRequest


class HandlePostWithoutSlashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST" and not request.path.endswith("/"):
            return HttpResponseBadRequest(
                "POST requests must end with a trailing slash."
            )

        response = self.get_response(request)
        return response
