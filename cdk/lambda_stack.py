from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
)
from constructs import Construct
import os

class LambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Lambda execution role
        lambda_role = iam.Role(
            self,
            "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        # Create Lambda function
        self.lambda_function = _lambda.Function(
            self,
            "MyPythonLambda",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="app.lambda_handler",
            code=_lambda.Code.from_asset(os.path.join(os.getcwd(), "../src")),
            role=lambda_role,
            environment={
                "ENVIRONMENT": "dev"
            }
        )