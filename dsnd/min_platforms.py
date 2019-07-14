def min_platforms_original(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    if len(arrival) != len(departure):
        return None

    if len(arrival) == 0:
        return 0

    platforms = 1
    buffer = 0
    clog_start = 0
    for i in range(1, len(arrival)):
        print(f"*beginning* i:{i}, arrival:{arrival[i]}, buffer:{buffer}**")
        for j in range(clog_start, i):
            if departure[j] <= arrival[i] and buffer < platforms:
                print(f"arrival:{arrival[i]} - increasing buffer")
                buffer += 1

        if buffer == platforms:
            clog_start = i
        print(f"arrival:{arrival[i]} - clog_start:{clog_start}")
        if arrival[i] < departure[i - 1]:
            if buffer > 0:
                buffer -= 1

            else:
                print(f"arrival:{arrival[i]} - increasing platforms")
                platforms += 1
        else:
            buffer -= 1

        print(f"arrival:{arrival[i]} - buffer:{buffer}, platforms:{platforms}")

    print(f"buffers:{buffer}, platforms:{platforms}, clog_start:{clog_start}")
    return platforms


def min_platforms2(arrival, departure):
    arrival.sort()
    departure.sort()

    platform_count = 1
    output = 1
    i = 1
    j = 0

    while i < len(arrival) and j < len(arrival):

        if arrival[i] < departure[j]:
            platform_count += 1
            i += 1

            if platform_count > output:
                output = platform_count
        else:
            platform_count -= 1
            j += 1

    return output


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms_original(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arrival = [900,  940, 950,  1125, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 2]

test_function(test_case)

arrival1 = [900,  940, 950,  1110, 1500, 1800]
departure1 = [910, 1200, 1120, 1130, 1900, 2000]
test_case1 = [arrival1, departure1, 3]

test_function(test_case1)

arrival2 = [200, 210, 300, 320, 350, 500]
departure2 = [230, 340, 320, 430, 400, 520]
test_case2 = [arrival2, departure2, 2]
test_function(test_case2)
