from django.db.models import CharField, DateTimeField, BooleanField
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.
class Client(TenantMixin):
    name = CharField(max_length=100)
    created_on = DateTimeField(auto_now_add=True)
    is_active = BooleanField(default=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

class Domain(DomainMixin):
    pass