from datetime import date

from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .form import CustomUserForm
from .models import CustomUser


@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            return JsonResponse({'message': f'New user {user.id} has been registered successfully!',})
        else:
            print(form.errors)

    return JsonResponse({'message': 'OOPS! Error occured while registering a new user.'})

@csrf_exempt
def login_custom_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')

            user = authenticate(request=request,
                                username=username,
                                password=password)
            
            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return JsonResponse({
                    'message': f'Successfully logged in {username}',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                # TODO: implement some kind of notification system
                pass
        else:
            print(form.errors)

    return JsonResponse({'message': f'OOPS! Error occured while logging in.'})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_current_user(request):
    user = request.user

    if not isinstance(user, AnonymousUser):
        return JsonResponse({
            'active_login': True,
            'id': user.id,
            'username': user.username,
            'profile_picture': request.build_absolute_uri(user.profile_picture.url)
        })
    else:
        return JsonResponse({
            'active_login': False
        })