import factory

from modules.models import Module


class ModuleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Module

    number = factory.Faker("sentence", nb_words=3)
    title = factory.Faker("sentence", nb_words=5)
    description = factory.Faker("sentence", nb_words=15)