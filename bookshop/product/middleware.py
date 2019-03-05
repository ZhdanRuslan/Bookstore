from .models import WebRequest


class BookShopMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_descr = f'Method: [{request.method}] Path: [{request.path}]'
        response = self.get_response(request)
        WebRequest.objects.create(req=request_descr)

        return response
