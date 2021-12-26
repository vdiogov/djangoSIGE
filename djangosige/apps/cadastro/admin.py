from django.contrib import admin
from .models import Empresa, MinhaEmpresa


class MinhaEmpresaConfig(admin.ModelAdmin):
    verbose_name = 'Usuarios e Empresas'
    list_display = ('empresa_usuario','minha_empresa')
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
        # All model fields as read_only
            return self.readonly_fields + tuple(['m_usuario'])
        return self.readonly_fields
    #readonly_fields=['m_usuario']
    ordering = ('m_usuario','m_empresa')

    def empresa_usuario(self, obj):
        return obj.m_usuario

    def minha_empresa(self, obj):
        return obj.m_empresa

    empresa_usuario.admin_order_field  = 'm_usuario'  #Allows column order sorting
    empresa_usuario.short_description = 'Usuario'  #Renames column head

    minha_empresa.admin_order_field  = 'm_empresa'  #Allows column order sorting
    minha_empresa.short_description = 'Empresa'  #Renames column head

admin.site.register(Empresa)
admin.site.register(MinhaEmpresa, MinhaEmpresaConfig)