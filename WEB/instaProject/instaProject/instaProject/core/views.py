from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage


@login_required
def home(request):
    return render(request, 'core/home.html')


def profile(request):
    if request.method == 'POST' and request.FILES['profile_picture']:
        myfile = request.FILES['profile_picture']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/profile.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/profile.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('timeline:index')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})
