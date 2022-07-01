from fixed_values import *

def calculate_result(elements, masses, targets, checked) -> int:
    """Calculates result using given algorithm"""
    result = 0
    global_min = min(masses)
    for i in range(elements):
        if not checked[i]:
            local_sum, local_min, cycle_length = 0, MAX_MASS, 0
            j = i
            while not checked[j]:
                checked[j] = True
                local_sum += masses[j]
                local_min = min(local_min, masses[j])
                j = targets[j + 1] - 1
                cycle_length +=1
            method1 = local_sum + (cycle_length - 2) * local_min
            method2 = local_sum + local_min + (cycle_length + 1) * global_min
            result += min(method1, method2)
    return result