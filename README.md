README
====================

An API for creating and processing shortened URLs
---------------------


Requirements:
---------------------
* Create a URL shortening service
* Put it behind a cherrypy Rest API in a meaningful way
* The service must be built as a Docker image
* Put the code in Github in a way that makes sense: Readme file, etc  Make it pretty as if someone's going to use it
* deploy to a cloud provider of your choice
* rate limit the service to 2 requests per second
* bonus: for any kind of GUI 

Design Considerations:
---------------------
This project builds a deployable docker image containing the URL shortening service running on port 8080. 

A service needs to be fault tolerant and horizontally scaleable. I envision that when deployed to  a production setting that many instances of this docker container will sit behind a load balancer such as HAProxy.  I feel the rate limiting belongs at the front door to the service where we can rate limit across all running instances. I have utilized NGINX within the vagrant built machine to simulate HAProxy and handle the rate limiting.

By installing vagrant with the vagrant-aws plugin and setting your custom values in the Vagrantfile and machines.d/ShortUrl.rb you can actually build an instance in your AWS instance. 



Usage:
---------------------
* Create a shortened URL
	* POST request to the URL with a form encoded parameter named url and the system will return the shortened URL you can use.
	  * Example:
		`curl  -X POST -d 'url=http://google.com' http://localhost/`
	  * Example success response:
		`code: 201`
        `body: http://localhost/fg5`

	  * Returns a status code of 500 on any error creating the URL
	
* Delete a shortened URL
	* DELETE request to the shortened URL
	  * Example:		
		`curl  -X DELETE http://localhost/fg5`
	  * Always returns a 204 status code and an empty body


* * * * *
#Recommended development setup:#
---------------------
*  Install pip using your package manager
*  pip install virtualenv
*  pip install virtualenvwrapper
*  mkdir ~/.virtualenvs
*  Add the following to your .bashrc  
export WORKON_HOME=~/.virtualenvs/  
export PIP_VIRTUALENV_BASE=$WORKON_HOME  
source /usr/local/bin/virtualenvwrapper.sh  
*  source ~/.bashrc
*  mkvirtualenv shortUrl
*  workon shortUrl
*  pip install -r requirements.txt
*  configure  git to ignore all compiled python files  
   *  In .git/info/exclude add *.pyc
* install virtualbox via your package manager
* download vagrant v 1.7.4 for your OS and install 
* vagrant plugin install vagrant-aws

Running in development:
---------------------
* Intialize database 
  * `python initalize.py`
* `python run.py`
   * This will not include rate limiting

Running Tests:
---------------------

*  `nosetests`
*  If you want to see the stdout during test runs: `nosetests -s`
*  If you want to see coverage reports for the tests:
`nosetests --with-coverage --cover-package app --cover-html --cover-html-dir=/path/to/html/output`

Helpful Development tools:
---------------------
[Advanced Rest Client for chrome](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo)


