from behave import fixture, use_fixture
from finlab_portfolio_ext import Manager


@fixture
def manager(context):
    context.manager = Manager()
    yield context.manager


def before_scenario(context, scenario):
    use_fixture(manager, context)
