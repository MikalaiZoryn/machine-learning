import matplotlib.pyplot as plt
import matplotlib.style as style

def main():
    data_set = open("../data_sets/cycling_calories.csv", "r")
    entries = []
    for line in data_set:
        date, distance, elevation, calories = line.strip().split(',')
        entry = CyclingCaloriesEntry(date, float(
            distance), int(elevation), int(calories))
        entries.append(entry)
        
    style.use
        
        
        
if __name__ == "__main__":
    main()