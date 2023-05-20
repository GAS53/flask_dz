from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_login import current_user
from flask_admin import Admin, AdminIndexView, expose

from models.database import db
from models.tags import Tag
from models.article import Article
from models.user import User


class CustomView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff
    
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("auth_app.login"))

class TagAdminView(CustomView):
    column_searchable_list = ("name",)
    column_filters = ("name",)
    can_export = True
    export_types = ["csv", "xlsx"]
    create_modal = True
    edit_modal = True


class UserAdminView(CustomView):
    column_exclude_list = ("pswd",)
    column_searchable_list = ("first_name", "last_name", "login", "is_staff", "email")
    column_filters = ("first_name", "last_name", "login", "is_staff", "email")
    column_editable_list = ("first_name", "last_name", "is_staff")
    can_create = True
    can_edit = True
    can_delete = False


class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for("auth.login"))
        return super(MyAdminIndexView, self).index()


admin = Admin(name='Admin aa', base_template='admin/index.html', endpoint='admin', url='/admin',  index_view=MyAdminIndexView(), template_mode='bootstrap4')
admin.add_view(UserAdminView(User,   db.session, name='user aa', category="Models"))
admin.add_view(TagAdminView(Tag, db.session, name='tags aa', category='Models'))
