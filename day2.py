
reports = []

with open('input/input2.txt', 'r') as f:
    for line in f.readlines():
        reports.append([int(x) for x in line.split()])


def unsafe_check(is_first, idx, report):
    if not is_first:
        return False
    if idx - 1 == 0:
        check_dampened = is_report_safe(report[1:], False) or is_report_safe(report[:idx - 1] + report[idx:], False)
    else:
        check_dampened = is_report_safe(report[:idx] + report[idx+1:], False)
    if check_dampened:
        return True
    return False

safe = 0

def is_report_safe(new_report, is_first=True):
    increasing = None
    prev_level = None
    for idx, level in enumerate(new_report):
        if prev_level:
            diff = prev_level - level
            if abs(diff) > 3 or abs(diff) < 1:
                break
                # return unsafe_check(is_first, idx, new_report)
            if increasing is None:
                break
                # increasing = diff < 0
            elif increasing and diff > 0:
                break
                # return unsafe_check(is_first, idx, new_report)
            elif not increasing and diff < 0:
                break
                # return unsafe_check(is_first, idx, new_report)
        prev_level = level
    return True


def brute_force_unsafe(report):
    for idx_1 in range(len(report)):
        increasing = None
        prev_level = None
        new_report = report[:idx_1] + report[idx_1 + 1:]
        # print(len(new_report))
        for idx, level in enumerate(new_report):
            if prev_level:
                diff = prev_level - level
                if abs(diff) > 3 or abs(diff) < 1:
                    break
                if increasing is None:
                    increasing = diff < 0
                elif increasing and diff > 0:
                    break
                    # return unsafe_check(is_first, idx, new_report)
                elif not increasing and diff < 0:
                    print(idx_1)
                    break
                    # return unsafe_check(is_first, idx, new_report)
            prev_level = level
        return True
#
# for report in reports:
#     is_safe = brute_force_unsafe(report)
#     if is_safe:
#         safe += 1


def new_brute_force_safe(bf_report):
    diffs = [x - bf_report[index] for index, x in enumerate(bf_report[1:])]
    # print(diffs)
    return set(diffs) <= {1,2,3} or set(diffs) <= {-1,-2,-3}


safe_count = 0
for report in reports:
    if new_brute_force_safe(report):
        safe_count += 1
        continue
    else:
        for idx, value in enumerate(report):
            new_report = report[:idx] + report[idx + 1:]
            if new_brute_force_safe(new_report):
                safe_count += 1
                break




print(safe_count)
