# 1. Project Summary
*Research Question: When both time and cognitive capacity are constrained, how does dynamic programming compare to greedy task-selection?* 

This project considers task optimization under two constraints: time and cognitive load. To address this, we implement a 0/1 Knapsack dynammic programming algorithm and compare its output to simulated greedy task-selection data, which reflects how we as humans naturally selects tasks. As we do not explicitly quantify cognitive load in real-world decision-making, the project will use synthetic data to simulate task optimization serving as a proof of concept for future decision-support tools. 

# 2. Inputs, Outputs, and Assumptions

## Input

Given a daily task list in csv format with the following information: 

| Name | Description | Data Type | 
| :--: | :---------: | :-------: |
| Task ID | Task Identifier | Int |
| Cognitive Capacity| Daily Cognitive Load Cap | Int |
| Cognitive Cost | Cognitive Cost per task | Int |
| Priority | Importance of Task | Binary |
| Deadline | Task Due Date: {0: Today, 1: This Week, 2: Flexible} | Int / Dictionary |

## Output
* A recommended task list, ordered based on capacity and deadline.
* Tasks that were not completed

## Assumptions
* Cognitive Capacity is a value between 0 and 100.
* Deadline will be simplified to 3 tiers - today, this week, or flexible.
* Priority is binary: high or low
* Tasks have to be fully completed - it is either done or not done.
* If a task has a deadline of today, it is scheduled regardless of whether it exceeds the remaining Cognitive Capacity
* All tasks are complete records
* The input file is a CSV file that represents one day of daily tasks for an individual.
* Total tasks is capped at 100

# Pseudocode


## Reason Code Lookup Function
Input: Reason Code (Int)
Output: Reason
Example: 
1 -> "Cognitive Capacity Exceeded"

## Knapsack 
### Build Knapsack array
*Note to self: The deadline tiers already acts like a bucket (urgency bucketing continuous discretization can be future extension) The idea is that the deadline tiers are ranked by capacity cost based on how close the deadline is so it can easily be added to the cognitive cost collapsing this into a classic knapsack problem*

```
Input: Input: Leftover Tasks, Remaining Capacity
Goal: The goal is to build the knapsack array


* W = Remaining Cognitive Capacity
* Values = Array of priority per task
* Weights = Array of cognitive cost + deadline tier per task

* Create a 2D array with number of tasks (O to len(tasks) and capacity (0 to W)
* Initialize the first row and column of the 2D array with zeros

# Go through each row which represents one task 
* for r in range(0, len(tasks)+1):

   # For each column, we will calaculate a score based on capacities ranging from 1 - W
   * for c in range(1, W+1):

      # This is the cost of the task
      * task_weight = Weights[r-1]

      # If the cost of the task is greater than the capacity represented by the column, we skip it
      * if task_weight > c:

          # We use the previous score of the row above the column
          * array[r][c] = array[r-1][c]

      # On the other hand, if the capacity cost of the task is <= the capacity represented by the column, we are tasked to see which score is more, that if we skip it or that if we keep it
      * else

          # First we will calculate if we keep the score, we want to remove the cost from the max capacity
          * weight_diff = c - task_weight

          # the score is calculated by adding the priority of the task to the remaining score... to get the remaining score, you look one row above, and you choose the column based on the weight difference we observed previously.
          * kept_score = Values[r-1] + array[r-1][weight_diff]

          # The final score takes the max of the kept score and the previous score which is the row above (same column)
          * final_score = max(array[r-1][c], kept_score)
          * array[r][c] = final_score

*return array

```

### Build Knapsack Traceback
```
Input: Knapsack Array, Tasks
Goal: To return scheduled and unscheduled tasks after tracing the knapsack array

# Initialize an empty list for scheduled and a full list of all tasks in the unscheduled 
* Initialize empty scheduled list
* Initialize task ids to unscheduled list

# c = W which is the last column of the array
* c = W

# Starting at the last row and last column, decrement through each row
* for r in range(len(tasks), 0, -1):
   # Compare the current row score to the score above (row - 1, column is same)
   * if array[r][c] != array[r-1][c]
      # if it is different that means the row was added to the knapsack so we want to append it to our task list
      * append tasks[id][r] to scheduled list
      # Remove the task from the unscheduled list
      * remove task[r] from unscheduled list
      # The capacity decreases by the weight of the task according the current row
      * c = c - Task[Weights][r-1]

# Return scheduled and unscheduled to-do lists 
* return scheduled, unscheduled
      

```
### Knapsack Driver
```
Input: Leftover Tasks, Remaining Capacity
Goal: Find the optimal combination of tasks is within the remaining cognitive capacity while maximizing total priority

* array = Build knapsack array(tasks, W) 
* scheduled, unscheduled = traceback(array, tasks) 
* Return scheduled and unscheduled list

```
## Greedy
```
Input: Leftover Tasks, Remaining Capacity
Goal: To maximize priority greedily wihthin the remaining cognitive capacity

* Sort Leftover tasks by priority descending
* Then sort leftover tasks by (deadline + cost) ascending
* Initialize current load to 0
* Initialize empty scheduled list
* Initialize tasks to unscheduled list

* for each task in sorted tasks:
   * task weight = deadline + cose 
   if current_load + task weight <= remaining capacity 
      * append task to scheduled list
      * remove task from unscheduled list
      * Add task weight to current load

* return scheduled and unscheduled lists

```

## Scheduling_Deadline_Tasks
```
Input: DF, cognitive capacity
Goal: This function prioritizes deadlines set today and add them to the final to-do list despite cognitive load

 * Initialize empty Final To-Do List
 * Initialize empty remaining tasks list
   
 *  for task in task_list:
    * Check if deadline is today
      *   append ID to final to-do list and remove from df
      *   subtract cognitive cost from cognitive capacity
   * Append tasks to remaining task list

return final to-do list, remaining task list, cognitive capacity
```

## Main
```
Input CSV file 

* Read file and parse into a dataframe excluding cognitive capacity
* Initialize Cognitive Capacity using data in csv file
* Validate no fields are missing as per assumption


* Initialize empty Leftover Tasks Dictionary {task_id : reason_code}


* Check if len(df) > 0
   * deadline_list, leftover_tasks, remaining_capacity =  Scheduling_Deadline_Tasks (df, cognitive capacity)
   * if remaining_capacity < 0:
    * Update Leftover Tasks with task id and reason code
    * Return Final To-do List, Leftover Task Dictionary
   * dp_scheduled, dp_unscheduled = Knapsack(leftover_tasks, remaining_capacity)
   * g_scheduled, d_unscheduled = Greedy(leftover_tasks, remaining_capacity)
   
   * Initialize empty DP Final To-Do List
   * Append deadline_list + dp_scheduled to DP final to-do list

   * Initialize empty Greedy Final To-Do List
   * Append deadline_list + g_scheduled to Greedy final to-do list
* else print "No tasks for today" 
```
# Complexity and Bottlenecks
As this is a proof of concept based on an average person daily tasks, this data wouldn't necessarily get large. Even the busiest person has less than 100 tasks per day therefore both the number of tasks and the max capacity load is constrained realistically.

The most expensive portion of each algorithm is building the knapsack array (O(nxW)) and sorting the df in the greedy algorithm (typically O(n log n)). Both are nelgibile when it comes to both time and space. With that being said if I wanted to be more efficient, the way the knapsack array is set up suggests there is a way to build it more efficiently such as making it a 1D array only capturing the traceback data, although it would require more research on my part.

# Validation and Testing Plan

# Updated Pitfall and Risk Log

# Generative AI Disclosure
Claude Sonnet 4.6 was utilized to improve readability by checking for syntax and grammatical errors, and made sure my idea was stated plainly. 

*"Can you help with syntax and grammatical concerns and make sure my paragraph flows and the idea is being stated plainly"*

