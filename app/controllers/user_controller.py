from app.framework.decorators.auth_required import auth_required
from app.framework.decorators.inject import inject
from app.services.auth_service import AuthService
from app.services.role_service import RoleService
from app.services.user_service import UserService
from app import app
from flask import redirect, render_template, request, session, url_for, jsonify
from app.forms.user.user_register_form import UserRegisterForm
from app.forms.user.user_login_form import UserLoginForm
from app.forms.user.user_update_form import UserUpdateForm


# http://localhost:8080/users -> GET
@app.route('/users')
@inject
def getUserList(userService: UserService):
    form = UserRegisterForm()

    return render_template('users/list.html', users=userService.find_all(), form=form)

@app.route('/api/users')
@inject
def getUsersAsJson(user_service: UserService):
    return jsonify([user.get_json_parsable() for user in user_service.find_all()])

# http://localhost:8080/users/5 -> GET
@app.route('/users/<int:userid>', methods=["GET"])
@auth_required()
@inject
def getOneUser(userid: int, userService: UserService):
    user = userService.find_one(userid)

    return render_template('users/profile.html', user=user)

# http://localhost:8080/users/register -> GET | POST
@app.route('/users/register', methods=["GET", "POST"])
@inject
def register(userService: UserService):
    form = UserRegisterForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = userService.insert(form)

            return redirect(url_for('getOneUser', userid=user.userid))

    return render_template('users/register.html', form=form)


@app.route('/users/update/<int:userid>', methods=["GET", "POST"])
@auth_required(level="ADMIN", or_is_current_user=True)
@inject
def userUpdate(userid: int, userService: UserService, roleService: RoleService):
    form = UserUpdateForm(request.form)
    roles = roleService.find_all()

    if request.method == 'POST':
        if form.validate():
            user = userService.update(userid, form)

            return redirect(url_for('getOneUser', userid=userid))

    user = userService.find_one(userid)
    return render_template('users/update.html', form=form, user=user, roles=roles)


@app.route('/login', methods=["GET", "POST"])
@inject
def login(userService: UserService):
    form = UserLoginForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = userService.login(form)

            if user != None:
                session['username'] = user.username
                session['userid'] = user.userid
                session['userroles'] = user.get_roles()
                return redirect(url_for('getOneUser', userid=user.userid))

            errors = {}
            errors['authentication'] = 'Wrong user or password!'

            return render_template('users/login.html', form=form, errors=errors)

    return render_template('users/login.html', form=form, errors=form.errors)


@app.route('/logout', methods=["GET"])
@inject
def logout():
    session.pop('userid', None)
    session.pop('username', None)
    session.pop('userroles', None)
    return redirect(url_for('index'))


@app.route('/profile', methods=["GET"])
@auth_required()
@inject
def profile(authService: AuthService):
    userid = authService.get_current_user().userid

    return redirect(url_for('getOneUser', userid=userid))

