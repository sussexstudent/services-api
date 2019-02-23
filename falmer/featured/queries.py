import graphene

from falmer.schema.schema import DjangoConnectionField
from . import models
from .types import Slate


class Query(graphene.ObjectType):
    active_slate = graphene.Field(Slate)
    slate = graphene.Field(Slate, slate_id=graphene.Int())
    all_slates = DjangoConnectionField(Slate)

    def resolve_active_slate(self, info):
        return models.Slate.objects.active()

    def resolve_slate(self, info, **kwargs):
        slate_id = kwargs.get('slate_id')
        if not info.context.user.has_perm('slate.view'):
            raise PermissionError('not authorised')

        return models.Slate.objects.get(pk=slate_id)

    def resolve_all_slates(self, info):
        if not info.context.user.has_perm('slate.view'):
            raise PermissionError('not authorised')

        return models.Slate.objects.order_by('updated_at').all()
