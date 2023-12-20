from django.shortcuts import render, redirect
from . models import User, Campaign
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'index.html')

def register(request):
    if 'email_error' in request.session:
        del request.session['email_error']
    results = User.objects.filter(email = request.POST['email'])
    if len(results) > 0:
        request.session['email_error'] = 'Please use a different email'
        return redirect("/")
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.add({
            'username' : request.POST['username'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            'confirm': request.POST['confirm']
        })
        request.session['user_id'] = user.id
    return redirect("/dashboard",)

def login(request):
    if 'email_error' in request.session:
        del request.session['email_error']
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect("/dashboard")
    request.session['email_error'] = 'Invalid login'
    return redirect("/")

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user' : User.get_by_id(request.session['user_id']),
        'campaigns' : User.get_by_id(request.session['user_id']).campaigns
    }
    return render(request, 'dashboard.html', context)

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')

def create_new_character(request):
    pass

def create_character(request):
    pass

def edit_character(request):
    pass

def update_character(request):
    pass

def delete_character(request):
    pass

def show_character(request):
    pass

def show_public_characters(request):
    pass

def create_new_campaign(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user' : User.get_by_id(request.session['user_id'])
    }
    return render(request, 'create_campaign.html', context)

def create_campaign(request):
    errors = Campaign.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/create/new/campaign')
    campaign = {
        'name' : request.POST['name'],
        'description' : request.POST['description'],
        'homebrew_allowed' : request.POST['homebrew_allowed'],
        'public' : request.POST['public'],
        'location' : request.POST['location'],
        'online' : request.POST['online'],
        'creator' : User.get_by_id(request.session['user_id'])
    }
    Campaign.add(campaign)
    return redirect('/dashboard')

def edit_campaign(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'campaign' : Campaign.get_by_id(id)
    }
    return render(request, 'edit_campaign.html', context)

def update_campaign(request):
    data = {
        'id' : request.POST['campaign_id'],
        'name' : request.POST['name'],
        'description' : request.POST['description'],
        'homebrew_allowed' : request.POST['homebrew_allowed'],
        'public' : request.POST['public'],
        'location' : request.POST['location'],
        'online' : request.POST['online'],
    }
    Campaign.update(data)
    return redirect('/dashboard')

def delete_campaign(request, id):
    Campaign.destroy(id)
    return redirect('/dashboard')

def show_campaign(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'campaign' : Campaign.get_by_id(id)
    }
    return render(request, 'show_campaign.html', context)

def show_public_campaigns(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'campaigns' : Campaign.objects.all()
    }
    return render(request, 'show_public_campaigns.html', context)

def create_new_dnd_class(request):
    pass

def create_dnd_class(request):
    pass

def edit_dnd_class(request):
    pass

def update_dnd_class(request):
    pass

def delete_dnd_class(request):
    pass

def show_dnd_class(request):
    pass

def show_public_dnd_classes(request):
    pass

def create_new_spell(request):
    pass

def create_spell(request):
    pass

def edit_spell(request):
    pass

def update_spell(request):
    pass

def delete_spell(request):
    pass

def show_spell(request):
    pass

def show_public_spells(request):
    pass

def create_new_skill(request):
    pass

def create_skill(request):
    pass

def edit_skill(request):
    pass

def update_skill(request):
    pass

def delete_skill(request):
    pass

def show_skill(request):
    pass

def create_new_feat(request):
    pass

def create_feat(request):
    pass

def edit_feat(request):
    pass

def update_feat(request):
    pass

def delete_feat(request):
    pass

def show_feat(request):
    pass

def show_public_feats(request):
    pass

def create_new_feature(request):
    pass

def create_feature(request):
    pass

def edit_feature(request):
    pass

def update_feature(request):
    pass

def delete_feature(request):
    pass

def show_feature(request):
    pass

def create_new_background(request):
    pass

def create_background(request):
    pass

def edit_background(request):
    pass

def update_background(request):
    pass

def delete_background(request):
    pass

def show_background(request):
    pass

def show_public_backgrounds(request):
    pass

def create_new_race(request):
    pass

def create_race(request):
    pass

def edit_race(request):
    pass

def update_race(request):
    pass

def delete_race(request):
    pass

def show_race(request):
    pass

def show_public_races(request):
    pass

def create_new_item(request):
    pass

def create_item(request):
    pass

def edit_item(request):
    pass

def update_item(request):
    pass

def delete_item(request):
    pass

def show_item(request):
    pass

def show_public_items(request):
    pass