from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User


class UserCodeVerification(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        code = int(request.query_params.get('code'))
        try:
            user = User.objects.get(unique_id=id)
            user_code = user.code
            if user_code == code:
                return Response({'result': True})
            else:
                user.attempt += 1
                if user.attempt == 3:
                    user.code = andom.randint(10000, 100000)
                    user.attempt = 0
                user.save()
                return Response({'result': False})
        except User.DoesNotExist:
            raise Http404
