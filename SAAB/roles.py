from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_usuarios_adm': True,
        'conceder_permissoes': True,
        'remover_usuarios_adm': True,
        'mexer_no_sistema': True,
    }

class Administrador(AbstractUserRole):
    available_permissions = {
        'mexer_no_sistema': True,
    }