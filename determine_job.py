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
        
        self.base_benchmarks = np.array([71, 82, 75, 74, 73, 71])

        self.benchmarks = {
            'Physical Sweeper': self.create_benchmark([0, 110, 0, 0, 0, 101]),  
            'Special Sweeper': self.create_benchmark([0, 0, 0, 110, 0, 101]),
            'Mixed Sweeper': self.create_benchmark([0, 100, 0, 100, 0, 101]),
            'Physical Tank': self.create_benchmark([95, 0, 110, 0, 0, 0]),
            'Special Tank': self.create_benchmark([95, 0, 0, 0, 110, 0]),
            'Wall': self.create_benchmark([100, 0, 110, 0, 110, 0]),
            'Jack-Of-All-Trades': self.create_benchmark([95, 95, 95, 95, 95, 95])
        }

    def create_benchmark(self, mask):
        return np.where(np.array(mask) == 0, self.base_benchmarks, np.array(mask))
    
    def get_jobs_primary(self, stats):
        best = self._best_stat_role(stats)
        return best

    def get_jobs_secondary(self, moveset):
        moves = self._move_roles(moveset)
        return moves

    def _best_stat_role(self, stats):
        best_role = None
        lowest_variance = float('inf')
        for role, bench in self.benchmarks.items():
            score = self._score(stats, bench)
            variance = np.var(score)
            if variance < lowest_variance:
                lowest_variance = variance
                best_role = role
        return best_role

    def _score(self, stats, bench):
        array = np.array(stats)
        array = np.where(bench == 0, 1, array)
        bench = np.where(bench == 0, 1, bench)
        ratios = array / bench
        return ratios

    def _move_roles(self, moveset):
        roles = []
        
        moves = [move.strip() for move in moveset.split(',')]
        for role, move_list in self.move_roles.items():
            if any(move in moves for move in move_list):
                roles.append(jobs[role].value)
        return roles



def main():
    x = DetermineJob()
    print(x.benchmarks)
    print(x.get_jobs_primary([50,50,50,50,50,50]))
        
if __name__ == "__main__":
    main()
