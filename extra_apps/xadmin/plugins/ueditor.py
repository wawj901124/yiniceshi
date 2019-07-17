#使用富文本编辑器-5：建立一个xadmin插件，使用xadmin可以识别UEditorField
import xadmin
from xadmin.views import BaseAdminPlugin, CreateAdminView, ModelFormAdminView, UpdateAdminView
from DjangoUeditor.models import UEditorField
from DjangoUeditor.widgets import UEditorWidget
from django.conf import settings


class XadminUEditorWidget(UEditorWidget):   #自定义Widget，继承UEditorWidget
    def __init__(self,**kwargs):
        self.ueditor_options=kwargs   #固定写法
        self.Media.js = None    #传递一个Media，传递一个None就可以了   #固定写法
        super(XadminUEditorWidget,self).__init__(kwargs)   #固定写法

class UeditorPlugin(BaseAdminPlugin):   #新建一个UeditorPlugin，继承BaseAdminPlugin

    def get_field_style(self, attrs, db_field, style, **kwargs):  #重写get_field_style，可以在xadmin中使用 style_fields = {"detail":"ueditor"}指定风格
                                                                  #xadmin可以自动识别
        if style == 'ueditor':   #ueditor,在插件中自定义，判断风格是否等于ueditor，如果等于
            if isinstance(db_field, UEditorField):  #如果传入的field是一个UEditorField，则执行下面的代码
                widget = db_field.formfield().widget   #固定写法
                param = {}                             #固定写法
                param.update(widget.ueditor_settings)  #固定写法
                param.update(widget.attrs)              #固定写法
                return {'widget': XadminUEditorWidget(**param)}  #固定写法， XadminUEditorWidget是自定义的Widget
        return attrs

    def block_extrahead(self, context, nodes):   #重写block_extrahead，block_extrahead可以让我们在自己生成的页面中加入自己的js文件
        js = '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.config.js")         #自己的静态目录
        js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.all.min.js")   #自己的静态目录
        nodes.append(js)   #将js加入到nodes中

xadmin.site.register_plugin(UeditorPlugin, UpdateAdminView)   #注册UeditorPlugin到UpdateAdminView（修改页面）
xadmin.site.register_plugin(UeditorPlugin, CreateAdminView)   #注册UeditorPlugin到CreateAdminView（新增页面）

