from behave import fixture, use_fixture
from finlab_portfolio_ext import HybridManager


@fixture
def manager(context):
    context.manager = HybridManager()
    yield context.manager


def before_scenario(context, scenario):
    use_fixture(manager, context)
