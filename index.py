def find_peak(lst):
    if len(lst) == 0:
        return "List is empty"
    if len(lst) == 1:
        return str(lst[0])  # only element is a peak
    if lst[0] > lst[1]:
        return str(lst[0])
    if lst[-1] > lst[-2]:
        return str(lst[-1])
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            return str(lst[i])  # Return the peak as a string
    return "No peak"  # If no peak is found
print(find_peak([1, 3, 2, 5, 4]))