import numpy as np
import pandas as pd


def generate_dataset(n, seed, choice="default", save=False):
    """
    Accepts command line argument for which dataset to generate, defaults to random if none specified, writes output to data/ as CSV and returns df for direct usage in algorithm

    :param n: number fo tasks
    :param seed: random seed
    :param choice: "default": random data for each column, "similar priorities": priorities clustered between 5-7 with low probability of extreme values, "high correlation": high priority tasks are assigned proportionally high cognitive costs
    :param save: True: save output to CSV file
    :return: df - pd.dataframe containing task_name, duration, cognitive_cost and priority columns
    """

    rng = np.random.default_rng(seed)
    if choice == "default":
        df = generate_default_dataset(n, rng)
    elif choice == "similar priorities":
        df = generate_similar_priority_dataset(n, rng)
    elif choice == "high correlation":
        df = generate_high_correlation_dataset(n, rng)

    if save:
        filename = f"../data/task_dataset_{choice}_{n}.csv"
        df.to_csv(filename, index=False)

    return df


def generate_default_dataset(n, rng, priority_probs=None, noise=None):
    """
    Generates a task dataset with n tasks

    :param n: number of tasks
    :param rng: random seed generator
    :param priority_probs: similar priority probabilities to assign probabilities centered around 5-7
    :param noise: noise added to provide variation in the correlation of priority and cognitive costs
    :return: task_df - pd.dataframe containing task_name, duration, cognitive_cost and priority columns
    """
    task_ids = []
    for i in range(n):
        # Task Name
        task_id = f"task_{i + 1}"
        task_ids.append(task_id)

    # Duration
    durations = rng.choice(([5, 10, 15, 20, 30, 45, 60, 90, 120]), size=n)

    # Priorities
    if priority_probs is not None:
        priorities = rng.choice(range(1, 11), size=n, p=priority_probs)
    else:
        priorities = rng.integers(low=1, high=10, size=n)

    # Cognitive Cost
    if noise is not None:
        cognitive_costs = np.clip((priorities * 10) + noise, 1, 100)
    else:
        cognitive_costs = rng.integers(low=1, high=100, size=n)

    # task_name,duration,cognitive_cost,priority
    task_df = pd.DataFrame(
        {"task_name": task_ids, "duration": durations, "cognitive_cost": cognitive_costs, "priority": priorities})

    return task_df


def generate_similar_priority_dataset(n, rng):
    """
    Generates a task dataset with n tasks with probabilities centered around 5-7 with low probability of extreme values
    :param n: number of tasks
    :param rng: random seed generator
    :return:
    df - pd.dataframe containing task_name, duration, cognitive_cost and priority columns
    """
    probs = [0.05, 0.05, 0.05, 0.05, 0.2, 0.2, 0.2, 0.1, 0.05, 0.05]
    return generate_default_dataset(n, rng, priority_probs=probs)


def generate_high_correlation_dataset(n, rng):
    """
    Stress Test: High Correlation
    Generates a task dataset with n tasks with high correlation between priority and cognitive costs
    :param n: number of tasks
    :param rng: random seed generator
    :return: df - pd.dataframe containing task_name, duration, cognitive_cost and priority columns
    """

    noise = rng.integers(low=-10, high=10, size=n)
    return generate_default_dataset(n, rng, noise=noise)