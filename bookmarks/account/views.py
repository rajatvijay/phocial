from django.shortcuts import render
from django.contrib.auth import authenticate, login
# from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .froms import UserRegistrationForm

def register(request):
  new_user = None
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    
    if form.is_valid:
      new_user = user_form.save(commit=False)
      new_user.set_password(user_form.cleaned_data['password'])
      new_user.save()
    
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


# If the user is authenticated, it executes the decorated view; if the user
# is not authenticated, it redirects him to the login URL with the URL he was trying to
# access as a GET parameter named next .
# Remember that we added a hidden input in the form of our log in template for this purpose.
@login_required
def dashboard(request):
  return render(request, 'account/dashboard.html', {'section': 'dashboard'})
  
  
  
  
  
  
  
