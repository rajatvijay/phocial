from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse

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
