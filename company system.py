import random

client_database=dict()

#we create the client class

class client:
    def __init__(self,client_name):
        self.client_name=client_name
        client_name=str()

#we create the function that assigns a number as an "ID" to a client then adds it to the client database
         
def register_client(client_name):
    client.id=random.choice([2501,20501])
    client_database[client.id]=client_name
    return(f"{client_name} has been registered.id is {client.id}")

#Below are some examples that I used to test the function

#david=client("david")

#print(registerclient("david"))

#we create the function that suspends a client's account by deleting it from the client database

def suspend_client_account(client_name):
    client_database.pop(client.id)
    return(f"{client_name}'s account has been deleted from the client database")

#print(suspend_client_account("david"))

staff_database=dict()

#we create the worker class

class worker:
    def __init__(self,worker_name,function):
        self.worker_name=worker_name
        self.function=function
        worker_name=str()
        function=str()
        
#we create the function that suspends a worker's account by deleting it from the staff database
        
def suspend_worker_account(worker_name):
    staff_database.pop(worker.id)
    print(f"{worker_name}'s account has been suspended")
    
    
def register_worker(worker_name):
    worker.id=random.choice([450000,1000000])
    staff_database[worker.id]=worker_name
    print(f"{worker_name} has been registered. id is {worker.id}")
    
    
    
john=worker("john","manager")
print(register_worker("john"))

print(suspend_worker_account("john"))