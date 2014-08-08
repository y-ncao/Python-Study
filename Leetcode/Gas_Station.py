"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        N = len(gas)
        diff = []
        for i in range(N):
            diff.append(gas[i]-cost[i])
        sum = 0
        start_node = 0
        left_gas = 0
        for i in range(0, N):
            left_gas += diff[i]
            sum += diff[i]
            if sum < 0:
                start_node = i+1
                sum = 0
        if left_gas < 0:
            return -1
        else:
            return start_node
