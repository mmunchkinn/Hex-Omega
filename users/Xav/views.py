from users.views import *

from .add_leader_form import *


def create_leader_user(request, username):
    form = LeaderForm()
    if request.method == 'POST':
        form = LeaderForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = get_default_password()
            user = LeaderUser.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                  email=email, password=password)
            user.set_password(password)
            send_default_password(user, password)
            user.save()
            update_session_auth_hash(request, request.user)
            return redirect('display_leader', request.user.username)
    return render(request, 'users/leaderuser_form.html', {'form': form})


def display_leader_detail(request, username):
    user = LeaderUser.objects.get(username__iexact=username)
    return render(request, 'users/leaderdetail.html', {'leaderuser': user})


def update_leader_detail(request, username):
    user = LeaderUser.objects.get(username__iexact=username)
    form_data = {'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name,
                 'email': user.email,
                 'password': user.password, 'bio': user.bio}
    form = UpdateLeaderForm(request.POST, initial=form_data)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            pw = request.POST['password']
            if (pw is not '' or pw is not None) and len(pw.strip()) >= 8:
                user.set_password(pw)
            user.bio = request.POST.get('bio')
            user.save()
            update_session_auth_hash(request, request.user)
            return redirect('display_leader', username)

    return render(request, 'users/update_leader_form.html', {'leaderuser': user, 'form': form, 'errors': form.errors})
