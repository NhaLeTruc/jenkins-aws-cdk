import aws_cdk as core
import aws_cdk.assertions as assertions

from jenkins_aws_cdk.jenkins_aws_cdk_stack import JenkinsAwsCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in jenkins_aws_cdk/jenkins_aws_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = JenkinsAwsCdkStack(app, "jenkins-aws-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
