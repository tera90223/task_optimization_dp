import pandas as pd
import sys
sys.path.insert(0, 'src')

from algorithms.knapsack import knapsack
from algorithms.greedy import greedy
from main import build_score_card


tasks = pd.DataFrame({
        'task_name': ['Task 1', 'Task 2', 'Task 3'],
        'duration': [30, 60, 90],
        'cognitive_cost': [10, 20, 30],
        'priority': [3,6,9]
    })

time_budget = 90
cog_budget = 30


def test_knapsack():

    scheduled, unscheduled = knapsack(tasks, cog_budget ,time_budget)
    # Check  lists are not empty
    assert len(scheduled) > 0
    assert len(unscheduled) > 0

    # Check if scheduled priority score == 9
    priority_map = dict(zip(tasks['task_name'], tasks['priority']))
    total_priority = sum(priority_map[v] for v in scheduled)
    assert total_priority == 9

    # Check if budgets are not exceeded
    cognitive_cost_map = dict(zip(tasks['task_name'], tasks['cognitive_cost']))
    duration_map = dict(zip(tasks['task_name'], tasks['duration']))
    total_cog = sum(cognitive_cost_map[v] for v in scheduled)
    total_duration = sum(duration_map[v] for v in scheduled)

    assert total_cog <= cog_budget
    assert total_duration <= time_budget

    # Check all tasks are stored in scheduled and unscheduled
    num_scheduled = len(scheduled)
    num_unscheduled = len(unscheduled)
    assert (len(tasks['task_name']) == num_scheduled+num_unscheduled)


def test_greedy():
    p_scheduled, p_unscheduled = greedy(tasks, time_budget, greedy_type = 0)
    d_scheduled, d_unscheduled= greedy(tasks, time_budget, greedy_type = 1)
    r_scheduled, r_unscheduled= greedy(tasks, time_budget, greedy_type = 2)

    # Check lists are not empty
    assert len(p_scheduled) > 0
    assert len(d_scheduled) > 0
    assert len(r_scheduled) > 0
    assert len(p_unscheduled) > 0
    assert len(d_unscheduled) > 0
    assert len(r_unscheduled) > 0

    # Check if tasks are being optimized correctly
    assert 'Task 3' in p_scheduled
    assert 'Task 1', 'Task 2' in d_scheduled
    assert 'Task 3' in r_scheduled

    # Check if task budget is not exceeded
    duration_map = dict(zip(tasks['task_name'], tasks['duration']))
    p_total_duration = sum(duration_map[v] for v in p_scheduled)
    d_total_duration = sum(duration_map[v] for v in d_scheduled)
    r_total_duration = sum(duration_map[v] for v in r_scheduled)

    assert p_total_duration <= time_budget
    assert d_total_duration <= time_budget
    assert r_total_duration <= time_budget

    # Check all tasks are stored in scheduled and unscheduled
    num_p_scheduled = len(p_scheduled)
    num_p_unscheduled = len(p_unscheduled)
    assert (len(tasks['task_name']) == num_p_scheduled + num_p_unscheduled)


    num_d_scheduled  = len(d_scheduled)
    num_d_unscheduled = len(d_unscheduled)
    assert (len(tasks['task_name']) == num_d_scheduled + num_d_unscheduled)

    num_r_scheduled = len(r_scheduled)
    num_r_unscheduled = len(r_unscheduled)
    assert (len(tasks['task_name']) == num_r_scheduled + num_r_unscheduled)

def test_scorecard():
    scheduled, unscheduled = knapsack(tasks, cog_budget, time_budget)
    p_scheduled, p_unscheduled = greedy(tasks, time_budget, greedy_type=0)
    d_scheduled, d_unscheduled = greedy(tasks, time_budget, greedy_type=1)
    r_scheduled, r_unscheduled = greedy(tasks, time_budget, greedy_type=2)

    results = {
        "knapsack": {"scheduled": scheduled, "unscheduled": unscheduled},
        "greedy_priority": {"scheduled": p_scheduled, "unscheduled": p_unscheduled},
        "greedy_duration": {"scheduled": d_scheduled, "unscheduled": d_unscheduled},
        "greedy_ratio": {"scheduled": r_scheduled, "unscheduled": r_unscheduled},
    }

    scorecard = build_score_card(tasks, results, cog_budget, time_budget)


    #expected_columns =
    assert list(scorecard.columns) == ['Algorithm', 'Priority Score (%)', 'Time Utilization (%)', 'Cognitive Utilization (%)',
                        'Tasks Utilization (%)']

