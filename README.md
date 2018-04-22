# Scheduled Provisioning for SageMaker notebook
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
* [CreateSagemakerNotebook](https://github.com/hongpham/Schedule-provisioning-SageMaker-Notebook/blob/master/bin/Lambda_CheckSageMakerNotebookStatus.py): in this example you're creating an ml.t2.medium Notebook instance. Events in Amazon CloudWatch Events are represented a JSON object. To see an example CloudWatch Evens, follow this [link](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html). Step Functions will take CloudWatch Events as input data, and pass it to CreateSageMakerNotebook function. When new Notebook instance is succesfully created, Lambda will return NotebookInstanceARN, which can be passed on to the next function - CheckSageMakerNotebookStatus
* [CheckSageMakerNotebookStatus](https://github.com/hongpham/Schedule-provisioning-SageMaker-Notebook/blob/master/bin/Lambda_CheckSageMakerNotebookStatus.py): this function will describe current status of new Notebook instance
* [SendEmailNotification](https://github.com/hongpham/Schedule-provisioning-SageMaker-Notebook/blob/master/bin/SendEmailNotification.py): if the new instance is InService, this Lambda function will push a message to SNS


## Create Step Functions state machine
Follow steps in this [instruction](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-creating-lambda-state-machine.html#create-lambda-state-machine-step-4) to create state machine. In the Code pane, copy and past [this state machine definition](https://github.com/hongpham/Schedule-provisioning-SageMaker-Notebook/blob/master/bin/StepFunctions_satemachines_definition.json). Please make sure to update the ARN of the Lambda functions that you created earlier.

## Set up SNS Topic
Follow steps in this [instruction](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) to create an SNS topic. Then you can [create subscription](https://docs.aws.amazon.com/sns/latest/dg/SubscribeTopic.html) and start receiving email when Notebook instance is succesfully create
## Set up CloudWatch Events rules
To set up CloudWatch Events that trigger Step Functions, please follow [this tutorial](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-cloudwatch-events-target.html)

# Delete resources
This example is not tested in Production. After running this example, please delete all related resources to avoid unnecssary costs.
