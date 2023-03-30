GCP Static Website
==================

============
Useful Links
============

* https://codelabs.developers.google.com/codelabs/cloud-webapp-hosting-gcs#8
* https://stackoverflow.com/questions/62113405/static-website-i-am-hosting-cannot-be-reached-and-the-server-ip-cannot-be-found
* https://cloud.google.com/storage/docs/hosting-static-website

Load balancing for HTTPS and avoid privacy error
--------------------------------------------------------------------
Ended up finding the answer thanks to @IshRaj on ServerFault.

For future reference to anyone else viewing, Google Cloud Storage only supports HTTP connections when hosting a static website through CNAME resource records. To serve content through a custom domain over SSL, you will need to either:

Set up an external HTTPS load balancer (instructions here), potentially with Google Cloud CDN (set-up documentation here)

Connect a third-party Content Delivery Network to your Google Cloud
Storage (guide here)

Host your static website on Google App Engine with Python (guide here)

Serve static website content through Google Firebase rather than
Google Cloud Platform (tutorial here/additional support)

Personally, I went with Google Firebase (the last option), which automatically upgrades websites to https. It was simple and quick to set up and content is now directly deployable from my files. As well, with Firestore's automatic scalability and powerful queries, Firebase becomes a viable alternative, especially with its other features (user authentication, realtime data synchronization, machine-learning, extensions).
--------------------------------------------------------------------

https://misskecupbung.wordpress.com/2022/09/22/google-cloud-deploying-a-static-web-application-to-google-cloud-storage-bucket-with-https-load-balancer/


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

gcloud cheat sheet:

https://gist.github.com/pydevops/cffbd3c694d599c6ca18342d3625af97


https://cloud.google.com/sdk/docs/install
%LOCALAPPDATA%\Google\Cloud SDK

From command line:

.. code-block:: bash
    
    # create project
    set PROJECT=[Your project]
    gcloud config set project %PROJECT%

    # if beta is not installed you will asked to install it in a new terminal
    gcloud beta billing accounts list 

    # you can rename billing acount at https://console.cloud.google.com/billing
    # else is will be named "M Billing Account" by default
    gcloud beta billing projects link %PROJECT% --billing-account samkhalilian@hotmail.com 

    # create bucket
    set BUCKET=[Your domain] # samkhalilian.dev
    gsutil mb gs://%BUCKET% # BadRequestException: 400 Unknown project id: static-website

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
