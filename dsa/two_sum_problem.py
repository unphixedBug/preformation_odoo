Two Sum Problem
Algorithm-focused 5-step method applied to a classic interview problem

Problem Statement
Given an array of integers and a target, return the indices of the two numbers that add up to the target.

Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]   → because nums[0] + nums[1] = 2 + 7 = 9
Step 1 : Restate the Problem
I'm given a list of integers and a target value.
I need to return the indices, not the values, of the two elements that sum to the target.
I can assume exactly one solution always exists.
Step 2 : Identify Edge Cases
Edge Case	Example	Expected
Fewer than 2 elements	[5], target 5	No valid pair
Same element used twice?	No - i and j must differ	i ≠ j
Duplicate values	[3, 3], target 6	[0, 1] ✅
Step 3 : Brute Force First (describe, don't code yet)
Two nested loops: for every pair (i, j), check if nums[i] + nums[j] == target.

For i from 0 to n:
    For j from i+1 to n:
        if nums[i] + nums[j] == target:
            return [i, j]
Complexity
⏱ Time	O(n²) - every pair is checked
🗂 Space	O(1) - no extra storage
Correct, but too slow for large inputs.

Step 4 : Optimize
Can a hash map help?

As we iterate, we store each value and its index in a dictionary.
For each new element, we compute complement = target - current.
If the complement is already in the map → we found the pair instantly.

seen = {}
For i, num in enumerate(nums):
    complement = target - num
    if complement is in seen:
        return [seen[complement], i]
    store num → i in seen
Complexity
⏱ Time	O(n) - single pass through the list
🗂 Space	O(n) - hash map stores at most n elements
Step 5 : Code, Test, Name Complexity
Implementation
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
Manual Trace - [2, 7, 11, 15], target = 9
i	num	complement	seen (before)	action
0	2	7	{}	store 2 → 0
1	7	2	{2: 0}	2 is in seen! → return [0, 1] ✅
Test Cases
two_sum([2, 7, 11, 15], 9)  # → [0, 1] ✅ standard case
two_sum([3, 3], 6)           # → [0, 1] ✅ duplicate values
two_sum([3, 2, 4], 6)        # → [1, 2] ✅ answer not at index 0
two_sum([1, 5, 3, 2], 4)     # → [2, 3] ✅ answer at the end
Final Complexity
Brute Force	Optimized
⏱ Time	O(n²)	O(n)
🗂 Space	O(1)	O(n)
Key Takeaway
By following the method, we naturally went from a slow O(n²) brute force to an elegant O(n) solution - without getting stuck or jumping ahead.

💡 The hash map trick: instead of looking for a pair, ask "have I already seen the complement?" - turning a double loop into a single pass.