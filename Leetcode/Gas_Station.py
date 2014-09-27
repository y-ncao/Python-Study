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
        start_node = 0
        total_gas = 0
        cur_gas = 0
        for i in range(N):
            total_gas += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]
            if cur_gas < 0:
                start_node = i + 1
                cur_gas = 0
        if total_gas < 0:
            return -1
        else:
            return start_node
        # Note:
        # 1. Notice line 18 for start node and line 30 for return
