Provisioning a new site
=======================

The notes herein are particular to using webfaction for deployment.

## Required packages:

* Apache 2.4    
* Python 3      
* Git           
* pip           
* virtualenv

Fortunately, on webfaction all the required packages are already installed
and available.


## Apache config
Webfaction provides a default, working httpd.conf configuration file for its 
setup. However the target deployment vias away a little from this setup by 
using virtualenv. Thus all WSGI related entries in httpd.conf needs updating to 
use the virtualenv.

* see httpd-wsgi-extra.template.conf
* replace $USR with username, $SITENAME with webfaction app name and $PJTNAME 
  with django project name.


## Folder structure:
Assume we have a user account at /home/username


    /home/username
        +-- webapps
            +-- SITENAME
                +-- apache2         # webfaction
                +-- bin             # webfaction
                +-- database        
                +-- lib             # webfaction
                +-- source
                +-- static
                +-- venv

