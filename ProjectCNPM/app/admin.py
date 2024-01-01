from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from ProjectCNPM.app import  app, db
from ProjectCNPM.app.models import Category, detail, User
from flask_login import logout_user, current_user
from flask import redirect


admin = Admin(app=app, name='Quản trị bán hàng', template_mode='bootstrap4')

class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class MyProductView(ModelView):
    column_list = ['id', 'name', 'price', 'active']
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    column_editable_list = ['name', 'price']
    edit_modal = True

class MyStatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html') #minh

class LogoutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()

        return redirect('/admin')

admin.add_view(ModelView(Category, db.session))
admin.add_view(MyProductView(detail, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(MyStatsView(name='Stats'))
admin.add_view(LogoutView(name='Đăng xuất'))