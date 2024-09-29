import aws_cdk as core
import aws_cdk.assertions as assertions

from my_serverless_project.my_serverless_project_stack import MyServerlessProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_serverless_project/my_serverless_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MyServerlessProjectStack(app, "my-serverless-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
