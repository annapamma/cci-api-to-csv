import os
import random
import time

from flask import Flask, request, send_file, after_this_request, redirect

import functions as f

app = Flask(__name__)

# circle-token from query-params


@app.route('/')
def hello():
    return 'hello!'


@app.route('/api/v2/insights/<vcs>/<org>/<project>/workflows')
def workflows(vcs, org, project):
    circle_token = request.args.get('circle-token')
    df = f.insights_workflows(project_slug=f'{vcs}/{org}/{project}', circle_token=circle_token)
    seconds = time.time()
    rand_int = random.getrandbits(128)
    f_name = f'insights_workflows_{seconds}_{rand_int}.csv'
    df.to_csv(f_name, index=False)

    @after_this_request
    def remove_file(response):
        os.remove(f_name)
        return response

    try:
        return send_file(f_name,
                         attachment_filename='insights_workflows.csv',
                         mimetype='text/csv',
                         as_attachment=True,
                         cache_timeout=-1)

    except Exception as e:
        return str(e)


@app.route('/api/v2/insights/<vcs>/<org>/<project>/workflows/<workflow_name>/jobs/<job_name>')
def jobs(vcs, org, project, workflow_name, job_name):
    circle_token = request.args.get('circle-token')
    df = f.insights_workflows(project_slug=f'{vcs}/{org}/{project}', circle_token=circle_token)
    seconds = time.time()
    rand_int = random.getrandbits(128)
    f_name = f'insights_workflows_{seconds}_{rand_int}.csv'
    df.to_csv(f_name, index=False)

    @after_this_request
    def remove_file(response):
        os.remove(f_name)
        return response

    try:
        return send_file(f_name,
                         attachment_filename='insights_workflows.csv',
                         mimetype='text/csv',
                         as_attachment=True,
                         cache_timeout=-1)

    except Exception as e:
        return str(e)