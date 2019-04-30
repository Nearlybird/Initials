import sys

def workout_coach(lift_name, wt):
    print("Time to", lift_name, wt, "pounds! You got this!")

def main():
    sys.setExecutionLimit(120000) # keep program from timing out
    lifts = ["squat", "bench", "deadlift"]
    weight = 0
    for extrasize in list lifts:
        workout_coach(extrasize, weight + 10)
    # Your code here

if __name__ == "__main__":
    main()

