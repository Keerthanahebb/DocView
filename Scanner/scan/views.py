# from django.shortcuts import render

# # Create your views

# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .forms import HotelForm


# from django.urls import reverse_lazy 
# # Create your views here.

# # scan/views.py
# from django.shortcuts import render, redirect
# from .models import Hotel

# from django.views.generic import ListView,CreateView

# def hotel_image_view(request):
#     if request.method == 'POST':
#         form = HotelForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("hotel")
#     else:
#         form = HotelForm()
#     return render(request, 'hotel_image_form.html', {'form': form})
#     # return render(request, 'hotel_image_form.html')


# def success(request):
#     return HttpResponse('successfully uploaded')





# class HomePageView(ListView):
#     model = Hotel
#     template_name = "hotel.html"
#     context_object_name='hotels'

# class CreatePostView(CreateView):  # new
#     model = Hotel
#     form_class = HotelForm
#     template_name = "post.html"
#     success_url = reverse_lazy("hotel")




from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import User, Image
from .forms import UserForm, ImageForm
from django.forms import modelformset_factory



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
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=5)
    if request.method == 'POST':
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if formset.is_valid():
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    Image.objects.create(user=user, image=image)
            return redirect('user_detail', pk=user.pk)
    else:
        formset = ImageFormSet(queryset=Image.objects.none())
    
    return render(request, 'user_detail.html', {'user': user, 'formset': formset})

def success(request):
    return HttpResponse('Successfully uploaded')

