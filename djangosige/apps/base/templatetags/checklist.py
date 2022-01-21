#checklist.py
from django import template
register = template.Library()

@register.filter()
def check_cadastro(user):
    perms = ['cliente', 'fornecedor', 'produto', 'empresa', 'transportadora', 'unidade', 'marca', 'categoria']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False