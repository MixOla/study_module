from pytest_factoryboy import register

from tests.factories import ModuleFactory

pytest_plugins = "tests.fixtures"

register(ModuleFactory)