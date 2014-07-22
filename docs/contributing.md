# Contributing

```dj-twiml``` is always under development, and welcomes any contributions!
If you'd like to get your hands dirty with the source code, please fork the
project on [our GitHub page](https://github.com/phalt/dj-twiml).

The guidelines below should help you get started.


### Setup


1. Fork the project on Github
2. Create a separate, **well named** branch to work on, off of the **develop**
   branch.
3. Install the requirements using pip:

```
    $ pip install -r requirements.txt
    $ pip install -r requirements-test.txt
```

You should now have the ```dj-twiml``` source code and development
environment ready to go.

### Style

When contributing code, please try to keep the style matching that of the
codebase. Right now, that means:

* 100% [PEP-8 compliance](http://www.python.org/dev/peps/pep-0008/).
* Proper spelling / punctuation in the source code.

After setting up your development environment, you can run::

```
    $ make lint
```

This will lint the entire project and ensure PEP8 standards are being stuck to.

**Please note**: We're pretty relaxed on line length, but make sure you keep
it below 90 characters where possible.


Docs
----

If you'd like to contribute any documentation, just dig right in! The documentation is made using the amazing [MkDocs](http://mkdocs.org) for documentation.


Tests
-----

In order to ensure high-quality releases, ``dj-twiml`` aims to have an
extensive test suite. All test suite patches and additions are welcome, and
encouraged for new developers! The tests are well documented, and can be
a great way to introduce yourself to the codebase!

To run the tests, you can either use::

```
    $ make test
```

You'll see output that looks something like:

```
    python runtests.py
    nosetests tests -s --verbosity=1
    Creating test database for alias 'default'...
    ......
    ----------------------------------------------------------------------
    Ran 6 tests in 0.024s

    OK
    Destroying test database for alias 'default'...
```
That's it! As you can see, when you run the test suite, ``dj-twiml`` should
output not only failing test results, but also the coverage reports.

When you submit patches or add functionality to ``dj-twiml``, be sure to
run the test suite to ensure that no functionality is broken!

Workflow
--------

When contributing to ``dj-twiml``, here's a typical developer workflow::

    # Preparing the environment:

    $ pip install --upgrade virtualenv virtualenvwrapper
    $ source "/usr/local/bin/virtualenvwrapper.sh"
    $ mkvirtualenv --no-site-packages djtw
    (djtw)$ git clone https://github.com/<your_username>/dj-twiml.git
    (djtw)$ cd dj-twiml/
    (djtw)$ git remote add upstream https://github.com/rdegges/django-twilio.git
    (djtw)$ git checkout develop
    (djtw)$ git pull upstream develop
    (djtw)$ pip install -r requirements.txt
    (djtw)$ pip install -r requirements-test.txt

    # Hacking:

    (djtw)$ git checkout develop
    (djtw)$ vim ...
    <<< hack time >>>

    # Writing tests:

    (djtw)$ cd test_project/test_app/
    $ vim ...
    <<< hack time >>>

    # Running tests:

    (djtw)$ cd dj-twiml/
    (djtw)$ make test
    <<< check test output >>>

.. note::
    Please be sure that if you fork the project, you work on the ```develop```
    branch. When submitting pull requests, please do so only if they're for the
    ```develop``` branch.


Bugs / Feature Requests / Comments
----------------------------------

If you've got any concerns about ``dj-twiml``, make your voice heard by
posting an issue on our [GitHub issue tracker](https://github.com/phalt/dj-twiml/issues). All bugs / feature
requests / comments are welcome.
