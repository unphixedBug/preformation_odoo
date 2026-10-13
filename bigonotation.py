# ============================================================
#  BIG O COMPLEXITY EXERCISES
#  For each function below:
#    1. Analyze the code
#    2. State the TIME complexity and explain why
#    3. State the SPACE complexity and explain why
# ============================================================
#
#  QUICK REMINDER OF THE 4 STEPS:
#    Step 1 - Count the loops         → one loop = O(n), nested = O(n²)
#    Step 2 - Look for halvings       → mid = (lo + hi) // 2 = O(log n)
#    Step 3 - Look for recursive calls → calls per level × number of levels = O(n)
#    Step 4 - Identify auxiliary structures → new list/dict = O(n) space
#
#  RULE: always state both TIME and SPACE before moving on.
# ============================================================

# ────────────────────────────────────────────────────────────
#  LEVEL 1 - Pure loops (Step 1)
# ────────────────────────────────────────────────────────────

# ── Exercise 1 ──────────────────────────────────────────────
#
#  Time  → O(n)
#  Space → O(1)
#  Why? => time dépend d'une seule boucle, space quasi rien car uniquement assignations de base
#
def sum_list(arr):
    total = 0
    for x in arr:
        total += x
    return total


# ── Exercise 2 ──────────────────────────────────────────────
#
#  Time  → O(n2)
#  Space → O(1)
#  Why? => time dépend de deux boucles, space quasi rien car uniquement assignations de base
#
#  HINT: Are both loops iterating over the same thing?
#
def find_pair(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False


# ────────────────────────────────────────────────────────────
#  LEVEL 2 - Halvings (Step 2)
# ────────────────────────────────────────────────────────────

# ── Exercise 3 ──────────────────────────────────────────────
#
#  Time  → O(n)
#  Space → O(n2)
#  Why?
#
#  HINT: What happens to the search space at each iteration?
#
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# ────────────────────────────────────────────────────────────
#  LEVEL 2 - Loops + auxiliary structures (Steps 1 + 4)
# ────────────────────────────────────────────────────────────

# ── Exercise 4 ──────────────────────────────────────────────
#
#  Time  → O( ? )
#  Space → O( ? )
#  Why?
#
#  HINT: Don't forget to look at ALL structures created, not just the loop.
#
def count_occurrences(arr):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    return counts


# ────────────────────────────────────────────────────────────
#  LEVEL 3 - Recognizing recursive calls (Step 3)
# ────────────────────────────────────────────────────────────

# ── Exercise 5 ──────────────────────────────────────────────
#
#  Time  → O( ? )
#  Space → O( ? )
#  Why?
#
#  HINT: How many times does the function call itself?
#        What happens on the call stack while it runs?
#
def countdown(n):
    if n == 0:
        print("Done")
        return
    print(n)
    countdown(n - 1)


# ────────────────────────────────────────────────────────────
#  BONUS - The trap exercise (apply the RULE)
# ────────────────────────────────────────────────────────────

# ── Exercise 6 ──────────────────────────────────────────────
#
#  A developer says: "there's a loop, so O(n) time and O(1) space."
#  Are they right? Justify your answer.
#
#  Time  → O( ? )
#  Space → O( ? )
#  Why?
#
def process(arr):
    result = []
    for x in arr:
        if x % 2 == 0:
            result.append(x * 2)
    return result


# ============================================================
#  SUMMARY TABLE - fill this in once you're done
#
#  Exercise | Time     | Space  | Key step
#  ---------|----------|--------|----------------------------
#  Ex 1     |          |        |
#  Ex 2     |          |        |
#  Ex 3     |          |        |
#  Ex 4     |          |        |
#  Ex 5     |          |        |
#  Ex 6     |          |        |
# ============================================================