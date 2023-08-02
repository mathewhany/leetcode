class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        parties = Counter(senate)
        skipR, skipD = 0, 0
        active = [True] * len(senate)

        i = 0
        while True:
            if active[i]: 
                if senate[i] == 'R':
                    if skipR > 0:
                        skipR -= 1
                        active[i] = False
                    else:
                        if parties['D'] == 0:
                            return 'Radiant'

                        skipD += 1
                        parties['D'] -= 1
                else:
                    if skipD > 0:
                        skipD -= 1 
                        active[i] = False                 
                    else:
                        if parties['R'] == 0:
                            return 'Dire'

                        skipR += 1
                        parties['R'] -= 1
            
            i = (i + 1) % len(senate)