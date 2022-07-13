from app.decorators.auth_required import auth_required
from app.services.user_service import UserService
from app import app
from flask import redirect, render_template, request, session, url_for, jsonify
from app.forms.UserRegisterForm import UserRegisterForm
from app.forms.UserLoginForm import UserLoginForm
from app.forms.UserUpdateForm import UserUpdateForm

userService = UserService()

# http://localhost:8080/users -> GET
@app.route('/users')
def getUserList():
    return render_template('users/list.html', users=userService.find_all())

# http://localhost:8080/users/5 -> GET
@app.route('/users/<int:userid>', methods=["GET"])
def getOneUser(userid: int):
    user = userService.find_one(userid)

    return render_template('users/profile.html', user=user)

# http://localhost:8080/users/register -> GET | POST
@app.route('/users/register', methods=["GET", "POST"])
def register():
    form = UserRegisterForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = userService.insert(form.getAsUser())

            return redirect(url_for('getOneUser', userid=user.userid))

    return render_template('users/register.html', form=form)


@app.route('/users/update/<int:userid>', methods=["GET", "POST"])
@auth_required(level="ADMIN", or_is_current_user=True)
def userUpdate(userid: int):
    form = UserUpdateForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = userService.update(userid, form.getAsUser())

            return redirect(url_for('getOneUser', userid=userid))

    user = userService.find_one(userid)
    return render_template('users/update.html', form=form, user=user)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = UserLoginForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = userService.login(form.getAsUser())

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
def logout():
    session.pop('userid', None)
    session.pop('username', None)
    session.pop('userroles', None)
    return redirect(url_for('index'))


@app.route('/profile', methods=["GET"])
@auth_required()
def profile():
    userid = session.get('userid')

    return redirect(url_for('getOneUser', userid=userid))

