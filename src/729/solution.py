class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        if not len(self.intervals):
            self.intervals = [(start, end)]
            return True
        
        if start >= self.intervals[-1][1]:
            self.intervals.append((start, end))
            return True
        
        if end < self.intervals[0][0]:
            self.intervals.insert(0, (start, end))
            return True

        possible_location = self.rightmostBinarySearch(start)

        # After finding possible location, there is only one condition to check;
        # whether the end of given interval intersects with the next interval
        if self.intervals[possible_location][0] >= end:
            self.intervals.insert(possible_location, (start, end))
            return True
        
        return False

    def halfUtil(self, a: int, b: int) -> int:
        return (a+b)//2

    def rightmostBinarySearch(self, start: int) -> int:
        '''
        Finds a possible location for a new interval,
        suggesting a index after a one that's not intersecting
        with the given interval start
        '''
        min_ind, max_ind = 0, len(self.intervals)

        while min_ind < max_ind:
            mid_ind = self.halfUtil(min_ind, max_ind)

            if self.intervals[mid_ind][1] > start:
                max_ind = mid_ind
            else:
                min_ind = mid_ind + 1
        return max_ind


if __name__ == '__main__':
    obj = MyCalendar()

    print(obj.book(10, 20))
    print(obj.book(15, 25))
    print(obj.book(20, 30))

    # Should yield true, false, true