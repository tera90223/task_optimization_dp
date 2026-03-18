# 1. Project Summary
*Research Question: When both time and cognitive capacity are constrained, how does dynamic programming compare to greedy task-selection?* 

This project considers task optimization under two constraints: time and cognitive load. To address this, we implement a 0/1 Knapsack dynammic programming algorithm and compare its output to simulated greedy task-selection data, which reflects how we as humans naturally selects tasks. As we do not explicitly quantify cognitive load in real-world decision-making, the project will use synthetic data to simulate task optimization serving as a proof of concept for future decision-support tools. 

# 2. Inputs, Outputs, and Assumptions

## Input

Given a daily task list with the following information: 

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
* A warning if Cognitive Capacity was exceeded

## Assumptions
* Cognitive Capacity is a value between 0 and 100.
* Deadline will be simplified to 3 tiers - today, this week, or flexible.
* Priority is binary: high or low
* Tasks have to be fully completed - it is either done or not done.
* If a task has a deadline of today, it is scheduled regardless of whether it exceeds the remaining Cognitive Capacity

# Pseudocode
# Complexity and Bottlenecks
# Validation and Testing Plan
# Updated Pitfall and Risk Log

# Generative AI Disclosure
Claude Sonnet 4.6 was utilized to improve readability by checking for syntax and grammatical errors, and made sure my idea was stated plainly. 

*"Can you help with syntax and grammatical concerns and make sure my paragraph flows and the idea is being stated plainly"*

