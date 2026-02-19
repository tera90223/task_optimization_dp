## 1. Project Title 
* **Optimal Task Selection Using Dynamic Programming**

## 2. Research Question
1. When both time and cognitive capacity are given, how does dynamic programming compare to greedy task-selection?
2. When using a to-do list, users manually decide the order in which tasks are completed, typically mirroring a greedy approach. For instance, I frequently default to completing shorter or easier tasks, while leaving the more challenging tasks for later. Although I am progressing, it does not guarantee my time and energy is being utilized effectively or efficiently.

   Most productivity tools with to-do lists allow tasks to be labeled by priority, yet the ordering of the task is still left to the user. The idea though is that if a task is flagged as a priority, it should be completed before the other tasks, and the primary constraint utilized here is time. This does not account for other factors, such as cognitive load. Would prioritizing that task affect the completion of other tasks if you have a low cognitive capacity but short timing deadline? Leaving it to your intuition is also cognitive demanding.
   
   This project will attempt to model task selection as an optimization problem in which both time and cognitive load are treated as constraints. Although the order of task selection is affected by many factors, the goal is to implement a dynamic programming solution and compare it to the baseline greedy approaches in order to evaluate whether the proposed system can provide measurable improvements. 

## 3. Algorithm and Algorithm Class
1. Broader Class: Dynamic Programming
2. 0/1 Knapsack
3. Dynamic programming seems like a good fit because the problem is riddled with overlapping subproblems and finding the optimal substructure. The algorithm is a good fit because 0/1 knapsack models binary task selection under given constraints.

## 4. Data Plan
1. As this is a proof of concept, synthetic data would suffice. It would be a CSV with three features - Duration, Cognitive Load, and Value. Each task is represented by a row. 
2. I will create a script to generate the data for reproducibility.
3. 
   | Feature | Data Type |
   |:------: | :-------: |
   | Duration | Integer |
   | Cognitive Load | Integer |
   | Value | Integer |
 
5. No License or access considerations
6. A brief "prototype data" plan
   1. I will manually construct a small dataset to validate my DP algorithm approach
   2. Once validate, I will scale to a larger and reproducible synthetic dataset to test performance and compare to greedy approaches.

 ## 5. Success Criteria
 This experiment is deemed successful if I am able to:
 
     * output a task selection model using 0/1 knapsack using time and cognitive load as constraints
     * Compare DP model to three simulated greedy approaches
        * The greedy approaches include shortest duration first, highest priority first, and highest value per time
     * Showcase the greedy approach in task selection can fail
     
 ## 6. Pitfall Scan     
  1. Data Related Issues
  2. Algorithmic Issues
   * One issue is that 0/1 knapsack can be computationally expensive asruntime and memory tends to scales linearly with each constraint. Dynamic Programming are pseudo-polynomial and for this program, runtime will take O(n*D*C), where n = number of tasks, D = Duration and C = Cognitive capcity. This is important to note as we scale our synthetic dataset. 
   * We can keep track of execution time across tasks and measure time across different constraints. We can also monitor memory usage.
   * To mitigate this problem, discretizing constraints like instead of using minutes for each task duration we can utilize 15-minute blocks may help. 
  4. Evaluation Issues

## 7. Planned Repository Structure
- Scripts/
   - python scripts
- Analysis/
   - Notebook with Analysis
- Documentation /
   - PROPOSAL.md
- README.md

