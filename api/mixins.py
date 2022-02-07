from rest_framework import mixins, viewsets


class CreateObjectViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    pass
