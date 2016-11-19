# Author:Alex Li
from django.shortcuts import HttpResponse
class M1:
    def process_request(self, request):
        print('M1.process_request')
        # return HttpResponse('滚')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('m1.process_view')

    def process_exception(self, request, exception):
        print('m1.process_exception')

    def process_response(self, request, response):
        print('M1.process_response')
        return response

    def process_template_response(self,request,response):
        print('template')


class M2:
    def process_request(self, request):
        print('M2.process_request')
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('m2.process_view')
    def process_exception(self, request, exception):
        print('m2.process_exception')

    def process_response(self, request, response):
        print('M2.process_response')
        return response