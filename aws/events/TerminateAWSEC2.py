import boto3

def lambda_handler(event, context):
    #print ("Received event: " + json.dumps(event, indent=2))
    #print ("************************************************")
    
    ec2_client = boto3.client("ec2")
    
    
    print "Event Region :", event['region']
    
    event_time = event['detail']['eventTime']
    print "Event Time :", event_time
    
    time = event_time.split('T')
    t = time[1]
    t = t.split(':')
    hour = t[0]
    
    instance_type = event['detail']['requestParameters']['instanceType']
    print "Instance Type:", instance_type
    
    instance_id = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']
    print "Instance Id:",instance_id
    
    if( instance_type.startswith( 't' ) and hour > 18 or hour < 8 ):
        print ec2_client.terminate_instances( InstanceIds = [ instance_id ] )
