## What Went Right
The knapsack and greedy algorithms were implemented early which gave me more time concerning design decisions and
how I wanted to render the results. I also think the modulation of the functions allowed me to easily implement a 
command-line compatible platform. I am proud I was able to implement the html version of the results as one of my 
classmates focus on the user experience pushed me to visually showcase my results. The html is simple but I think it is
easier to digest the results. 

I also was personally happy I was able to implement the three greedy variations as it definitely provided a more
comprehensive discussion. 

Choosing to synthesize dataset based on real to-do lists also proved to be a strong design choice. 
It allowed for more interpretability and was more personally meaningful to me as I chose cognitive capacity, because I 
struggle with burnout often. 

## What Went Wrong or Was Hard

Originally making a 3d array was hard to implement as I could not understand how the array could be 3D, but once I 
created a visual, it was easier for me to navigate. With that being said, I used numpy arrays and did not take 
advantage of vectorization mostly because I did not know it was a feature until after I implemented the array. 
If I could do things differently, I would have used vectorization. 
I also think that designing the implementation of the experiment was tedious. I knew exactly what I wanted to test, 
but to implement it in a way that was reasonable to my peers and was also streamlined so they wouldn't have to jump 
from code to code was harder to think through. 
I also used some elementary coding practices, such as using a map instead of enum to reference greedy variation, 
due to time constraints. I do feel If I had more time, I would think about ways to be more efficient. Lastly, I would
have liked to spent more time analyzing my results. While finishing up my final V1 of the experiment, I thought about 
more thoughtful ways to analyze my results.

## Algorithmic Lessons
0/1 Knapsack algorithm was a natural fit for my problem since task optimization is inherently a breakdown of subproblems.
For each task you have to see if you have the time and capacity to complete it and if including it with the other tasks
leads to a better combination than excluding it The knapsack table captures this by building up the answers starting 
from no tasks or budget to all tasks using previously computed answers to evaluate each step.

With that being said, we did optimize by priority another user-assigned feature. This means the algorithm is as good as 
the users input and so if the user is inaccurate concerning priority, their cognitive capacity, or their time budget, 
they will receive suboptimal recommendations. 

One surprise was how well the ratio-based greedy matched the knapsack solution on my default dataset. Based on multiple
runs, greedy is not able to guarantee optimal results, but in the situation that it does, it does raise a question 
concerning if DP is ALWAYS necessary and if not, when should it be utilized?

## Future Directions
Some ideas for improving my project is to introduce vectorization to the knapsack algorithm to increase efficiency 
during runtime. Another idea is to add task dependencies as tasks are not always dependencies and to experiment with 
making time and cognitive capacity dynamic. Lastly, I would like to implement a version I introduced previously, but I 
chalked down to scope creep which is to add another time layer due dates.

## Generative AI Disclosure
Tool: Claude Sonnet 4.6

### How it was used:
Claude was used as a thought partner throughout the design, implementation, and documentation stages. Specific use includes:
* **Dataset design** - Discussing schema decisions and constraint budget selection
* **HTML Rendering** - Designing the Jinja2 template structure and scorecard normalization approach
* **Writing** - Refining reflections, observations, and documentation for clarity and technical accuracy
### Influence on implementation:
All code was written by me. Claude was used to test my reasoning and catch bugs rather than generate implementation directly.
The AI was used as a sound board and design decisions, implementations, and interpretation of results were also made by me.
