import boto3

sagemakerClient = boto3.client('sagemaker')

def lambda_handler(event, context):
    #this fuction create new Notebook and names it based on CloudWatch event ID
    CWeventID = event['id']

    # create new Notebook Instances

    createNewNotebook = sagemakerClient.create_notebook_instance(
    NotebookInstanceName=CWeventID, #name instance using CloudWatch event ID
    InstanceType='ml.t2.medium', # isntance type
    RoleArn='arn:aws:iam::1234567890:role/service-role/AmazonSageMaker-ExecutionRole-20101010T105609' #SageMaker Role
    )
    return(createNewNotebook.get('NotebookInstanceArn'))
