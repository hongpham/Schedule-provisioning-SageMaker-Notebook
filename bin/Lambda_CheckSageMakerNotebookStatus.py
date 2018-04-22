import boto3

sagemakerClient = boto3.client('sagemaker')

def lambda_handler(event, context):
    #event is the newly created NotebookInstanceARN
    #getting instane name from NotebookInstanceARN
    resource,instance = event.split('/')

    #getting status of new Notebook Instance
    response = sagemakerClient.describe_notebook_instance(
    NotebookInstanceName=instance
    )

    return(response.get('NotebookInstanceStatus'))
