from flask import send_file
import json
import urllib.request
import os
import pandas as pd

# circle_token = os.getenv('CIRCLE_TOKEN')


def make_request(endpoint, circle_token):
    header = {
        'Circle-Token': circle_token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    req = urllib.request.Request(endpoint, headers=header)
    return json.loads(urllib.request.urlopen(req).read())


def flatten_dict_duration(d, a):
    for k, v in d.items():
        new_k = f"duration_{k}"
        a[new_k] = v


def insights_workflows(project_slug, circle_token):
    workflows_endpoint = f"https://circleci.com/api/v2/insights/{project_slug}/workflows"

    workflows = make_request(workflows_endpoint, circle_token)['items']

    processed_workflows = []
    for workflow in workflows:
        processed_workflow = {
            'name': workflow['name'],
            'window_start': workflow['window_start'],
            'window_end': workflow['window_end'],
            **workflow['metrics'],
        }
        flatten_dict_duration(workflow['metrics']['duration_metrics'], processed_workflow)
        del processed_workflow['duration_metrics']
        processed_workflows.append(processed_workflow)
    workflows_dataframe = pd.DataFrame.from_records(processed_workflows)
    return workflows_dataframe


def insights_jobs(project_slug, circle_token, workflow_name, job_name):
    jobs_endpoint = f"https://circleci.com/api/v2/insights/{project_slug}/workflows/{workflow_name}/jobs/{job_name}"

    jobs = make_request(jobs_endpoint, circle_token)['items']

    jobs_dataframe = pd.DataFrame.from_records(jobs)
    return jobs_dataframe



