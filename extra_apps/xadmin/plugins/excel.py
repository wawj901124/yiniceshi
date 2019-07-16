# coding:utf-8

import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from django.template import loader  #导入loader，加载渲染
from xadmin.plugins.utils import get_context_dict   #导入get_context_dict，将context转换为一个字典


#excel 导入
class ListImportExcelPlugin(BaseAdminPlugin):   #自定义一个plugin,继承BaseAdminPlugin
    import_excel = False   #设置默认值为False，就是不加载该插件，import_excel为变量的名称，可以自己随便定义

    def init_request(self, *args, **kwargs):   #重写init_request函数，init_request为整个插件的入口函数，只有返回True的时候，才会加载插件
        return bool(self.import_excel)   #返回一个True或False，如果是True，就加载这个插件，如果为False，就不加载

    def block_top_toolbar(self, context, nodes):  #问题解决网址：https://blog.csdn.net/daniel_qinzhao/article/details/89212063
        context = get_context_dict(context or {})  # 用此方法来转换,转换成字典形式的内容
        nodes.append(loader.render_to_string('xadmin/excel/model_list.top_toolbar.import.html', context=context))  #重载这个函数，就可以重载导入的html文件，写法固定
        #使用nodes添加，使用loader方法加载模板（自定义的模板model_list.top_toolbar.import.html），查找的默认路径是从xadmin\templates下开始查找的，
        #xadmin/excel/model_list.top_toolbar.import.html实际为相对路径，绝对路径为xadmin/templates/xadmin/excel/model_list.top_toolbar.import.html，
        #model_list：表示列表页，top_toolbar：就是“导出”所在的那个区域，import：就是import导入文件，
        #model_list.top_toolbar.import.html：是自己写的内容，


xadmin.site.register_plugin(ListImportExcelPlugin, ListAdminView)    #注册插件ListImportExcelPlugin到ListAdminView中