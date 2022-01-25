#checklist.py
from django import template
register = template.Library()

@register.filter()
def check_cadastro(user):
    perms = ['cadastro.view_cliente', 'cadastro.view_fornecedor', 'cadastro.view_produto', 'cadastro.view_empresa', 'cadastro.view_transportadora', 'cadastro.view_marca', 'cadastro.view_unidade', 'cadastro.view_categoria']
    check = any(item in perms for item in user.get_all_permissions())
    print(user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_cadastro_outros(user):
    perms = ['cadastro.view_categoria', 'cadastro.view_marca', 'cadastro.view_unidade']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_vendas(user):
    perms = ['vendas.view_pedidovenda', 'vendas.view_orcamentovenda', 'vendas.view_condicaopagamento']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_compras(user):
    perms = ['compras.view_pedidocompra', 'compras.view_orcamentocompra', 'vendas.view_condicaopagamento']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_fiscal(user):
    perms = ['fiscal.view_notafiscalentrada', 'fiscal.view_notafiscalsaida', 'fiscal.view_notafiscalentrada', 'fiscal.view_notafiscalsaida', 'fiscal.configurarnfe', 'fiscal.view_naturezaoperacao', 'fiscal.view_grupofiscal''fiscal.consultar_cadastro', 'fiscal.inutilizar_notafiscal', 'fiscal.consultar_notafiscal', 'fiscal.baixar_notafiscal', 'fiscal.manifestacao_destinatario']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_nf(user):
    perms = ['fiscal.view_notafiscalentrada', 'fiscal.view_notafiscalsaida', 'fiscal.configurarnfe']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_sefaz(user):
    perms = ['fiscal.consultar_cadastro', 'fiscal.inutilizar_notafiscal', 'fiscal.consultar_notafiscal', 'fiscal.baixar_notafiscal', 'fiscal.manifestacao_destinatario']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False


@register.filter()
def check_financeiro(user):
    perms = ['financeiro.view_planocontasgrupo', 'financeiro.view_lancamento']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False


@register.filter()
def check_estoque(user):
    perms = ['estoque.consultarestoque', 'estoque.view_localestoque', 'estoque.view_movimentoestoque']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

@register.filter()
def check_movimenta_estoque(user):
    perms = ['estoque.view_movimentoestoque']
    check = any(item in perms for item in user.get_all_permissions())
    if check or user.is_superuser:
        return True
    return False

