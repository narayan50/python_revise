"""practice.py
Simple utility to find the maximum (largest) and minimum (smallest) elements
in a list of numbers entered by the user.

Usage:
 - Enter numbers separated by spaces when prompted, or press Enter to use
   a default example list.
"""

from typing import List, Tuple


def get_numbers_from_input(prompt: str = "Enter numbers separated by spaces (empty for example list): ") -> List[float]:
    s = input(prompt).strip()
    if not s:
        # example default list
        return [3, 1, 4, 1, 5, 9]
    parts = s.split()
    nums: List[float] = []
    for p in parts:
        try:
            if "." in p:
                nums.append(float(p))
            else:
                nums.append(int(p))
        except ValueError:
            raise ValueError(f"Invalid number: {p}")
    return nums


def manual_min_max(nums: List[float]) -> Tuple[float, float]:
    if not nums:
        raise ValueError("Empty list")
    smallest = largest = nums[0]
    for n in nums[1:]:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return smallest, largest


def main() -> None:
    try:
        nums = get_numbers_from_input()
    except ValueError as e:
        print(e)
        return

    print("Numbers:", nums)

    # Using built-in functions
    print("Built-in min:", min(nums))
    print("Built-in max:", max(nums))

    # Using manual method
    small, large = manual_min_max(nums)
    print("Manual smallest:", small)
    print("Manual largest:", large)


if __name__ == "__main__":
    main()

