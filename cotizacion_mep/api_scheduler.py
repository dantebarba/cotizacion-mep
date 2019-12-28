import time
import cotizacion_mep.mep_api as mep_api
import cotizacion_mep.iol_mep_strategy as iol_mep_strategy
import cotizacion_mep.mep_api_strategy as mep_api_strategy
import cotizacion_mep.mongodb_mep_strategy as mongodb_mep_strategy

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
import logging


class SchedulerStrategy(mep_api_strategy.MEPApiStrategy):

    def __init__(self, credentials={}, bonds=[], cron="*/1 11-17 * * 1-5"):
        self._trigger = CronTrigger.from_crontab(cron)
        self._scheduler = BackgroundScheduler()
        self._scheduler.add_job(
            lambda: self.persist_bonds(bonds), self._trigger)
        self._iol_strategy = iol_mep_strategy.IolMEPStrategy(credentials)
        self._strategy = mongodb_mep_strategy.MongodbMepStrategy()
        self.start()

    def persist_bonds(self, bonds_list):
        self._strategy.drop()
        for bond in bonds_list:
            self._strategy.persist_bonds(
                self._iol_strategy.get_bonds([bond]))
            self._strategy.persist_bonds(
                self._iol_strategy.get_bonds([bond+"D"]))

    def get_bonds(self, bonds_list):
        return self._strategy.get_bonds(bonds_list)

    def start(self):
        # first data load
        self._scheduler.start()
