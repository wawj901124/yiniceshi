
PLUGINS = (
    'actions',
    'filters',
    'bookmark',
    'export',
    'layout',
    'refresh',
    'details',
    'editable',
    'relate',
    'chart',
    'ajax',
    'relfield',
    'inline',
    'topnav',
    'portal',
    'quickform',
    'wizard',
    'images',
    'auth',
    'multiselect',
    'themes',
    'aggregation',
    # 'mobile',
    'passwords',
    'sitemenu',
    'language',
    'quickfilter',
    'sortablelist',
    'importexport',
    'excel',   #添加导入excel（1.在plugins中新加excel.py文件，
                # 2.在templates/xadmin中添加excel文件夹，在excel文件夹下添加model_list.top_toolbar.import.html模板,
                #3.在要配置的adminx文件中，把import_excel = True加入，即可配置,
                #4.在在要配置的adminx文件中，重写（重载）post函数
                #5.在plugins中的__init__文件中加入excel（excel为excel.py的文件名） ）
                #Xadmin插件规则：https://xadmin.readthedocs.io/en/docs-chinese/make_plugin.html
    'ueditor',   #注册ueditor插件
)


def register_builtin_plugins(site):
    from importlib import import_module
    from django.conf import settings

    exclude_plugins = getattr(settings, 'XADMIN_EXCLUDE_PLUGINS', [])

    [import_module('xadmin.plugins.%s' % plugin) for plugin in PLUGINS if plugin not in exclude_plugins]
