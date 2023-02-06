from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleWare(MiddlewareMixin):
    """ 中间件 """

    def process_request(self, request):
        if request.path_info in ["/login/", "/image/code/"]:
            return
        info_dict = request.session.get("info")
        # print(info_dict)
        if info_dict:
            return
        return redirect('/login/')

