from django.dispatch import receiver
from django.db.models.signals import post_save
from privado.models import Usuario
from rolepermissions.roles import assign_role

@receiver(post_save, sender=Usuario)
def define_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.tipo == "A":
            assign_role(instance, 'administrador')
        elif instance.tipo == "G":
            assign_role(instance, 'gerente')
        else:
            assign_role(instance, 'gerente')
            obj = Usuario.objects.get(id = instance.id)
            obj.tipo = "G"
            obj.save()