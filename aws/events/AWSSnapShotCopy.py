import json
import boto3
import boto3.session

def lambda_handler(event, context):

    print event.keys()
    
    srcRegion = event['detail']['requestParameters']['sourceRegion']
    destRegion = event['detail']['requestParameters']['destinationRegion']
    srcSnapshotId = event['detail']['requestParameters']['sourceSnapshotId']
    destSnapshotId = event['detail']['responseElements']['snapshotId']
    
    print "Executing copy snapshot lambda ......................"
    print "srcRegion : " + srcRegion
    print "destRegion : " + destRegion
    
    if srcRegion != destRegion:
        destSession = boto3.session.Session(region_name=destRegion)
        destEc2Client = destSession.client('ec2')
        destEc2Client.delete_snapshot(SnapshotId = destSnapshotId)
        print "Deleted snapshot (" + destSnapshotId + ") since snapshot is copied from " + srcRegion + " region to " + destRegion + " region"
    
