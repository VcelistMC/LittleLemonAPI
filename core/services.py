from django.db.models import Model

def get_object_or_none(klass: Model, *args, **kwargs):
    instance = None
    try:
        instance = klass.objects.get(**kwargs)
    except klass.DoesNotExist:
        pass

    return instance