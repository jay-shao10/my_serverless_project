from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_sqs as sqs,
)
from constructs import Construct

class MyServerlessProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        queue=sqs.Queue(self,"AWS_lab_Queue")
        post_lambda=_lambda.Function(
            self,"PostLambdaHandler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="post_lambda.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                'QUEUE_URL': queue.queue_url
            }
        
        )
        queue.grant_send_messages(post_lambda)
        # Create Lambda function to handle GET requests
        get_lambda = _lambda.Function(
            self, "GetLambdaHandler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="get_lambda.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                'QUEUE_URL': queue.queue_url
            }
        )
        queue.grant_consume_messages(get_lambda)

        # Create API Gateway
        api = apigateway.RestApi(self, "AWS_lab_API",
            rest_api_name="AWS LAB Service",
            description="This service serves the AWS LAB.")

        post_integration = apigateway.LambdaIntegration(post_lambda)
        get_integration = apigateway.LambdaIntegration(get_lambda)

        api.root.add_method("POST", post_integration)
        api.root.add_method("GET", get_integration)