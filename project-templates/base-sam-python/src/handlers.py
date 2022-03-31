import json
import logging

import boto3


logger = logging.getLogger()


def fail_deployment(event):
    deployment_id = event["DeploymentId"]
    lifecycle_event_hook_execution_id = event["LifecycleEventHookExecutionId"]
    client = boto3.client("codedeploy")
    client.put_lifecycle_event_hook_execution_status(
        deploymentId=deployment_id,
        lifecycleEventHookExecutionId=lifecycle_event_hook_execution_id,
        status="Failed"
    )


def pass_deployment(event):
    deployment_id = event["DeploymentId"]
    lifecycle_event_hook_execution_id = event["LifecycleEventHookExecutionId"]
    client = boto3.client("codedeploy")
    client.put_lifecycle_event_hook_execution_status(
        deploymentId=deployment_id,
        lifecycleEventHookExecutionId=lifecycle_event_hook_execution_id,
        status="Succeeded"
    )


def pre_traffic_hook():
    logger.info("Running pre-traffic hook...")


def pre_traffic_hook_handler(event, context):
    logger.info("Starting pre-traffic hook...")
    try:
        pre_traffic_hook()
        pass_deployment(event)
    except:
        fail_deployment(event)
        raise
    logger.info("Finished pre-traffic hook.")


def post_traffic_hook():
    logger.info("Running post-traffic hook...")


def post_traffic_hook_handler(event, context):
    logger.info("Starting post-traffic hook...")
    try:
        post_traffic_hook()
        pass_deployment(event)
    except:
        fail_deployment(event)
        raise
    logger.info("Finished post-traffic hook.")


def hello_world_handler(event, context):
    logger.info(json.dumps(event))
