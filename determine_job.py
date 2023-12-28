import numpy as np
from poke_jobs import jobs

class DetermineJob:
    def __init__(self):
        self.move_roles = {
            'hazer': ["haze"],
            'pseudo_hazer': ["perish song", "leech seed", "roar", "whirlwind", "dragon tail"],
            'cleric': ["heal bell", "aromatherapy"],
            'staller': ["toxic", "protect", "leech seed", "will-o-wisp", "confuse ray", "pain Split", 
                        "giga Drain", "recover", "soft-boiled", "moonlight", "synthesis", "roost"],
            'spiker': ["spikes", "toxic spikes", "stealth rock"],
            'baton_pass': ["baton pass"],
            'toxi_shufflers': ["toxic", "roar", "whirlwind"],
            'para_shufflers': ["thunder wave", "roar", "whirlwind"],
            'pivots': ["u-turn", "volt switch"]
        }

        self.benchmarks = {
            'Physical Sweeper': np.array([0, 120, 0, 0, 0, 101]),  
            'Special Sweeper': np.array([0, 0, 0, 115, 0, 101]),
            'Mixed Sweeper': np.array([0, 100, 0, 105, 0, 101]),
            'Physical Tank': np.array([95, 0, 120, 0, 0, 0]),
            'Special Tank': np.array([95, 0, 0, 0, 120, 0]),
            'Wall': np.array([100, 0, 120, 0, 120, 0]),
            'Jack-Of-All-Trades': np.array([90, 90, 90, 90, 90, 90])
        }

    def get_jobs_primary(self, stats):
        best = self._best_stat_role(stats)
        return best

    def get_jobs_secondary(self, moveset):
        moves = self._move_roles(moveset)
        return moves

    def _best_stat_role(self, stats):
        best_role = None
        high = 0
        for role, bench in self.benchmarks.items():
            score = self._score(stats, bench)
            if score > high:
                high = score
                best_role = role
        return best_role

    def _score(self, stats, bench):
        array = np.array(stats)
        array = np.where(bench == 0, 1, array)
        bench = np.where(bench == 0, 1, bench)
        ratios = array / bench
        return np.sum(ratios)

    def _move_roles(self, moveset):
        roles = []
        
        moves = [move.strip() for move in moveset.split(',')]
        for role, move_list in self.move_roles.items():
            if any(move in moves for move in move_list):
                roles.append(jobs[role].value)
        return roles



x = DetermineJob()

print(x.get_jobs_primary([95,95,95,95,95,95]))
        
