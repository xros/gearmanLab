gearmanLab
==========
Instruction
---------
### Install gearman client and gearman server
* on ubuntu/debian ```sudo apt-get install gearman-job-server gearman-tools -y``` You can find useful information [HERE](http://gearman.org/getting-started/)
* From the link above it will show you how to use command lines to pass jobs from client via server to worker. Even though it's in PHP I think it's very neat and handy.

### After installation. Please follow the steps below:
-   1) start the gearmand daemon: ```$ sudo gearmand -p4730``` -p means port
-   2) write a worker. In this example, its name is ```gmwork.py```
-   3) write a client. In this example, its name is ```gmclient.py```
-   4) start the work as for the worker ```$ sudo python gmwork.py ```
-   5) start the client ```$ sudo python gmclient.py```

### See what we got
#### Then you will see something like this, everytime you do the client:

```root@raspberrypi /home/pi/sanbox/gearmanLab # python gmclient.py ```

 foo is done by a gearman cute worker  

*****
* From the work(er) daemon we will see this:

```root@raspberrypi /home/pi/sanbox/gearmanLab # python gmwork.py```
 Job started

 foo is done by a gearman cute worker 
*****
 So now gearman works well with python. Happy hacking!
