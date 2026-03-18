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

# Pseudocode


## Reason Code Lookup Function
Input: Reason Code (Int)
Output: Reason
Example: 
1 -> "Cognitive Capacity Exceeded"

## Knapsack
*Note to self: The deadline tiers already acts like a bucket (urgency bucketing continuous discretization can be future extension) The idea is that the deadline tiers are ranked by capacity cost based on how close the deadline is so it can easily be added to the cognitive cost collapsing this into a classic knapsack problem*

```
Input: Leftover Tasks, Remaining Capacity

* W = Remaining Cognitive Capacity
* Values = Array of priority per task
* Weights = Array of cognitive cost + deadline tier per task

* Create a 2D array with number of tasks (O to len(tasks) and capacity (0 to W)

* for c in range(1, W+1):
   * for r in range(0, len(tasks)):
      * if weight[0] > current_W
         *continue
      *

```
## Greedy
```
Input: Leftover Tasks, Remaining Capacity 
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

Provide pseudocode that:
Has clear function signatures or step headings.
Explicitly describes main loops, conditionals, and data structures.
Handles at least one non-trivial edge case (e.g., empty input, unexpected characters, disconnected graph).
Use code-style formatting (indented blocks, consistent naming) so that another student could implement it in Python or another language.
main
# Complexity and Bottlenecks
# Validation and Testing Plan

# Updated Pitfall and Risk Log

# Generative AI Disclosure
Claude Sonnet 4.6 was utilized to improve readability by checking for syntax and grammatical errors, and made sure my idea was stated plainly. 

*"Can you help with syntax and grammatical concerns and make sure my paragraph flows and the idea is being stated plainly"*

