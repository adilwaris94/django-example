from django import template

register =template.Library()
@register.filter(name='cut') #decorator to regist filters
def cut(value,args):

    return values.replace(args,'')

#register.filter('cut',cut) #simple way to register filter 
