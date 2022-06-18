import os

import boto3
import pytest


@pytest.fixture
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture
def sqs_client(aws_credentials):
    with mock_sqs():
        yield boto3.client("sqs")


@pytest.fixture
def a_lambda_url_event():
    def _a_lambda_url_event(headers=None, body=None):
        return {
            "headers": headers or {},
            "body": body or '{"hello": "world"}'
        }
    return _a_lambda_url_event


@pytest.fixture
def answers_queue():
    pass
