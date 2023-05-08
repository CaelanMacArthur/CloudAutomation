from localstack_client.patch import enable_local_endpoints
from HandlerEC2 import EC2GeneralPurposeTasks
from HandlerEC2 import EC2Security 
from HandlerEC2 import  EC2ComputeOptimized 
from HandlerEC2 import EC2MemoryOptimized
from HandlerEC2 import  EC2AcceleratedOptimized 
from DataAnalysis import AnalyzeEC2 


# from DataAnalysis import AnalyzeEC2


def main(): 
        
    # Redirect to local endpionts 
    enable_local_endpoints()

    # New objects 
    ec2GeneralPurposeTasks = EC2GeneralPurposeTasks()
    ec2Security =  EC2Security() 
    ec2ComputeOptimized = EC2ComputeOptimized() 
    ec2MemoryOptimized = EC2MemoryOptimized() 
    ec2AcceleratedOptimized = EC2AcceleratedOptimized()

    # List of resources or services 
    listResources = ['capacity-reservation','client-vpn-endpoint','customer-gateway','carrier-gateway','coip-pool','dedicated-host','dhcp-options','egress-only-internet-gateway','elastic-ip','elastic-gpu','export-image-task','export-instance-task','fleet','fpga-image','host-reservation','image','import-image-task','import-snapshot-task','instance','instance-event-window','internet-gateway','ipam','ipam-pool','ipam-scope','ipv4pool-ec2','ipv6pool-ec2','key-pair','launch-template','local-gateway','local-gateway-route-table','local-gateway-virtual-interface','local-gateway-virtual-interface-group','local-gateway-route-table-vpc-association','local-gateway-route-table-virtual-interface-group-association','natgateway','network-acl','network-interface','network-insights-analysis','network-insights-path','network-insights-access-scope','network-insights-access-scope-analysis','placement-group','prefix-list','replace-root-volume-task','reserved-instances','route-table','security-group','security-group-rule','snapshot','spot-fleet-request','spot-instances-request','subnet','subnet-cidr-reservation','traffic-mirror-filter','traffic-mirror-session','traffic-mirror-target','transit-gateway','transit-gateway-attachment','transit-gateway-connect-peer','transit-gateway-multicast-domain','transit-gateway-policy-table','transit-gateway-route-table','transit-gateway-route-table-announcement','volume','vpc','vpc-endpoint','vpc-endpoint-connection','vpc-endpoint-service','vpc-endpoint-service-permission','vpc-peering-connection','vpn-connection','vpn-gateway','vpc-flow-log','capacity-reservation-fleet','traffic-mirror-filter-rule','vpc-endpoint-connection-device-type','verified-access-instance','verified-access-group','verified-access-endpoint','verified-access-policy','verified-access-trust-provider','vpn-connection-device-type','vpc-block-public-access-exclusion','ipam-resource-discovery','ipam-resource-discovery-association']
    optionalResource = 0
   
    # Agurements taken list of resources, domain type, and default type none for 
    # Allocate Elastic IP address for each resource type requested

    # Request specfic resource without key and value
    # ec2GeneralPurposeTasks.reserveAddress(listResources, "vpc",optionalResource, '', 'string', '', '')

    # Request all available types without key and value 
    ec2GeneralPurposeTasks.reserveAddress(listResources, "standard", None, '', '', '', '')


    # List of the Regions supported by Amazon EC2 
    # print(ec2GeneralPurposeTasks.getSupportRegions("", "", "", False))
    # List all regions
    # print(ec2GeneralPurposeTasks.getSupportRegions("", "", "", True))


if __name__ == "__main__": 
    main() 
