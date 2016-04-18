=============================================================
How to setup your enviroment to work on the RBP documentation
=============================================================


First download and install python then:

::

	sudo easy_install pip
	sudo pip install --upgrade pip
	sudo pip install -U Sphinx

On OSX, add these lines to your :file:`~/.bash_profile`:

::

	export LC_ALL=en_US.UTF-8
	export LANG=en_US.UTF-8


To install the required modules:

::
 
	sudo pip install sphinx_rtd_theme
	sudo pip install rst2pdf
	sudo pip install requests


