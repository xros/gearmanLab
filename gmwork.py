import os
import gearman
import math
class MyGearmanWorker(gearman.GearmanWorker):
    def on_job_execute(self, current_job):
        print 'Job started'
        return super(MyGearmanWorker, self).on_job_execute(current_job)

def task_callback(gearman_worker, gearman_job):
    print gearman_job.data + ' is done by a gearman cute worker'
    return gearman_job.data + ' is done by a gearman cute worker'


# An worker instance to listen
my_worker = MyGearmanWorker(['127.0.0.1:4730'])
# register a task: its name is echo, and its function is task_callback
my_worker.register_task('echo', task_callback)
my_worker.work()
