import boto3
import schedule
import time
import os

# AWS Region
REGION = os.getenv("AWS_REGION", "eu-central-1")

# Boto3 Clients
ec2_client = boto3.client('ec2', region_name=REGION)
ec2_resource = boto3.resource('ec2', region_name=REGION)


def check_instance_status():
    """
    Check the health status of EC2 instances and print their state.
    """
    try:
        statuses = ec2_client.describe_instance_status(IncludeAllInstances=True)
        for status in statuses['InstanceStatuses']:
            ins_status = status['InstanceStatus']['Status']
            sys_status = status['SystemStatus']['Status']
            state = status['InstanceState']['Name']
            print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status {sys_status}")
        print("#############################\n")
    except Exception as e:
        print(f"Error fetching instance statuses: {e}")


def main():
    """
    Schedule health checks and run indefinitely.
    """
    schedule.every(5).seconds.do(check_instance_status)
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)  # Prevents high CPU usage
    except KeyboardInterrupt:
        print("Script terminated by user.")


if __name__ == "__main__":
    main()
