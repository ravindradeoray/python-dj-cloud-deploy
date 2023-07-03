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
- for easy start, we will keep default vpc with all public subnets covering 3 Az's. For default setup EB will use ALB which requires vpc with atleast 2 subnets covering different az's.
- install aws cli, aws eb cli
- setup aws account for cli access as I like to do things via commandline. It helps to then understand how to automate stuff and not do it manually. Ensure that account you are going to use has necessary permissions to run EB cli

### Application changes to support AWS deployment.
- `DEBUG=0` to run applciation in secure mode with AWS and ALB support for static files.
- update your own secret-key which is specific to aws env
- my sample shows how to setup SSL port with ALB. you can skip this and not bother running secure. but then set all secure ssl related flags to False in settings.py
- here is full optional_settings section
```
option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: "mysite.settings"
    DEBUG: "0"
    SECRET_KEY: "env-specitic-secret-key-goes-here"
  aws:elasticbeanstalk:container:python:
    WSGIPath: mysite.wsgi:application
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /static: "www/static"
  aws:elbv2:listener:443:
    ListenerEnabled: 'true'
    Protocol: HTTPS
    SSLCertificateArns: <arn-for-your-ssl-cert-goes-here>
  AWSEBV2LoadBalancerTargetGroup.aws:elasticbeanstalk:environment:process:default:
    HealthCheckPath: /health/
    MatcherHTTPCode: '200'
    HealthCheckInterval: '15'
    HealthCheckTimeout: '5'
    HealthyThresholdCount: '3'
```
- To run number of django-admin/manage.py commands during application setup here is section of config
```
container_commands:
  01_migrations:
    command: "source /var/app/venv/*/bin/activate && python manage.py migrate --noinput"
    leader_only: true
  02_collectstatic:
    command: "source /var/app/venv/*/bin/activate && python manage.py collectstatic --noinput"
  03_load_initial_data:
    command: "source /var/app/venv/*/bin/activate && python manage.py load_initial_data"
    leader_only: true
  06_dbpermissions:
    command: "chown webapp:webapp db.sqlite3"
```
- setup above `container_commands` and `option_settings` in `01_python.config` file under `.ebextentions` folder under `BASE_DIR`
- time check-in your code fire `eb create` or `eb deploy`. I prefer to check-in stuff before deploying to any enviornment but if you want you want to skip check-in then add `--staged` flag with your eb commands.

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


