def compute_prefix(pattern):
    p = [0] * len(pattern)
    j = 0
    i = 1

    while i < len(pattern):
        if pattern[j] == pattern[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]

    return p


def kmp_search(haystack, needle):
    indices = []

    if not needle:
        return indices
    p = compute_prefix(needle)
    m = len(needle)
    n = len(haystack)

    i = 0
    j = 0
    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == m:
                indices.append(i - j)
                j = p[j - 1]
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    return indices



