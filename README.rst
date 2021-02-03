=========
pyscraper
=========


.. image:: https://img.shields.io/pypi/v/pyscraper.svg
        :target: https://pypi.python.org/pypi/pyscraper

.. image:: https://img.shields.io/travis/ClintEsteMadera/pyscraper.svg
        :target: https://travis-ci.com/ClintEsteMadera/pyscraper

.. image:: https://readthedocs.org/projects/pyscraper/badge/?version=latest
        :target: https://pyscraper.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/ClintEsteMadera/pyscraper/shield.svg
     :target: https://pyup.io/repos/github/ClintEsteMadera/pyscraper/
     :alt: Updates



**pyscraper** is a super simple Python script that accepts a mandatory URL (URI, actually) as parameter. It issues a
request to that URI and attempts to interpret the response body as HTML and count the HTML elements present. It returns
a brief summary of such figure as well as the top 5 most used tags.

* Free software: Apache Software License 2.0
* Documentation: https://github.com/ClintEsteMadera/pyscraper

Context
-------

This script was created in the context of a code challenge that a company asked me to do. These are the exact requirements:

    Build a web page scraper in python that generates some basic metrics about a given page.

    Requirements:

    - A "README" explaining usage and any dependencies/setup/caveats/etc
    - The exercise should be written in Python (2 or 3, as you prefer). Please, specify in the README the version that was used
    - No external python libraries are allowed. But built-in Python libraries are allowed
    - The target URL to scrape should be a parameter
    - In whatever output format you see fit, your code should hit the target domain and output the total number of HTML elements and the top 5 most frequently used tags, and their respective counts.
    - Must-have/Compulsory: Write tests to make sure your code is behaving correctly.
    - You must create a repo on Github and send us the link to it.

    Please include any good practices you usually follow and present it as if it were production-ready code.

Requirements
------------

**Mandatory:**

* Python 3 or greater

**Optional:**

If you are interested in running code coverage (currently at 100%), lint or api-docs generation, you will need the following:

* flake8 (``pip install flake8``)
* coverage (``pip install coverage``)
* sphinx (``pip install sphinxcontrib-apidoc``)

Virtual Environment
-------------------

Although optional, using a virtual environment is highly recommended. To manage these virtual environments, if you haven't
already done so, please install pyenv:

``brew install pyenv pyenv-virtualenv``

You then need to add this to ``.bashrc``:

::

    if command -v pyenv 1>/dev/null 2>&1; then
        eval "$(pyenv init -)"
        eval "$(pyenv virtualenv-init -)"
    fi


Then run ``pyenv versions`` to know which Python versions you've got already. Choose any Python 3+ for basing the
virtualenv you will create. For example:

``pyenv virtualenv system-3.8.2 pyscraper``

Now run ``pip install -r requirements_dev.txt`` and you should be good to go.

Note that there is a ``Makefile`` that has several goals to accomplish these tasks.

Script Usage
------------

``python main.py <url_to_scrape>``


**Example:**

::

    python main.py https://www.ordergroove.com/

**Sample Output:**

::

    Number of HTML elements: 1104
    Most frequently used elements (Top 5):
    div : 452
    script : 163
    span : 88
    a : 70
    li : 60

Run tests
---------
Just run the following:

::

    make test

Note: you might see there is a warning that was intentionally omitted (``pytest --disable-pytest-warnings``) as I could
not easily (properly) fix it.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

Even though many auto-generated things, specially in the ``Makefile``, might strike people as unnecessary for the purpose
of this code challenge, as a Python newbie, I found it was a good excuse for me to at least scratch the surface of several
tools commonly used in the Python ecosystem. That is why I decided to go this route, as opposed to a dead-simple setup
which is what my IDE (PyCharm) generated for me in the first place.
