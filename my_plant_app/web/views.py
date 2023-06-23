from django.shortcuts import render, redirect

from my_plant_app.web.form import CreateProfileForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, EditProfileForm, \
    ProfileDeleteForm
from my_plant_app.web.models import Profile, Plant


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None
# Create your views here.
def index(request):
    profile=get_profile()
    not_profile=False
    if profile==None:
        not_profile=True

    context = {
        'hide_nav_links': not_profile
    }
    return render(request, 'home-page.html', context)

def create_profile(request):
    if request.method=='GET':
        form=CreateProfileForm()
    else:
        form=CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context={
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)

def catalogue(request):
    plants=Plant.objects.all()

    context={
        'plants':plants
    }
    return render(request, 'profile/../../templates/catalogue.html', context)

def create_plant(request):
    if request.method=='GET':
        form=PlantCreateForm()
    else:
        form=PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context={
        'form': form,
    }

    return render(request, 'plant/create-plant.html', context)

def plant_details(request, pk):
    plant=Plant.objects.filter(pk=pk).get()
    context={
        'plant':plant
    }

    return render(request, 'plant/plant-details.html', context)
def edit_plant(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method=='GET':
        form=PlantEditForm(instance=plant)
    else:
        form=PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context={
        'form': form,
        'plant': plant
    }
    return render(request, 'plant/edit-plant.html', context)

def plant_delete(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'plant': plant
    }

    return render(request, 'plant/delete-plant.html', context)

def profile_details(request):
    profile = get_profile()
    stars=Plant.objects.count()
    context = {
        'profile': profile,
        'stars':stars

    }
    return render(request, 'profile/profile-details.html', context)

def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    context = {
        'form': form,
        'profile':profile
    }
    return render(request, 'profile/edit-profile.html', context)

def profile_delete(request):
    profile=get_profile()
    # if request.method == 'GET':
    #     form = ProfileDeleteForm(instance=profile)
    # else:
    #     form = ProfileDeleteForm(request.POST, instance=profile)
    #     if form.is_valid():
    if profile:
        Plant.objects.all().delete()
        profile.delete()
        return redirect('index')

    # context = {
    #     'form': form,
    #
    # }

    return render(request, 'profile/delete-profile.html')