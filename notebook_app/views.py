from main import auth, db
from flask.views import MethodView
from flask import request
from database import User, Notebook, Note


@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if user is not None and user.check_password(password):
        return user
    return 0


class RegisterNewUser(MethodView):
    @auth.login_required
    def get(self):
        return auth.current_user().to_dict()

    def post(self):
        dat = [request.form.get('email', None), request.form.get('password', None)]
        if None not in dat:
            user = User(email=dat[0], password=dat[1])
            try:
                db.session.add(user)
                db.session.commit()
            except Exception as e:
                print(e)
                return {'status': False, 'error': 'send message for admin'}
            return {'status': True}
        return {'status': False, 'error': 'incomplete data'}

    @auth.login_required
    def delete(self):
        user = auth.current_user()
        try:
            db.session.delete(user)
            db.session.commit()
            return {'status': True}
        except:
            return {'status': False, 'error': 'send message for admin'}

    @auth.login_required
    def put(self):
        user = auth.current_user()
        try:
            if request.form.get('password', None) is not None:
                user.password = user.get_hash_sha256(request.form.get('password', None))
                db.session.commit()
                return {'status': True}
        except:
            return {'status': False, 'error': 'send message for admin'}
        return {'status': False, 'error': 'incomplete data'}


class WorkWithNotebook(MethodView):
    @auth.login_required
    def get(self):
        notebook = []
        if request.form.get('name', None) is not None:
            notebook = Notebook(user=auth.current_user().id, name=request.form.get('name', None)).first().to_dict()
        else:
            for i in auth.current_user().notebook:
                notebook.append(i.to_dict())
        return {'status': True, 'notebook': notebook}

    @auth.login_required
    def post(self):
        if request.form.get('name', None) is not None:
            Notebook(user=auth.current_user().id, name=request.form.get('name', None)).add_notebook(auth.current_user())
        else:
            return {'status': False, 'error': 'Incorrect data'}
        return {'status': True}

    @auth.login_required
    def delete(self):
        if request.form.get('id', None) is not None:
            try:
                Notebook.query.get(id=int(request.form.get('id', None)))\
                    .delete_notebook(auth.current_user())
            except:
                return {'status': False, 'error': 'Incorrect data'}
        else:
            return {'status': False, 'error': 'Incorrect data'}
        return {'status': True}

    @auth.login_required
    def put(self):
        if request.form.get('id', None) is not None:
            try:
                notebook = Notebook.query.get(id=int(request.form.get('id', None)))
                notebook.name = request.form.get('name', notebook.name)
            except:
                return {'status': False, 'error': 'Incorrect data'}
        else:
            return {'status': False, 'error': 'Incorrect data'}
        return {'status': True}


class WorkWithNote:
    @auth.login_required
    def get(self):
        pass

    @auth.login_required
    def post(self):
        pass

    @auth.login_required
    def delete(self):
        pass

    @auth.login_required
    def put(self):
        pass
