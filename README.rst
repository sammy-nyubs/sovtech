sovtech test automation
=============================
Following are instructions on how to set up and run your automated scripts

Getting Started
---------------

Tools used
----------
- Python 3+ `<https://www.python.org/downloads/>`_
- Selenium `<https://selenium-python.readthedocs.io/installation.html>`_
- Toolium `<https://readthedocs.org/projects/toolium/downloads/pdf/latest/>`_
- Behave `<https://behave.readthedocs.io/en/latest/install.html>`_
- IDE  preferrably pycharm or any

In our case we used chromedriver but any webDriver can be installed and configured on properties.cfg.


The requirements to install Toolium are `3.3+ or higher <http://www.python.org>`_ and
`pip <https://pypi.python.org/pypi/pip>`_. If you use Python 2.7.9+, you don't need to install pip separately.

Clone the repository and install requirements.
It's highly recommendable to use a virtualenv.

On the terminal hit the following commands

    $ git clone https://github.com/sammy-nyubs/sovtech-project.git
    
    $ cd sovtech-mini-project
    
    $ cd sovtech-mini-project (again, yep)

    $ pip install -r requirements.txt

Running Tests
-------------

By default, our tests are configured to run in chrome locally, so chrome must be installed in your machine and the
chrome driver must be downloaded and configured:

- Download `chromedriver_*.zip <https://chromedriver.chromium.org/downloads>`_
- Unzip file and save the executable in a local folder
- Configure driver path in *[Driver]* section in `conf/properties.cfg` file ::

    [Driver]
    chrome_driver_path: C:\Drivers\chromedriver.exe

To run all tests:

Now that you are on the sovtech-mini-project directory.

Ensure you are on the second sovtech-mini-project directory.

On the terminal hit the following command

    $ cd features


Your present directory should look something like this:

    $ sovtech-mini-project\\sovtech-min-project\\features>

    $ run behave

Should like this:

    $ sovtech-mini-project\\sovtech-min-project\\features> behave

