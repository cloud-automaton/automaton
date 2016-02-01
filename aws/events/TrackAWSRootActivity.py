import boto3

def lambda_handler(event, context):
    try:
        if event['detail']['userIdentity']['type'] == 'Root' and  'accessKeyId' in event['detail']['userIdentity']:
            print 'user type : ',event['detail']['userIdentity']['type']
            print 'access key :',event['detail']['userIdentity']['accessKeyId']
            print 'root acc has been used to access the APIs'
            sns_client = boto3.client('sns')
            sns_client.publish( TopicArn='arn:aws:sns:us-east-1:<account_number>:notify_me',Message='Root Account has been used to access EC2 APIs. Please check.', Subject='Root Account Usage Notification')
    except Exception, e:
        print e
