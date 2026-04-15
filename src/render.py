from jinja2 import Environment, FileSystemLoader
import os

def highlight_over_budget(val):
    """
    Checks if cognitive utilization is higher than the budget and changes the style
    :param val: [int] Cognitive Utilization value
    :return: [str] styling command that will change the font of the affected values to red
    """
    return 'color: red' if val > 100 else ''

def render_results(results, scorecard_df, output_path="output/results.html"):
    """
    Renders results in html file for readability
    :param results: [dict] Results dictionary
    :param scorecard_df: [pd.DataFrame] Scorecard dataframe
    :param output_path: [string] Path to output html file
    :return: none
    """
    env = Environment(loader=FileSystemLoader("../templates/"))
    template = env.get_template("results.html")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    scorecard_df = scorecard_df.style.map(highlight_over_budget, subset=['Cognitive Utilization (%)'])
    html = template.render(results=results, scorecard=scorecard_df.to_html(classes = 'table table-hover table-bordered table-striped', index=False))
    with open(output_path, "w") as f:
        f.write(html)
    with open(output_path, "w") as f:
        f.write(html)