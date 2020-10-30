# Listing objects in S3 bucket, filter by modified date
# https://stackoverflow.com/questions/59143045/how-to-filter-s3-objects-by-last-modified-date-with-boto3

import boto3
import datetime

#bucket Name
bucket_name = 'bucket_name'
#folder Name
folder_name = 'folder_name/'

#bucket Resource
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name) 

# filter modified date
YEAR = 2020
MONTH = 10
DAY = 25

# create empty dictionary to store results by date
di_date_s3filename = {}

for file in bucket.objects.filter(Prefix= folder_name):
    
    #compare dates 
    if (file.last_modified).replace(tzinfo = None) > datetime.datetime(YEAR,MONTH,DAY,tzinfo = None):
        
        str_file_date_modified = str(file.last_modified)
        str_folder_filename = str(file.key)
        
        #print results
        print(f'File Name: {str_folder_filename}')
        print(f'Date: {str_file_date_modified}')
        print()
        
        di_date_s3filename[str_file_date_modified] = str_folder_filename
        
# print out the keys which are modified dates
_ = [print(x, '\n') for x in sorted(di_date_s3filename.keys()) ]

