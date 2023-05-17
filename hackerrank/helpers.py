def calculate_with_regex(utc_regex, utc_difference):
    count = 0
    hour_diff_float = ""

    regex = utc_regex.get(
        utc_difference.__len__()
    )

    while count < regex.__len__():

        if regex[count] == "H":
            hour_diff_float += utc_difference[count]

        elif regex[count] == "M":
            hour_diff_float = float(hour_diff_float) if hour_diff_float else 0.0
            converted_min = int(utc_difference[count:]) / 60
            hour_diff_float += float(f"{converted_min}")
            break

        count += 1

    return hour_diff_float
