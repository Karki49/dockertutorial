import boto3


client = boto3.client('batch')

for i in range(0,3):
	containerOverrides={
        'environment': [
            {
                'name': 'passedValue',
                'value': 'passedValue-%s' %i
            }
        ]
    }
	jobName = "jobname%s" %i
	print(containerOverrides)
	client.submit_job(jobName=jobName, jobQueue='first-run-job-queue', 
	jobDefinition="first-job:1", containerOverrides=containerOverrides)
	print("submitted")