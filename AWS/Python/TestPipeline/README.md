## Function Definitions <br><br>

#### TestPipline creates an automated Python that runs and builds AWS services. It aims to allow developers to test AWS services without racketing an AWS bill. The function reserveAddress implements the python AWS sdk ec2 allocate_address function. It finds resources based on the requested domain or a specific resource. It also analyzes the JSON response headers' development status and networking traffic. <br><br>

#### Addtion

## Requirements <br><br>

### Requirements that are needed is Golang, Python, Docker, Localstack, Elastic Search, and Kubernetes. <br>

* Golang install: https://go.dev/doc/install 
* Python install: https://www.python.org/downloads/
* Docker install: https://docs.docker.com/get-docker/ 
* Localstack install: https://docs.localstack.cloud/getting-started/installation/ 
<br>

####  Additionally, you will need to install two third party libraries with pip for the Python modules. 
* Create the venv folder:  python3 -m venv venv
* Activate venv MacOs/Linux:  source venv/bin/activate 
* Activate venv Windows: source venv\Scripts\activate
* localstack-client: pip install localstack-client
* boto3: pip install boto3 
* ydata_profilin: pip install ydata_profilin  
* numpy: pip install numpy
* flask: pip install Flask 
<br><br>

#### Thrird party library functionality: localstack-client ensures all traffic goes to local endpoints, and boto3 is a Python SDK from Amazon to create cloud applications.  <br><br>

#### For these modules is recommended to use a Python virtual enivorment and install the Python thrid party libraries there. Below is a reference document about how. <br><br> 

* https://docs.python.org/3/library/venv.html 

<br>

## Notes <br> <br>

####  To disable your traffic from going to AWS, but instead goes to local endpoints. It would help if you utilized localstack-client function enable_local_endpoints() in your main file: 

```python
from localstack_client.patch import enable_local_endpoints 
enable_local_endpoints() function 
```

#### If you want to test your applications are they run locally and pass all test then you can use in your main file and function:  

```python
from localstack_client.patch import disable_local_endpoints()
disable_local_endpoints() 
```

### To be noted:
#### <mark>This repo is still a work in progress and has a long way to go. </mark><br>

#### <mark> This project is apart of a larger project automation cloud project. The main repo is: https://github.com/CaelanMacArthur/CloudAutomation/tree/master  </mark>


