import argparse
import pandas as pd
from data_generation import generate_dataset
from algorithms.knapsack import knapsack
from algorithms.greedy import greedy
from render import render_results

def parse_args():
    parser = argparse.ArgumentParser(description='Task Optimization using DP and Greedy Algorithms')

    parser.add_argument('--csv', type=str, default='../data/real_todo_list.csv', help='Path to existing task CSV file')
    parser.add_argument('--generate', action='store_true', help='Generate synthetic task dataset')
    parser.add_argument('--n', type=int, default=10, help='Number of tasks to generate')
    parser.add_argument('--choice', type=str, choices=["default", "similar priorities", "high correlation"], default="default", help='Select dataset type')
    parser.add_argument('--seed', type=int, default=None, help='Random seed')
    parser.add_argument('--save', action='store_true', help='Save synthetic task dataset as a CSV file')
    parser.add_argument('--time_budget', type=int, default=240, help='Total Time budget for the day')
    parser.add_argument('--cog_budget', type=int, default=80, help='Total Cognitive budget for the day')

    return parser.parse_args()

def build_score_card(task_df, results, cog_budget, time_budget):
    """
    Function builds a score card to easily interpret results.
    Score card provides
    - name of Algorithm
    - Priority Score normalized to knapsack
    - Time Utilization
    - Cognitive Utilization
    - Tasks Utilization

    :param task_df: [pd.DataFrame] task DF
    :param results: [dict] results of each algorithm
    :param cog_budget: [int] total cognitive budget
    :param time_budget: [int] total time budget
    :return: score_card: [pd.DataFrame] score card for each algorithm
    """
    score_card = pd.DataFrame()
    total_priority_per_alg = []
    total_duration_per_alg = []
    total_cog_cost_per_alg = []
    n_scheduled_per_alg = []

    for algorithm in results.keys():
        total_priority = 0
        total_duration = 0
        total_cog_cost = 0

        for task in results[algorithm]["scheduled"]:
            total_priority += task_df.loc[task_df["task_name"] == task, 'priority'].values[0]
            total_duration += task_df.loc[task_df["task_name"] == task, 'duration'].values[0]
            total_cog_cost += task_df.loc[task_df["task_name"] == task, 'cognitive_cost'].values[0]
        if algorithm == "knapsack":
            knapsack_total_priority = total_priority

        total_priority_per_alg.append(round(total_priority / knapsack_total_priority*100, 2))
        total_duration_per_alg.append(round(total_duration/time_budget*100, 2))
        total_cog_cost_per_alg.append(round(total_cog_cost/cog_budget*100, 2))
        n_scheduled_per_alg.append(round(len(results[algorithm]["scheduled"])/len(task_df)*100, 2))

    score_card["Algorithm"] = results.keys()
    score_card[f"Priority Score (%)"] = total_priority_per_alg
    score_card["Time Utilization (%) "] = total_duration_per_alg
    score_card["Cognitive Utilization (%)"] = total_cog_cost_per_alg
    score_card["Tasks Utilization (%)"] = n_scheduled_per_alg

    return score_card

if __name__ == "__main__":
    args = parse_args()
    # if data is being generated, use data_generation to get synthetic data
    if args.generate:
        df = generate_dataset(n=args.n, seed=args.seed, choice=args.choice, save=args.save)
    # else if provided a csv file, convert to df
    elif args.csv:
        with open(args.csv, mode='r', newline='') as csv_file:
            df = pd.read_csv(csv_file)
    else:
        raise ValueError("Must provide either --csv or --generate")


    cog_budget = args.cog_budget
    time_budget = args.time_budget
    # Greedy variation map
    greedy_type = {"Priority_First": 0, "Duration_First": 1, "Highest_Value_Per_time": 2}

    results = {
        "knapsack": {},
        "greedy_priority": {},
        "greedy_duration": {},
        "greedy_ratio": {},
    }

    # Get results for each algorithm or algorithm variation
    if len(df) > 0:
        results["knapsack"]["scheduled"], results["knapsack"]["unscheduled"] = knapsack(df, cog_budget, time_budget)
        results["greedy_priority"]["scheduled"], results["greedy_priority"]["unscheduled"] = greedy(df, time_budget,
                                                                                                    greedy_type["Priority_First"])
        results["greedy_duration"]["scheduled"], results["greedy_duration"]["unscheduled"] = greedy(df, time_budget,
                                                                                                    greedy_type[
                                                                                                        "Duration_First"])
        results["greedy_ratio"]["scheduled"], results["greedy_ratio"]["unscheduled"] = greedy(df, time_budget,
                                                                                              greedy_type[
                                                                                                  "Highest_Value_Per_time"])
    else:
        print("No tasks for today!")

    # Compute score card
    score_card = build_score_card(task_df = df, results = results, cog_budget = cog_budget, time_budget = time_budget)

    # Render results in html
    render_results(results, score_card)






