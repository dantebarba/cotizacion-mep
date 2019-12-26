import time
import atexit
import cotizacion_mep.mep_api as mep_api
import cotizacion_mep.iol_mep_strategy as iol_mep_strategy
import cotizacion_mep.mongodb_mep_strategy as mongodb_mep_strategy

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
import logging


class Scheduler():

    def __init__(self, credentials={}, interval=60, bonds=[]):
        self._trigger = CronTrigger.from_crontab("*/2 11-17 * * 1-5")
        self._scheduler = BackgroundScheduler()
        self._scheduler.add_job(lambda: self.get_bonds(bonds), self._trigger)
        self._mep_api = mep_api.MEPApi(
            iol_mep_strategy.IolMEPStrategy(credentials))
        self._strategy = mongodb_mep_strategy.MongodbMepStrategy()

    def get_bonds(self, bonds_list):
        self._strategy.drop()
        for bond in bonds_list:
            self._strategy.persist_bonds(
                self._mep_api.get_bonds([bond]))
            self._strategy.persist_bonds(
                self._mep_api.get_bonds([bond+"D"]))

    def start(self):
        self._scheduler.start()


# Shut down the scheduler when exiting the app
