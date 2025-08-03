import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('ec2')
    #approach 1
    # client.stop_instances(InstanceIds=['i-00017002b4735c54e'])
    # approach 2 
    print(event['State'])
    ec2_list = client.describe_instances(
        Filters=[
        {
            'Name': 'tag:Schedule',
            'Values': [
                'True',
                'true'
            ]
        },
        ]
    )
    # print(ec2_list)
    for reservation in ec2_list['Reservations']:
        for instance in reservation['Instances']:
            print(instance['InstanceId'])
            print(instance['State']['Name'])
            instance_state = instance['State']['Name']
            if instance_state == 'running' and event['State'] == 'Stop':
                print('Stop instance')
                client.stop_instances(InstanceIds=[instance['InstanceId']])
            elif instance_state == 'stopped' and event['State'] == 'Start':
                print('Start instance')
                client.start_instances(InstanceIds=[instance['InstanceId']])
            else : 
                print('Do nothing')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
