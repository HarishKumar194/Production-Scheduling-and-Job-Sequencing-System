import csv

# Load jobs from CSV
jobs = []

with open("jobs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        jobs.append({
            "job_id": row["JobID"],
            "processing_time": int(row["ProcessingTime"]),
            "priority": int(row["Priority"])
        })


# Scheduling Algorithms
def fcfs(job_list):
    return job_list


def shortest_processing_time(job_list):
    return sorted(job_list, key=lambda x: x["processing_time"])


def priority_scheduling(job_list):
    return sorted(job_list, key=lambda x: x["priority"], reverse=True)


# Performance Metrics
def calculate_metrics(schedule):

    current_time = 0
    waiting_times = []

    for job in schedule:
        waiting_times.append(current_time)
        current_time += job["processing_time"]

    avg_waiting_time = sum(waiting_times) / len(waiting_times)

    return avg_waiting_time, current_time


# Menu
print("\nProduction Scheduling and Job Sequencing System")
print("------------------------------------------------")
print("1. First Come First Serve (FCFS)")
print("2. Shortest Processing Time (SPT)")
print("3. Priority Scheduling")

choice = input("\nEnter your choice: ")

if choice == "1":
    schedule = fcfs(jobs)
    algorithm = "FCFS"

elif choice == "2":
    schedule = shortest_processing_time(jobs)
    algorithm = "SPT"

elif choice == "3":
    schedule = priority_scheduling(jobs)
    algorithm = "Priority Scheduling"

else:
    print("Invalid Choice")
    exit()

avg_waiting, total_completion = calculate_metrics(schedule)

print(f"\nSelected Algorithm: {algorithm}")

print("\nJob Execution Order:")
for job in schedule:
    print(job["job_id"])

print("\nPerformance Metrics")
print("-------------------")
print(f"Average Waiting Time : {avg_waiting:.2f}")
print(f"Total Completion Time: {total_completion}")
