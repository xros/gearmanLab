from gearman import GearmanClient
gearman_client = GearmanClient(['127.0.0.1:4730'])
# The 'echo' is the function named and registered in a worker: 'my_worker' in the 'gmwork.py'
# The 'foo' is the data which is passed to the the worker to be handled
gearman_request = gearman_client.submit_job('echo','foo',wait_until_complete=True)
result_data = gearman_request.result
print result_data
