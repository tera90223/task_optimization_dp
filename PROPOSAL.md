## 1. Project Title 
* **Optimal Task Selection Using Dynamic Programming**

## 2. Research Question
1. When both time and cognitive capacity are given, how does dynamic programming compare to greedy task-selection?
2. When using a to-do list, users manually decide the order in which tasks are completed, typically mirroring a greedy approach. For instance, I frequently default to completing shorter or easier tasks, while leaving the more challenging tasks for later. Although I am progressing, it does not guarantee my time and energy is being utilized effectively or efficiently.

   Most productivity tools with to-do lists allow tasks to be labeled by priority, yet the ordering of the task is still left to the user. The idea though is that if a task is flagged as a priority, it should be completed before the other tasks, and the primary constraint utilized here is time. This does not account for other factors, such as cognitive load. Would prioritizing that task affect the completion of other tasks if you have a low cognitive capacity but short timing deadline? Leaving it to your intuition is also a cognitive demanding.
   
   This project will attempt to model task selection as an optimization problem in which both time and cognitive load are treated as constraints. Although the order of task selection is affected by many factors, the goal is to implement a dynamic programming solution and compare it to the baseline in order to evaluate whether the proposed system can provide measurable improvements. 

## 3. Algorithm and Algorithm Class
1. Dynamic Programming
2. *The algorithm I intend to implement*
3. *A brief justification of why this algorithm class is a good fit for my question**
