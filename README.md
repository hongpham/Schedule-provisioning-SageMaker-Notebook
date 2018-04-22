# Automate-provisioning-SageMaker-Notebook
Using Amazon CloudWatch Events to trigger Amazon Step Functions to provisioned SageMaker Notebook instance

![Architecture Diagram](https://github.com/hongpham/Schedule-provisioning-SageMaker-Notebook/blob/master/images/Architecture%20diagram.png)


# Running the example

## Create neccessary IAM Roles
In this example, you will need to create 4 IAM roles
* IAM roles for Lambda function to create SageMaker notebook and push notification to SNS
* IAM roles for SageMaker to manage underlying resources
* IAM roles for Step Functions to trigger Lambda functions
* IAM roles for CloudWatch event to trigger Step Functions state machine

## Create Lambda Functions

There will be 3 Lambda functions used in this example. 
* CreateSagemakerNotebook: in this example you're creating an ml.t2.medium Notebook instance. Events in Amazon CloudWatch Events are represented a JSON object. To see an example CloudWatch Evens, follow this [link](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html). Step Functions will take CloudWatch Events as input data, and pass it to CreateSageMakerNotebook function. When new Notebook instance is succesfully created, Lambda will return NotebookInstanceARN, which can be passed on to the next function - CheckSageMakerNotebookStatus
* CheckSageMakerNotebookStatus: this function will describe current status of new Notebook instance
* SendEmailNotification: if the new instance is InService, this Lambda function will push a message to SNS


## Create Step Functions state machine

## Set up SNS Topic

## Set up CloudWatch Event rules
