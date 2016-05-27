from django.shortcuts import render
from django.contrib.auth import authenticate, login
# from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.views import login as contrib_login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .models import Contact
from actions.utils import create_action
from actions.models import Action

def register(request):
  new_user = None
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    
    if user_form.is_valid():
      new_user = user_form.save(commit=False)
      new_user.set_password(user_form.cleaned_data['password'])
      new_user.save()
      profile = Profile.objects.create(user=new_user)

      create_action(new_user, 'has created an account')
    
    return render(request, 'account/register_done.html', {'new_user': new_user})
  else:
    user_form = UserRegistrationForm()
    
  return render(request, 'account/register.html', {'user_form': user_form})

#def user_login(request):
#  if request.method == 'POST':
#   form = LoginForm(request.POST)   
#    
#    if form.is_valid():
#      cd = form.cleaned_data
#      user = authenticate(username=cd['username'], password=cd['password'])     
#      if user is not None:       
#        if user.is_active:
#          # We set the user in the session by calling the login() method and return a success message.
#          # Note the difference between authenticate and login: 
#          # authenticate() checks user credentials and returns a user object if they are right; 
#          # login() sets the user in the current session.
#          login(request, user)
#          return HttpResponse('Authenticated successfuly')
#        else:
#          return HttpResponse('Disabled Account')
#     else:
#        return HttpResponse('Invalid Login')
#  
#  else:
#    form = LoginForm()
#    
#  return render(request, 'account/login.html', {'form': form})


def login(request, **kwargs):
  ### My Code: BEGINS
    print request.user.is_authenticated
    if request.user.is_authenticated():
      return render(request, 'registration/already_authenticated.html', {'user_name': request.user.username})
    ### My Code: ENDS
    else:
      return contrib_login(request, **kwargs)

# If the user is authenticated, it executes the decorated view; if the user
# is not authenticated, it redirects him to the login URL with the URL he was trying to
# access as a GET parameter named next .
# Remember that we added a hidden input in the form of our log in template for this purpose.
@login_required
def dashboard(request):

  actions = Action.objects.exclude(user=request.user)
  following_ids = request.user.following.values_list('id', flat=True)

  if following_ids:
    actions = actions.filter(user_id__in=following_ids).select_related('user', 'user__profile').prefetch_related('target')

  actions = actions[:10]

  return render(request, 'account/dashboard.html', {'section': 'dashboard', 'actions': actions})
  
@login_required
def edit(request):
  if request.method == 'POST':
    user_form = UserEditForm(instance=request.user, data=request.POST)
    profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
    
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, 'Profile updated successfully')
    else:
      messages.error(request, 'Error updating your profile')
      
  else:
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    
  return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def user_list(request):
  users = User.objects.filter(is_active=True)

  return render(request, 'account/user/list.html', {'section': 'people', 'users': users})

@login_required
def user_detail(request, username):
  user = get_object_or_404(User, username=username, is_active=True)

  return render(request, 'account/user/detail.html', {'section': 'people', 'user': user})


@ajax_required
@require_POST
@login_required
def user_follow(request):
  user_id = request.POST.get('id')
  action = request.POST.get('action')

  if user_id and action :

    try:
      user = User.objects.get(id=user_id)

      if action == 'follow':
        Contact.objects.get_or_create(user_from=request.user, user_to=user)

        create_action(request.user, 'is following', user)

      else:
        Contact.objects.filter(user_from=request.user, user_to=user).delete()

      return JsonResponse({'status': 'ok'})

    except User.DoesNotExist:
      return JsonResponse({'status': 'ko'})

  return JsonResponse({'status': 'ko'})
  
  
  
  
  
