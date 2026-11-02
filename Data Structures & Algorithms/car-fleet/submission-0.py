class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(speed))]

        cars.sort(reverse=True, key=lambda x: x[0])

        times = [(target - x[0]) / x[1] for x in cars]

        monotonic_stack = []

        for i in range (len(times)):
            time = times[i]

            if (monotonic_stack and time <= monotonic_stack[-1]):
                continue
            else:
                monotonic_stack.append(time)


        return len(monotonic_stack)

        