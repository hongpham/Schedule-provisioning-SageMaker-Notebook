import boto3

sagemakerClient = boto3.client('sagemaker')
snsclient = boto3.client('sns')
notebookinstances = [];

def lambda_handler(event, context):

    #get list of current InService instances
    getCurrentInstances = sagemakerClient.list_notebook_instances(
    SortBy='CreationTime',
    SortOrder='Descending',
    StatusEquals='InService'
    )

    for items in getCurrentInstances["NotebookInstances"]:
        print("INSERVICE NOTEBOOK INSTANCES: " + items["NotebookInstanceName"])
        notebookinstances.append(items["NotebookInstanceName"])

    listofInstances= ', '.join(notebookinstances)
    composeMessage = "New Notebook instance created today: " +  notebookinstances[0] + "\n" + "List of InService Notebook: " + listofInstances

    #push message to SNS
    sendMessage = snsclient.publish(
    TopicArn='arn:aws:sns:us-west-2:1234567890:SageMaker-Notebooks',
    Message=composeMessage,
    Subject='List of notebookinstance',
    MessageStructure='string',
    )
