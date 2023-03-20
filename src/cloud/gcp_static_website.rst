GCP Static Website
==================

https://medium.com/google-cloud/hosting-a-static-website-on-google-cloud-using-google-cloud-storage-ddebcdcc8d5b
https://medium.com/google-cloud/using-chrome-dev-tools-with-google-cloud-50c20f230d61

==============
Google Domains
==============

Create a domain:

https://domains.google/intl/en-GB

https://cloud.google.com/gcp?hl=en

==================
Google Cloud Shell
==================

https://cloud.google.com/shell

====================
Google Cloud Storage
====================

https://cloud.google.com/storage/docs/hosting-static-website

https://console.cloud.google.com/getting-started/guide/website

1. Create a GCP account
https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=GB&continue=https%3A%2F%2Fconsole.cloud.google.com%2Ffreetrial%3Ffacet_utm_source%3Dgoogle%26facet_utm_campaign%3D(organic)%26facet_utm_medium%3Dorganic%26facet_url%3Dhttps%3A%2F%2Fcloud.google.com%2Fstorage%2Fdocs%2Fhosting-static-website%26facet_id_list%3D%255B39300012%2C%2B39300020%2C%2B39300118%2C%2B39300195%2C%2B39300251%2C%2B39300319%2C%2B39300320%2C%2B39300325%2C%2B39300333%2C%2B39300345%2C%2B39300354%2C%2B39300364%2C%2B39300374%2C%2B39300412%2C%2B39300422%2C%2B39300436%2C%2B39300473%255D%26_ga%3D2.151648956.441770899.1678547597-1397288281.1678547597&dsh=S856063625%3A1678547864015952&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fconsole.cloud.google.com%2Ffreetrial%3Ffacet_utm_source%3Dgoogle%26facet_utm_campaign%3D(organic)%26facet_utm_medium%3Dorganic%26facet_url%3Dhttps%3A%2F%2Fcloud.google.com%2Fstorage%2Fdocs%2Fhosting-static-website%26facet_id_list%3D%255B39300012%2C%2B39300020%2C%2B39300118%2C%2B39300195%2C%2B39300251%2C%2B39300319%2C%2B39300320%2C%2B39300325%2C%2B39300333%2C%2B39300345%2C%2B39300354%2C%2B39300364%2C%2B39300374%2C%2B39300412%2C%2B39300422%2C%2B39300436%2C%2B39300473%255D%26_ga%3D2.151648956.441770899.1678547597-1397288281.1678547597&ifkv=AWnogHdboG2VmYOz6atW5rsok4MXw5BFj0lvjRoqOZgoz6caIlAMc7y7t9bA9sjMan9LjOaQEpwPtg&osid=1&service=cloudconsole&nogm=true

2.


===============
Install GCP CLI
===============

https://cloud.google.com/sdk/docs/install
%LOCALAPPDATA%\Google\Cloud SDK

From command line:

.. code-block:: bash
    
    # create project
    PROJECT=[Your project]
    gcloud config set project $PROJECT

    # create bucket
    BUCKET=[Your domain]
    gsutil mb gs://${BUCKET}

    # copy web files
    gsutil cp *.html gs://${BUCKET}
    gsutil cp *.js gs://${BUCKET}

    # enable bucket as website
    gsutil web set -m index.html -e notfound.html gs://${BUCKET}

    # test website
    curl http://${BUCKET}/index1.html

    # make the website public
    gsutil iam ch allUsers:objectViewer gs://${BUCKET}
    gsutil acl ch -u AllUsers:R gs://${BUCKET}
    
    # optional environment variables
    >> set PYTHON = %LOCALAPPDATA%\Programs\Python\Python310\python
    >> set HOME = %HOMEDIR%%HOMEPATH%  # set home directoy
    >> set PROJECT = %HOME%/project  # select project directoy
    
    >> cd %PROJECT%
    >> git clone https://github.com/samkhalilian/blog.git

    # virtual environment
    >> cd blog
    >> %PYTHON% -m venv .venv 
    >> .venv\Scripts\activate

    # install packages (to be superseded by setup.py)
    >> pip install ablog # install https://ablog.readthedocs.io/
    >> pip install Pallets-Sphinx-Themes # install theme
    >> pip install sphinxcontrib-youtube
    >> pip install -U sphinx-mathjax-offline
    >> pip install numpydoc
    >> pip install sphinx-notfound-page

    # build blog pages
    >> cd ./blog/src
    >> ablog clean
    >> ablog build # build HTML pages
    >> ablog serve # to launch HTML pages
