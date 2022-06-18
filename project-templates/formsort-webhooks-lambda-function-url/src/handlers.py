import os
import logging

import boto3
import base64
import hashlib
import hmac

from src.codedeploy import pass_deployment, fail_deployment

logger = logging.getLogger()

SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL")
SIGNING_KEY = os.getenv("FORMSORT_SIGNING_KEY", "your-signing-key")


def hmac_sign(signing_key, original_request_body):
    key = signing_key.encode("utf8")
    message = original_request_body.encode("utf8")
    return (
        base64.urlsafe_b64encode(
            hmac.new(key, message, hashlib.sha256).digest())
            .rstrip(b"=")
            .decode("utf8")
    )


def pre_traffic_hook_handler(event, context):
    logger.info("Starting pre-traffic hook...")
    try:
        logger.info("Running pre-traffic hook...")
        pass_deployment(event)
    except:
        fail_deployment(event)
        raise
    logger.info("Finished pre-traffic hook.")


def post_traffic_hook_handler(event, context):
    logger.info("Starting post-traffic hook...")
    try:
        logger.info("Running post-traffic hook...")
        pass_deployment(event)
    except:
        fail_deployment(event)
        raise
    logger.info("Finished post-traffic hook.")


unauthorized = {
            "statusCode": 401,
            "body": "forbidden"
        }

successful = {
    "statusCode": 200,
    "body": "successful"
}


def handler(event, context):
    # Verify Signature
    if not event["headers"].get("x-formsort-signature"):
        return unauthorized
    signature = hmac_sign(SIGNING_KEY, event["body"])
    if signature != event["headers"]["x-formsort-signature"]:
        return unauthorized

    # Send Message to Queue
    sqs = boto3.resource("sqs")
    answers_queue = sqs.Queue(SQS_QUEUE_URL)
    answers_queue.send_message(MessageBody=event["body"])
    return successful
