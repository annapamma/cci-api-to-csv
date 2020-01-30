# pull out workflows
# turn workflows to csv

"""
{
    workflow_a: {
        job_1: 10,
        job_2: 5
    },
    workflow_b: {
        job_1: 10,
        job_2: 5
    },
}
"""

import functions as f
import os
import pandas as pd

circle_token = os.getenv('CIRCLE_TOKEN')

project_slug = "gh/annapamma/sandbox"
workflows_endpoint = f"https://circleci.com/api/v2/insights/{project_slug}/workflows"

workflows = f.make_request(workflows_endpoint, circle_token)

workflows_dataframe = pd.DataFrame.from_dict(workflows['items'])

print(workflows_dataframe)
workflows_dataframe.to_csv('workflows_dataframe.csv')
