from ..callers import Caller
from .bootstrap import Bootstrap

class SummonerIdSeeder(Bootstrap):
    
    def __init__(self, output_queue=None, strategies={}, n_callers=10):
        
        super().__init__(output_queue, strategies, n_callers)
        
    def set_output_queue(self, output_queue):
        self._output_queue = output_queue
        
    def put_output_queue(self, input_value, data):
        for entry in data['entries'][:5]:
            self._output_queue.put_nowait(entry['summonerId'])
        self._data_found = True
        
    async def run(self):
        if self._output_queue is None:
            raise Exception("An output queue must be set")
        
        league_queue = Queue()
        league_queue.put_nowait("RANKED_SOLO_5x5")
        league_queue.put_nowait(None)
        
        self._callers = [Caller(self._pantheon.getMasterLeague, league_queue, callback=self.put_output_queue, strategies=self._strategies)]
        await asyncio.gather(*([c.run() for c in self._callers]))
        
        if not self._data_found:
            league_queue.put_nowait("RANKED_SOLO_5x5")
            league_queue.put_nowait(None)

            self._callers = [Caller(self._pantheon.getLeaguePages, master_league_queue, callback=self.put_output_queue, strategies=self._strategies)]
            await asyncio.gather(*([c.run() for c in self._callers]))
        
        if not self._data_found:
            raise Exception("Sorry, it seems that we couldn't find any accountId to bootstrap the queue.")