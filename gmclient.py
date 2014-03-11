from gearman import GearmanClient
gearman_client = GearmanClient(['127.0.0.1:9000'])
gearman_request = gearman_client.submit_job('echo','foo',wait_until_complete=True)
result_data = gearman_request.result
print result_data
