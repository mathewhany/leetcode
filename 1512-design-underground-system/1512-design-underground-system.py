class UndergroundSystem:

    def __init__(self):
        self.ids = {}
        self.times = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInTime, startStation = self.ids[id]
        del self.ids[id]
        self.times[(startStation, stationName)].append(t - checkInTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.times[(startStation, endStation)]

        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)