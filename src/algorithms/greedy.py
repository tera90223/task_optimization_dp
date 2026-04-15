def greedy(tasks,time_budget, greedy_type = None):
    if greedy_type is None or greedy_type == 0:
        # Sort tasks by priority descending, then duration ascending (Tiebreaker: If two tasks have the same priority, prefer the shortest duration one)
        tasks_sorted = tasks.sort_values(by=["priority", "duration"], ascending=[False, True])
    elif greedy_type == 1:
        # Sort tasks by duration ascending, then priority descending (Tiebreaker: If two tasks have the same duration, prefer the highest priority one)
        tasks_sorted = tasks.sort_values(by=["duration", "priority"], ascending=[True, False])
    elif greedy_type == 2:
        # Add column for highest value per time
        tasks["ratio"] = tasks["priority"] / tasks["duration"]
        # Sort tasks by ratio descending, then priority descending (Tiebreaker: If two tasks have same efficiency score, prefer highest priority one)
        tasks_sorted = tasks.sort_values(by=["ratio", "priority"], ascending=[False, False])


    # initial current time spent to 0
    time_spent = 0

    # Initialize empty scheduled list
    scheduled = []

    # Initialize tasks to unscheduled list
    unscheduled = tasks.task_name.tolist()

    # for each task in sorted list
    for _,task in tasks_sorted.iterrows():
        # if cumulative time spent <= time budgeted
        if time_spent + task.duration <= time_budget:
            # Append the task to schedule
            scheduled.append(task.task_name)
            # Remove task from unscheduled list
            unscheduled.remove(task.task_name)
            # Add task duration to time spent
            time_spent += task.duration
    return scheduled, unscheduled
