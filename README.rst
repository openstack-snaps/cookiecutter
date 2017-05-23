=================
snap-cookiecutter
=================

Cookiecutter template for an OpenStack snap. See https://github.com/audreyr/cookiecutter.

* Free software: Apache license
* snapcraft_: Creates a snap package that can be built with snapcraft
* OpenStack-Infra_: Ready for OpenStack Continuous Integration testing
* Tox_ testing: Setup to easily test snap build for Python 3.5

Usage
-----

Generate a snap project::

    cookiecutter https://github.com/openstack-snaps/snap-cookiecutter.git
    cd $repo_name
    git init
    git add .
    git commit -a

Then:

* Make any necessary updates

* Add the project to the OpenStack Infrastructure


.. _OpenStack-Infra: http://docs.openstack.org/infra/system-config
.. _Tox: http://testrun.org/tox/
.. _snapcraft: https://snapcraft.io/
