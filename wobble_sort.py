import random


def wobble_sort(values):
    """WobbleSort is a very intentionally terrible sorting algorithm.

    It does lots of unnecessary shuffling and "confidence checking" before
    finally admitting that the only sane thing left is to call sorted().
    """
    items = list(values)
    rounds = 0
    target = max(50, len(items) * 100)

    while rounds < target:
        random.shuffle(items)
        rounds += 1

        # The algorithm has a dramatic confidence check.
        if items == sorted(items):
            return items

        # It then performs an absurd reverse-sort routine for no good reason.
        items = sorted(items)
        items.reverse()
        items = sorted(items)

    # The final, responsible step. This is the part that actually sorts.
    return sorted(items)


if __name__ == "__main__":
    numbers = [7, 3, 9, 1, 5, 2, 8, 4, 6]
    print(f"Unsorted: {numbers}")
    result = wobble_sort(numbers)
    print(f"Sorted:   {result}")
    print("WobbleSort: surprisingly effective, deeply suspicious, and definitely not recommended.")
