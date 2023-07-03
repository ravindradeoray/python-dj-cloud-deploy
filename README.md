# Python Django app 

 App created following tutorial page at djangoprojects.com. Ready to run locally and for additional changes to support cloud deployments. I will be using this app for AWS EB (elasticbeanstalk) demo.

 ## Running app locally
> Recommended to setup a virtual environment with python 3.9.x

- `cd python-dj-cloud-deploy`
- activate python virtual env
- `pip install -r  requirements.txt`
- setup env variable `export DEBUG=1` to activate local mode
- `python manage.py migrate` 
- `python manage.py loaddata polls`
- optonal `python manage.py createsuperuser`
- `python manage.py runserver`
- validate - http://127.0.0.1:8080/polls/

 ## Running app on AWS EB

### pre-requisites
- have a working aw accont
- for easy start, we will keep default vpc with all public subnets. In part 2 we will deal with network customization 
- install aws cli, aws eb cli
- setup account for cli, ensure you account has all necessary permissions. Start with non console admin role. 

### Application changes to support AWS and local
-- drive configuration using environment variables
Add env variable DEBUG=1 which will force application to run with Debug mode
if debug is not set of is set to anything other than '1' will be considered as production mode



### steps/commands to launch aws envrionment
- `eb init` - sets up eb application profile. answer questions related to setting up brand new eb application for first time. Follow aws tutotial if you need help
- `eb create`  - sets up new deployment. with its own unique CNAME which we need to add to settings.py as django needs for secure connection. Again AWS document explains at details
- if everything is fine till this point then you should have a working eb deployment 

### Validations 
- `eb logs`
- `eb ssh` - if you setup key propertly then you shoudl be able to ssh into ec2 instance running python/django here are important folders 
    - `/var/app/current` - For application working directory
    - `/var/log` - for application logs, if any of the startup command fails then you eb logs will just tell you one liner but if you ssh into ec2 instance then you will be able to check eb-init-cmd.log for details of startup command logs.


## Setup like a pro

### VPC 

### Logs

### Database

### Monitoring


