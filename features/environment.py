from behave import fixture, use_fixture
from finlab_portfolio_ext import CustomPositionManager


@fixture
def manager(context):
    context.manager = CustomPositionManager()
    yield context.manager


def before_scenario(context, scenario):
    use_fixture(manager, context)
