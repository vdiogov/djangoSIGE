#checklist.py
from django import template
register = template.Library()

@register.filter()
def check_cadastro(user):
    perms = ['cadastro.view_cliente', 'cadastro.view_fornecedor', 'cadastro.view_produto', 'cadastro.view_empresa', 'cadastro.view_transportadora', 'unidade', 'marca', 'cadastro.view_categoria']
    check = any(item in perms for item in user.get_all_permissions())
    print(user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_cadastro_outros(user):
    perms = ['cadastro.view_categoria', 'unidade', 'marca']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_vendas(user):
    perms = ['condicaopagamento', 'pedidovenda', 'orcamentovenda']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_compras(user):
    perms = ['orcamentocompra', 'pedidocompra', 'condicaopagamento']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_fiscal(user):
    perms = ['notafiscalsaida', 'notafiscalentrada', 'configurar_nfe','consultar_cadastro', 'inutilizar_notafiscal', 'consultar_notafiscal', 'naturezaoperacao', 'grupofiscal']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_nf(user):
    perms = ['notafiscalsaida', 'notafiscalentrada', 'configurar_nfe']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_sefaz(user):
    perms = ['consultar_cadastro', 'inutilizar_notafiscal', 'consultar_notafiscal']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False


@register.filter()
def check_financeiro(user):
    perms = ['planocontasgrupo', 'acesso_fluxodecaixa', 'lancamento', 'all_entradas', 'all_contasreceber','all_contaspagar']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_fin_entradas(user):
    perms = ['all_entradas', 'all_contasreceber']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False
    
@register.filter()
def check_fin_saidas(user):
    perms = ['all_contasreceber', 'all_contaspagar']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_estoque(user):
    perms = ['consultar_estoque', 'localestoque', 'movimentoestoque','all_entradas', 'all_saidas', 'all_transferencias' ]
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_movimenta_estoque(user):
    perms = ['movimentoestoque', 'all_entradas', 'all_saidas', 'all_transferencias' ]
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

