class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude, max_altitude = 0, 0
        for g in gain:
            altitude += g
            if altitude > max_altitude:
                max_altitude = altitude
        return max_altitude
