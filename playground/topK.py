from collections import Counter


def get_top_k(nums, k):
    """
    Return the top k most frequent elements in the given list of numbers.

    Parameters:
    - nums (List[int]): A list of integers.
    - k (int): The number of most frequent elements to return.

    Returns:
    - List[int]: A list of the top k most frequent elements.
    """
    freqDict = Counter(nums)

    out = []
    while k > 0:
        nextKey = freqDict.most_common(1)[0][0]
        out.append(nextKey)
        freqDict.pop(nextKey)
        k -= 1

    return out


hello = lambda: "hello world"
