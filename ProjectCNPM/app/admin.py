from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from ProjectCNPM.app import  app, db
from ProjectCNPM.app.models import Category, detail

admin = Admin(app=app, name='Quản trị bán hàng', template_mode='bootstrap4')

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
admin.add_view(ModelView(Category, db.session))
admin.add_view(MyProductView(detail, db.session))
admin.add_view(MyStatsView(name='Thông kê báo cáo'))
