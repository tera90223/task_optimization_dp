import argparse
import pandas as pd
import numpy as np
from data_generation import generate_dataset
from algorithms.knapsack import knapsack
from algorithms.greedy import greedy

def parse_args():
    parser = argparse.ArgumentParser(description='Task Optimization using DP and Greedy Algorithms')

    parser.add_argument('--csv', type=str, default='../data/Version2_duration.csv', help='Path to existing task CSV file')
    parser.add_argument('--generate', action='store_true', help='Generate synthetic task dataset')
    parser.add_argument('--n', type=int, default=10, help='Number of tasks to generate')
    parser.add_argument('--choice', type=str, choices=["default", "similar priorities", "high correlation"], default="default", help='Select dataset type')
    parser.add_argument('--seed', type=int, default=None, help='Random seed')
    parser.add_argument('--save', action='store_true', help='Save synthetic task dataset as a CSV file')
    parser.add_argument('--time_budget', type=int, default=240, help='Total Time budget for the day')
    parser.add_argument('--cog_budget', type=int, default=80, help='Total Cognitive budget for the day')

    return parser.parse_args([])


if __name__ == "__main__":
    args = parse_args()

    if args.generate:
        df = generate_dataset(n=args.n, seed=args.seed, choice=args.choice, save=args.save)
    elif args.csv:
        with open(args.csv, mode='r', newline='') as csv_file:
            df = pd.read_csv(csv_file)
    else:
        raise ValueError("Must provide either --csv or --generate")

    cog_budget = args.cog_budget
    time_budget = args.time_budget
    greedy_type = {"Priority_First": 0, "Duration_First": 1, "Highest_Value_Per_time": 2}

    results = {
        "knapsack": {},
        "greedy_priority": {},
        "greedy_duration": {},
        "greedy_ratio": {},
    }

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



