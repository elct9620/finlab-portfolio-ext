from behave import fixture, use_fixture
from finlab_portfolio_ext import HybridManager
from finlab.portfolio import PortfolioSyncManager


@fixture
def portfolio_manager(context):
    context.portfolio_manager = PortfolioSyncManager()
    yield context.portfolio_manager


@fixture
def manager(context):
    context.manager = HybridManager(portfolio_manager=context.portfolio_manager)
    yield context.manager


def before_scenario(context, scenario):
    use_fixture(portfolio_manager, context)
    use_fixture(manager, context)
