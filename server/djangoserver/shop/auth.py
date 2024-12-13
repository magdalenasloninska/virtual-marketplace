from datetime import date

from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .form import CustomUserForm
from .models import CustomUser

@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            about = form.cleaned_data.get('about')
            profile_picture = form.cleaned_data.get('profile_picture')
            password = form.cleaned_data.get('password')

            user = CustomUser.objects.create_user(
                email=email,
                username=username,
                date_joined=date.today(),
                about=about,
                profile_picture=profile_picture,
                password=password
            )

            if user:
                return JsonResponse({
                    'success': True,
                    'message': f'New user {user.id} has been registered successfully!'
                })
        
    print(form.errors.as_json())

    return JsonResponse({
        'success': False,
        'message': 'OOPS! Error occured while registering a new user.'
    })

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
                    'success': True,
                    'message': f'Successfully logged in {username}',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': "Oops, this user doesn't exist!"
                })
        else:
            print(form.errors.as_json())

    return JsonResponse({
        'success': False,
        'message': 'Oops, an error occured while logging in!'
    })

@csrf_exempt
def logout_custom_user(request, pk):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=pk)
        logout(request)

        return JsonResponse({
            'success': True,
            'message': 'User loogged out successfully'
        })
    
    return JsonResponse({
        'success': False,
        'message': 'Oops, an error occured while logging out!'
    })

@csrf_exempt
def edit_custom_user(request, pk):
    if request.method == 'POST':
        new_about = request.POST.get('new_about')
        user = CustomUser.objects.get(id=pk)
        user.about = new_about
        user.save()

        return JsonResponse({
            'success': True,
            'message': 'Successful edit!'
        })
    
    return JsonResponse({
        'success': False,
        'message': 'Oops! Error occured during profile edit'
    })

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
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
    
    return JsonResponse({
        'active_login': False
    })