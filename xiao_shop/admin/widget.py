from django.forms.widgets import Textarea

class WangEditorWidget(Textarea):
    template_name = 'xiao_shop/widgets/wangeditor.html'

    class Media:
        css = {
            'all': ('xiao_shop/css/wangeditor.css',)
        }
        js = (
            'admin/js/vendor/jquery/jquery.min.js',
            'xiao_shop/js/wangeditor/editor.js'
        )