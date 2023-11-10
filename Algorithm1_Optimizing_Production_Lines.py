#Created by Aria Askaryar
#Algorithm 1: Optimizing Production Lines

def canDistribute(Durations, mid, Stations):
    """
    Check if the assembly line can be optimized to ensure that no station exceeds the given time 'mid'.

    Parameters:
    Durations (list of int): A non-empty list of positive integers representing the duration of each step in the assembly line.
    mid (int): The maximum allowed time that a station can take.
    Stations (int): The total number of stations available.

    Returns:
    bool: True if the given durations can be distributed among the stations without exceeding 'mid' time per station, False otherwise.
    """
    used_stations = 0  # Counter for the number of stations used
    current_time = 0   # Time accumulator for the current station

    # Process each duration in the Durations list
    for d in Durations:
        # If adding the current duration to the current_time exceeds the 'mid', allocate a new station
        if current_time + d > mid:
            used_stations += 1  # Increment the station count
            current_time = 0    # Reset the time for the new station
        current_time += d  # Add the duration to the current station's time

    used_stations += 1  # Account for the last station used

    # If the number of used stations is within the limit, return True
    return used_stations <= Stations

def longestDuration(Durations, Stations):
    """
    Finds the optimized longest duration for a single station in the assembly line.

    Parameters:
    Durations (list of int): A non-empty list of positive integers representing the duration of each step in the assembly line.
    Stations (int): The total number of stations available.

    Returns:
    int: The optimized longest duration of a single station after the distribution of steps.
    """
    left, right = max(Durations), sum(Durations)  # Initialize the binary search boundaries

    # Binary search to find the minimum maximum duration that can be handled by the Stations
    while left <= right:
        mid = (left + right) // 2  # Find the middle value between the current bounds

        # If the current 'mid' can be distributed without exceeding the station limits, search left (lower durations)
        if canDistribute(Durations, mid, Stations):
            right = mid - 1
        else:  # If not, search right (higher durations)
            left = mid + 1

    # The 'left' pointer represents the minimum maximum duration after binary search
    return left

# Testing the function
Durations = [15, 15, 30, 30, 45]
Stations = 3
print(longestDuration(Durations, Stations))  # Expected Output: 60
