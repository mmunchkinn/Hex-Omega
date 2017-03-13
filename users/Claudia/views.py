from users.views import *

from .add_user_form import AdminUserForm, AdminUpdateForm, PasswordForm


@login_required
def create_admin_user(request, username):
    """
    Create an admin user.
    username/add/$
    :param username:
    :param request:
    :return:
    """
    form = AdminUserForm()
    if request.method == 'POST':
        form = AdminUserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            bio = request.POST.get('bio')
            user = AdminUser.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                 email=email, password=password, bio=bio)
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, request.user)
            return redirect('display_admin', request.user.username)
    return render(request, 'users/adminuser_form.html', {'form': form})


@login_required
def get_admin_detail(request, username):
    """
    Display the information of an admin user
    :param request:
    :return:
    """
    user = AdminUser.objects.get(username__iexact=username)
    return render(request, 'users/user_information.html', {'adminuser': user})


@login_required
def update_admin_detail(request, username):
    """
    Update the information of an admin user
    :param request:
    :param username:
    :return:
    """
    user = AdminUser.objects.get(username__iexact=username)
    form_data = {'first_name': user.first_name, 'last_name': user.last_name,
                 'email': user.email, 'password': " ", 'bio': user.bio}
    form = AdminUpdateForm(request.POST, initial=form_data)
    # password_form = PasswordForm(request.POST)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            # user.username = request.POST.get('username')
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            p = request.POST['password']
            if (p is not '' or p is not None) and len(p.strip()) >= 8:
                user.set_password(p)
            user.bio = request.POST.get('bio')
            user.save()
            update_session_auth_hash(request, request.user)
            return redirect('display_admin', username)

        # if password_form.is_valid():
        #     p = request.POST.get('password')
        #     if (p is not '' or p is not None) and len(p.strip()) >= 8:
        #         user.set_password(p)
        #         user.save()
        #         update_session_auth_hash(request, request.user)

    return render(request, 'users/update_admin_form.html', {'adminuser': user, 'form': form, 'errors': form.errors})
