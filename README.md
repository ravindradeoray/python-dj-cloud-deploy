# Python Django app 

 App created following tutorial page at djangoprojects.com. Ready to run locally and for additional changes to support cloud deployments. I will be using this app for AWS EB (elasticbeanstalk) demo.

 ## Running app locally
> Recommended to setup a virtual environment with python 3.9.x

- `cd python-dj-cloud-deploy`
- activate python virtual env
- `pip install -r  requirements.txt`
- `python manage.py migrate` 
- `python manage.py runserver`


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
- `eb init`

- eb create 

### Validations
- eb logs
- eb ssh 


## Setup like a pro

### VPC 

### Logs

### Database

### Monitoring


