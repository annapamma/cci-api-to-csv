# cci-api-to-csv

This is a workaround for customers to hit a CircleCI API endpoint and receive a CSV in response. To use this, you need a [CircleCI token](https://circleci.com/docs/2.0/managing-api-tokens/). 


## Available endpoints

Get summary metrics for a project's workflows
```
circleci.com/api/v2/insights/{project-slug}/workflows?circle-token={CIRCLETOKEN}
```
Get recent runs of a workflow job
```
circleci.com/insights/{project-slug}/workflows/{workflow-name}/jobs/{job-name}?circle-token={CIRCLETOKEN}
```
## To use

Replace "circleci.com" with "api-to-csv.herokuapp.com"
ie:
```
api-to-csv.herokuapp.com/insights/{project-slug}/workflows/{workflow-name}/jobs/{job-name}
```

## Notes
Reference
Please see more information from the [CircleCI API v2 docs](https://circleci.com/docs/api/v2/#circleci-api-insights)


This is not an official CircleCI endpoint or solution by any means.

Contributions welcome via issues or pull request. 

