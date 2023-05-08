## TestEC2Pipeline <br><br>

#### This repository is an example of setting up an automated service to test your EC2 instance using localstack and every available service has been implemented.<br><br>

## Notes <br> <br>

####  To disable your traffic from going to AWS, but instead goes to local endpoints. It would help if you utilized localstack-client function enable_local_endpoints() in your main file: e: 

```python
from localstack_client.patch import enable_local_endpoints 
enable_local_endpoints() function 
```

#### If you want to test your applications are they run locally and pass all test then you can use in your main file and function:  

```python
from localstack_client.patch import disable_local_endpoints()
disable_local_endpoints() 
```


