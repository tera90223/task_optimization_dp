## Project Snapshot 
Research Question:  When both time and cognitive capacity are given, how does dynamic programming compare to greedy task-selection?

Algorithm: 0/1 knapsack

Current Implementation Status: In-progress

## What is Implemented?
I have implemented a full version of the knapsack and greedy algorithm as well as the driver for version 2 of my data
which is focused on duration of tasks instead of the task's deadline. 

This meant that we did not have to focus on filtering out tasks that had a deadline of *Today*.

The knapsack algorithm changed because we had two constraints to consider: duration and cognitive cost. 
The original pseudocode consolidated deadline and cognitive cost into one variable allowing it to mirror a traditional 
knapsack algorithm. 

Lastly, the greedy algorithm changed, as it only took time and priority into consideration as this is more realistic to 
how people typically choose their tasks. They are not typically thinking about their cognitive cost so it was not 
factored in although it was originally written that way in the pseudocode.

## Prototype Demo Description

To run the project, open and execute `code/task_optimization.ipynb` in Jupyter or IDE that supports Jupyter notebook. 
The notebook expects a single input file located at `data/Version2_duration.csv`, which contains the synthetic task 
dataset with columns for *task_name*, *duration*, *cognitive_cost*, and *priority*.

The notebook produces two outputs: a scheduled task list from the 0/1 knapsack algorithm and a scheduled task list 
from the greedy algorithm. Both lists are printed to the consoles with their unscheduled remainders. 

```
Knapsack Scheduled: ['Book Flights to Boston', 'Complete Duolingo', 'Wash 2 Loads of Laundry', 'Pilates', 'Complete Quiz ', 'Complete Peer Reviews', 'Run 2 miles']
Unscheduled tasks included: ['Read Literature Review', 'Meal Prep Dinner', 'Pick up Dry-Cleaning']

Greedy scheduled: ['Complete Duolingo', 'Pilates', 'Run 2 miles', 'Read Literature Review', 'Book Flights to Boston']
Unscheduled tasks included: ['Complete Peer Reviews', 'Complete Quiz ', 'Meal Prep Dinner', 'Wash 2 Loads of Laundry', 'Pick up Dry-Cleaning']
```
## Data Documentation
I created the data and I borrowed it from one of my to-do lists from my Notes app. The duration is based on the time I 
typically take to complete the task, and the cognitive cost is based on my subjective ranking. Priority scores were also 
based on personal importance and urgency. 

This data is self-reported and synthetic so there are no ground truths. This experiment is a proof of concept and the
data does not need validation.

## Initial Observations
My initial observations is that the knapsack algorithm provided us more tasks to do compared to the greedy algorithm. 
There was a bit of overlap between the tasks selected which is good, because my premise is not necessarily that dynamic 
programming would be better than greedy although that is promising, but that it is comparable.

## Reflection on Changes and Challenges
In creating the dataset, I noticed I deviated from my original idea when I wrote the `CONCEPT.md`. When I first designed 
the experiment, I wanted to build a knapsack algorithm that took in two constraints - duration of the task and cognitive
cost.

When I wrote the `CONCEPT.md` however, I shifted focus towards deadlines, likely because my personal life was filled 
with deadlines. This introduced personal scope creep which pushed the optimization towards scheduling which although 
is characterized as time, it adds more complexity. Scheduling optimizes a to-do list within a fixed timeline, which is
different concern than the original problem I had in mind.. 

As the concept is already written out, I am still planning on writing for both although I am now aware that my scheduling
plan might be more naive than I might have accounted for. 

Another thing to note is that the knapsack 2 algorithm could potentially be computationally expensive. 
With that being said, as stated before the number of tasks would stay relatively small to reflect real-world data, and 
the cognitive capacity is capped at 100. Yet there is a potential that time isn't capped and that could be troublesome 
as the runtime complexity is O(number of tasks * time * capacity). Since I am currently using nested `for` loops, 
it has the potential to become really slow.

## Next Steps 
My next steps include:
* Implementing the algorithm so it will work with Version 1 data (deadline dataset)
* Analysis of Greedy vs Dynamic Algorithm
* Implementing Edge Cases

*Optional Steps:*
* Implement an efficient Version 2 knapsack algorithm 
* Exploring if there is a way to combine the datasets

## Generative AI Disclosure
Tool: Claude Sonnet 4.6

### How it was used:
Claude was used as a thought partner throughout the design and implementation stages. Specific use includes:
* Algorithm reasoning - Extending 1D knapsack to a 3D array structure, and reasoning through my pseudocode and indexing logic
* Debugging - Identifying an off-by-one indexing error in the knapsack traceback function
* Writing - Refine my writing for clarity and technical precision (confirming my understanding of knapsack runtime complexity)

### Influence on implementation:
All code was written by me. Claude was used to test my reasoning and catch bugs rather than generate implementation directly.
The AI was used as a sound board and design decisions were also made by me.
