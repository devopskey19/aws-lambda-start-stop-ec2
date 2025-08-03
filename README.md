# AWS Pyton Lambda function to start / stop EC2 instance
Lambda function code is mentioned in main.py file this code is tested with python 3.10 and above

**Note: Update ACCOUNT-ID with your account before using**

Policy file structure : 
1. policy/ec2_start_stop_policy.json :- contains policy for Lambda function role to execute instance start / stop , instance list and cloudwatch log create / update
2. policy/ec2_start_stop_trust_policy.json :- contains trust policy for Lambda function role
3. policy/event_bridge_scheduler_policy.json :- contains policy for event bus schedulers, it allows event scheduler to invoke lambda function
4. policy/event_bridge_scheduler_trust_policy.json :- contains trust policy for event bus scheduler
