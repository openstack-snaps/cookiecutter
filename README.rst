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
    # Make any necessary changes
    git init
    git add .
    git commit -a -m "Initial snap creation"
    git push https://github.com/openstack/$repo_name

And then get the project registered on Launchpad and added to the OpenStack
Infrastructure.

If you need any help, you can find the OpenStack Snap team in `#openstack-snaps`
on Freenode IRC.

.. _OpenStack-Infra: http://docs.openstack.org/infra/system-config
.. _Tox: http://testrun.org/tox/
.. _snapcraft: https://snapcraft.io/
