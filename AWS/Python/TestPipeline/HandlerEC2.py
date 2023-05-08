import boto3
import json 
import datetime 

class EC2Security:

    def __init__(self):
        
        self.__client = boto3.client('ec2')
    
    
    def createSecurityGroup(self, listResources = list, description = str, groupName = str, vpcId= str, key= "", value = ""): 
        
        #TODO a logic like reserveAddress were it alllows
        record = []

        for r in range(len(listResources)):

            response = self.__client.create_security_group(

                Description= description,
                GroupName= groupName,
                VpcId=vpcId,
                TagSpecifications=[
                    {
                        'ResourceType': listResources[r],
                        'Tags': [
                            {
                                'Key': key,
                                'Value': value
                            },
                        ]
                    },
                ],
                
            )
        record.append(response)

        return record
    
class EC2GeneralPurposeTasks(): 

    def __init__(self):
        
        self.__client = boto3.client('ec2')
        self.__recordTime =  datetime.datetime.now()
    

    """ Networking Section """

    #Loops and allocates an all Elastic IP address for each resource type requested. Then returns a list of requests. 
    def reserveAddress(self, listResources: list, domain = str,  optionalResource = None,  address = str, publicIpv4Pool= str, networkBorderGroup= str, customerOwnedIpv4Pool = str, key = "", value = ""):  
        lowercaseDomain = domain.lower() 
        record = []
        
        # Creates a specfic resource
        if optionalResource !=  None: 

            requestedResouce = listResources[optionalResource]

            response = self.__client.allocate_address (

                            Domain = lowercaseDomain,
                            Address = address,
                            PublicIpv4Pool = publicIpv4Pool,
                            NetworkBorderGroup = networkBorderGroup,
                            CustomerOwnedIpv4Pool = customerOwnedIpv4Pool,
                            TagSpecifications = [
                                {
                                    'ResourceType': requestedResouce,
                                    'Tags': [
                                        {
                                            'Key': key,
                                            'Value': value
                                        },
                                    ]
                                },
                            ]
                    )
            
            ## Recording data
            record.append(response)
            jsonRecord = json.dumps(record, indent=4)
            recordTime = self.__recordTime
            service = "allocate_address"
            

            # Writing to json file 
            with open(f"Cloud/AWS/Python/TestEC2Pipeline/jsonrecords/{recordTime} {service} record.json", "w") as storeRecord:
                storeRecord.write(jsonRecord)
            
        
            return record

        ## Looks up every resource in standard 
        elif optionalResource  ==  None: 
        
            if lowercaseDomain == "standard": 
            
                for r in range(len(listResources)): 
                    
                    response = self.__client.allocate_address (
                            Domain = lowercaseDomain,
                            Address = address,
                            PublicIpv4Pool = publicIpv4Pool,
                            NetworkBorderGroup = networkBorderGroup,
                            CustomerOwnedIpv4Pool = customerOwnedIpv4Pool,
                            TagSpecifications = [
                                {
                                    'ResourceType': listResources[r],
                                    'Tags': [
                                        {
                                            'Key': key,
                                            'Value': value
                                        },
                                    ]
                                },
                            ]
                    )
    
                    record.append(response)

                ## Recording data
                record.append(response)
                jsonRecord = json.dumps(record, indent=4)
                recordTime = self.__recordTime
                service = "allocate_address"

                # Writing to json file 
                with open(f"Cloud/AWS/Python/TestEC2Pipeline/jsonrecords/{recordTime} {service} record.json", "w") as storeRecord:
                    storeRecord.write(jsonRecord)

                return record
             
            ## Looks up every resource in standard 
            elif lowercaseDomain == "vpc":

                for r in range(len(listResources)): 
                    
                    response = self.__client.allocate_address (
                            Domain = lowercaseDomain,
                            Address = 'string',
                            PublicIpv4Pool = 'string',
                            NetworkBorderGroup = 'string',
                            CustomerOwnedIpv4Pool = 'string',
                            TagSpecifications = [
                                {
                                    'ResourceType': listResources[r],
                                    'Tags': [
                                        {
                                            'Key': 'string',
                                            'Value': 'string'
                                        },
                                    ]
                                },
                            ]
                    )
                record.append(response)

                ## Recording data
                record.append(response)
                jsonRecord = json.dumps(record, indent=4)
                recordTime = self.__recordTime
                service = "allocate_address"

                # Writing to json file 
                with open(f"Cloud/AWS/Python/TestEC2Pipeline/jsonrecords/{recordTime} {service} record.json", "w") as storeRecord:
                    storeRecord.write(jsonRecord)
                
                return record 
        
            else: 

                raise LookupError("Error your request domain does not exist: try vpc or standard.")
            
    # List of the Regions supported by Amazon EC2 
    def getSupportRegions(self, name = str, values = str , regionNames = str, allRegions = bool):
        response = self.__client.describe_regions(
            Filters=[
                {
                    'Name': name,
                    'Values': [
                        values,
                    ]
                },
            ],
            RegionNames=[
                regionNames,
            ],
          
            AllRegions= allRegions
        )

        return response

class EC2ComputeOptimized(): 

    def __init__(self):
        
        self.__client = boto3.client('ec2') 


class EC2MemoryOptimized():

     def __init__(self):
        
        self.__client = boto3.client('ec2') 

class EC2AcceleratedOptimized():
     
     def __init__(self):
        
        self.__client = boto3.client('ec2') 