   

from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import User, Image
from .forms import UserForm, ImageForm
from django.forms import modelformset_factory

# login by user
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm

from django.contrib.auth.decorators import login_required
import uuid

    

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            user_id = form.cleaned_data['id']
            
            try:
                user = User.objects.get(name=name, id=user_id)
                # Here you might want to set the session or handle the user login as needed
                # Assuming a simple redirect for demonstration
                return redirect('user_view', pk=user.id)
            except User.DoesNotExist:
                form.add_error(None, "Invalid credentials")
    else:
        form = UserLoginForm()
    
    return render(request, 'login.html', {'form': form}) 



def logadm(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        # Add authentication logic here
        
        if authenticate(userid, password):  # Replace with actual authentication logic
            return redirect('list_users')
    return render(request, 'logadm.html')

def authenticate(userid, password):
    # Replace this with actual authentication logic
    # For now, it returns True for any non-empty userid and password
    return bool(userid) and bool(password)



def welcome(request, user_id):
    return render(request, 'welcome.html', {'user_id': user_id})

def main(request):
    return render(request, 'main.html')




def create_user_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})


def list_users_view(request):
    users = User.objects.all()
    return render(request, 'list_users.html', {'users': users})

def user_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=1)
    
    if request.method == 'POST':
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    image = form.cleaned_data.get('image')
                    img_name = form.cleaned_data.get('img_name')
                    uploaded_at = form.cleaned_data.get('uploaded_at')
                    if image and img_name:
                        Image.objects.create(user=user, image=image, img_name=img_name)
            return redirect('user_detail', pk=user.pk)
    else:
        formset = ImageFormSet(queryset=Image.objects.none())
    
    return render(request, 'user_detail.html', {'user': user, 'formset': formset})


def user_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_view.html', {'user': user})


def success(request):
    return HttpResponse('Successfully uploaded')


def logout(request):
    request.session.flush()
    return redirect('main')




# @login_required
def delete_image(request,image_id):
    image = get_object_or_404(Image, id=image_id)
    user_id = image.user.id
    image.delete()
    return redirect('user_detail', pk=user_id)

# def delete_image(request, pk):
#     contact = get_object_or_404(Image, pk=pk)
#     contact.delete()
#     return redirect('user_detail')
