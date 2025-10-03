class CyclingCaloriesEntry:
    def __init__(self, date, distance, elevation, calories):
        self.date = date
        self.distance = distance  # in miles
        self.elevation = elevation  # in feet
        self.calories = calories  # calories burned

    def __repr__(self):
        return f"CyclingCaloriesEntry(date={self.date}, distance={self.distance}, elevation={self.elevation}, calories={self.calories})"

    def __str__(self):
        return f"Date: {self.date}, Distance: {self.distance} mi, Elevation: {self.elevation} feet, Calories: {self.calories}"


def main():
    # Example usage of CyclingCaloriesEntry
    data_set = open("../data_sets/cycling_calories.csv", "r")
    entries = []
    for line in data_set:
        date, distance, elevation, calories = line.strip().split(',')
        entry = CyclingCaloriesEntry(date, float(
            distance), int(elevation), int(calories))
        entries.append(entry)

    print("Cycling Calories Entries:")

    for entry in entries:
        print(entry)

    data_set.close()

    coefficients = [860.4443636582432, 14.930068432084498, -0.3650368714719225]
    difference = calculate_difference(entries, coefficients)
    initial_difference = difference

    print(f"initial coefficients: {coefficients}")
    print(f"initial difference: {difference}")

    delta = 0.000001
    for _ in range(100000):  # number of iterations
        for i in range(len(coefficients)):
            print(f"current coefficients: {coefficients}")
            step = 0
            for entry in entries:
                step += (calculate_calories(entry, coefficients) - entry.calories) * \
                    (entry.distance if i == 1 else entry.elevation if i == 2 else 1)

            coefficients[i] -= delta * step
            difference = calculate_difference(entries, coefficients)
            print(f"updated coefficients: {coefficients}")
            print(f"new difference: {difference}")

    print(f"difference change: {initial_difference - difference}")


def calculate_difference(entries, coefficients):
    difference = 0
    for entry in entries:
        prediction = calculate_calories(entry, coefficients)
        difference += ((prediction - entry.calories) ** 2)
    return difference / 2


def calculate_calories(entry, coefficients):
    return coefficients[0] + coefficients[1] * entry.distance + coefficients[2] * entry.elevation


if __name__ == "__main__":
    main()
