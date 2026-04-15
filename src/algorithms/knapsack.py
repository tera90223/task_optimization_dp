import numpy as np

def build_knapsack_array(tasks, capacity, time_budget):

    # INITIALIZATION
    weights_cog = tasks.cognitive_cost.tolist()
    weights_duration = tasks.duration.tolist()
    values = tasks.priority.tolist()

    # Create a 3D array with number of tasks x cognitive capacity x total time and feel with 0s
    knapsack_array = np.zeros((len(tasks)+1, time_budget+1, capacity+1), dtype = int)

    # Go through each row which represents one task
    for r in range(1, len(tasks)+1):
        for c_time in range(1, time_budget+1):
            for c_cap in range(1, capacity+1):

                # Cognitive cost
                task_cog = weights_cog[r-1]
                # duration cost
                task_duration = weights_duration[r-1]

                # if the cost of the task is grater than the capacity or duration represented by the column, we skip it
                if task_duration > c_time or task_cog > c_cap:
                    # We will use the previous score of the row above the column
                    knapsack_array[r][c_time][c_cap] = knapsack_array[r-1][c_time][c_cap]

                # On the other hand, if the capacity cost of the task is <= the capacity represented by the column, we are tasked to see which score is more, that if we skip it or that if we keep it
                else:
                    # First we will calculate if we keep the score, we want to remove the cost from the max capacity
                    time_weight_diff = c_time - task_duration
                    capacity_weight_diff = c_cap - task_cog

                    # the score is calculated by adding the priority of the task to the remaining score... to get the remaining score, you look one row above, and you choose the column based on the weight difference we observed previously.
                    kept_score = values[r-1] + knapsack_array[r-1][time_weight_diff][capacity_weight_diff]

                    # The final score takes the max of the kept score and the previous score which is the row above (same column)
                    final_score = max(knapsack_array[r-1][c_time][c_cap], kept_score)
                    knapsack_array[r][c_time][c_cap] = final_score

    return knapsack_array

def knapsack_traceback(knapsack_array, tasks):
    scheduled = []
    unscheduled = tasks.task_name.tolist()
    duration_list = tasks.duration.tolist()
    capacity_list = tasks.cognitive_cost.tolist()

    # We want to start at the last cell for both time anc capacity
    c_time = knapsack_array.shape[1]-1
    c_cap = knapsack_array.shape[2]-1

    # Starting at the last row and last column, decrement through each row
    for r in range(len(tasks), 0, -1):
        # Compare the current row score to the score above (row - 1, column is same)
        if knapsack_array[r][c_time][c_cap] != knapsack_array[r-1][c_time][c_cap]:
            # if it is different that means the row was added to the knapsack so we want to append it to our task list
            scheduled.append(unscheduled[r-1])
            # Remove the task from the unscheduled list
            unscheduled.remove(unscheduled[r-1])
            # The capacity decreases by the weight of the task according the current row
            c_time = c_time - duration_list[r-1]
            c_cap = c_cap - capacity_list[r-1]

    # Return scheduled and unscheduled to-do lists
    return scheduled, unscheduled

def knapsack(tasks, capacity, time_budget):
    array = build_knapsack_array(tasks, capacity, time_budget)
    scheduled, unscheduled = knapsack_traceback(array, tasks)
    return scheduled, unscheduled