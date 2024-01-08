from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose, AdminIndexView
from ProjectCNPM.app import app, db, dao
from ProjectCNPM.app.models import Category, Product, User
from flask_login import logout_user, current_user
from flask import redirect, request
from ProjectCNPM.app.models import UserRoleEnum


class MyAdminIndex(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html', stats=dao.count_products_by_cate())

admin = Admin(app=app, name='Quản trị bán hàng', template_mode='bootstrap4', index_view=MyAdminIndex())

class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN

class MyCategoryView(AuthenticatedAdmin):
    column_list = ['id', 'name', 'products']

class MyProductView(AuthenticatedAdmin):
    column_list = ['id', 'name', 'price', 'active']
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    column_editable_list = ['name', 'price']
    edit_modal = True
class MyUserView(AuthenticatedAdmin):
      column_list = ['name', 'username','password','avatar']
class MyStatsView(AuthenticatedUser):
    @expose("/")
    def index(self):
        kw = request.args.get("kw")
        return self.render('admin/stats.html',
                           stats=dao.revenue_stats(kw),
                           month_stats=dao.revenue_stats_by_month())


class LogoutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()

        return redirect('/admin')

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyUserView(User, db.session))
admin.add_view(MyStatsView(name='Stats'))
admin.add_view(LogoutView(name='Đăng xuất'))
