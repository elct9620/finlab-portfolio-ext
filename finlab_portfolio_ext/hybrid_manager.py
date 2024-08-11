from finlab.portfolio import PortfolioSyncManager


class HybridManager:
    def __init__(self, portfolio_manager: PortfolioSyncManager):
        self._pm = portfolio_manager

    def current_position(self):
        return self._pm.get_position()
