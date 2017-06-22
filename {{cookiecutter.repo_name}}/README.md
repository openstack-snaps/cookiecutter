# The {{ cookiecutter.snap_name }} snap

This repository contains the source code for the {{ cookiecutter.snap_name }} snap.

{{ cookiecutter.project_description }}

## Installing this snap

The {{ cookiecutter.snap_name }} snap can be installed directly from the snap store:

    sudo snap install --edge {{ cookiecutter.snap_name }}

The {{ cookiecutter.snap_name }} snap is working towards publication across tracks for
OpenStack releases. The edge channel for each track will contain the tip
of the OpenStack project's master branch, with the beta, candidate and
release channels being reserved for released versions. These three channels
will be used to drive the CI process for validation of snap updates. This
should result in an experience such as:

    sudo snap install --channel=ocata/stable {{ cookiecutter.snap_name }}
    sudo snap install --channel=pike/edge {{ cookiecutter.snap_name }}

## Configuring {{ cookiecutter.snap_name }}

The {{ cookiecutter.snap_name }} snap gets its default configuration from the following $SNAP
and $SNAP_COMMON locations:

### Insert trees of /snap/{{ cookiecutter.snap_name }}/current/etc/ and
### /var/snap/{{ cookiecutter.snap_name }}/common/etc. If the OpenStack service has an API
### that runs behind uwsgi+nginx, the trees may like like this:

    /snap/{{ cookiecutter.snap_name }}/current/etc/
    └── {{ cookiecutter.snap_name }}
        ├── {{ cookiecutter.snap_name }}.conf
        └── ...

    /var/snap/{{ cookiecutter.snap_name }}/common/etc/
    ├── {{ cookiecutter.snap_name }}
    │   └── conf.d
    │       └── {{ cookiecutter.snap_name }}-snap.conf
    ├── nginx
    │   ├── snap
    │   │   ├── nginx.conf
    │   │   └── sites-enabled
    │   │       └── {{ cookiecutter.snap_name }}.conf
    └── uwsgi
        └── snap
            └── {{ cookiecutter.snap_name }}.ini

### Add any details here on how to configure services for this snap.
### Insert a tree of /var/snap/{{ cookiecutter.snap_name }}/common/etc with override files.
### If the OpenStack service has an API that runs behind uwsgi+nginx,
### the tree may like like this:

The {{ cookiecutter.snap_name }} applications can be configured in a few ways. The directory
structure can be modified to override config as follows:

The {{ cookiecutter.snap_name }} snap supports configuration updates via its $SNAP_COMMON writable
area. The default {{ cookiecutter.snap_name }} configuration can be overridden as follows:

    /var/snap/{{ cookiecutter.snap_name }}/common/etc/
    ├── {{ cookiecutter.snap_name }}
    │   ├── conf.d
    │   │   ├── {{ cookiecutter.snap_name }}-snap.conf
    │   │   ├── database.conf
    │   │   └── rabbitmq.conf
    │   └── {{ cookiecutter.snap_name }}.conf
    ├── nginx
    │   ├── snap
    │   │   ├── nginx.conf
    │   │   └── sites-enabled
    │   │       └── {{ cookiecutter.snap_name }}.conf
    │   ├── nginx.conf
    │   ├── sites-enabled
    │   │   └── {{ cookiecutter.snap_name }}.conf
    └── uwsgi
        ├── snap
        │   └── {{ cookiecutter.snap_name }}.ini
        └── {{ cookiecutter.snap_name }}.ini

The {{ cookiecutter.snap_name }} configuration can be overridden or augmented by writing
configuration snippets to files in the conf.d directory.

Alternatively, {{ cookiecutter.snap_name }} configuration can be overridden by adding a full
{{ cookiecutter.snap_name }}.conf file to the {{ cookiecutter.snap_name }}/ directory. If overriding in this way, you'll
need to either point this config file at additional config files located in $SNAP,
or add those to $SNAP_COMMON as well.

The {{ cookiecutter.snap_name }} nginx configuration can be overridden by adding an nginx/nginx.conf
and new site config files to the nginx/sites-enabled directory. In this case the
nginx/nginx.conf file would include that sites-enabled directory. If
nginx/nginx.conf exists, nginx/snap/nginx.conf will no longer be used.

The {{ cookiecutter.snap_name }} uwsgi configuration can be overridden similarly by adding a
uwsgi/{{ cookiecutter.snap_name }}.ini file. If uwsgi/{{ cookiecutter.snap_name }}.ini exists, uwsgi/snap/{{ cookiecutter.snap_name }}.ini
will no longer be used.

## Logging {{ cookiecutter.snap_name }}

The services for the {{ cookiecutter.snap_name }} snap will log to its $SNAP_COMMON writable area:
/var/snap/{{ cookiecutter.snap_name }}/common/log.

## Managing {{ cookiecutter.snap_name }}

### If this snap has any aliases, they should be defined here. For example,
### {{ cookiecutter.snap_name }}-manage may be a well-known command that is used to manage
### the database for this project.
The {{ cookiecutter.snap_name }} snap has alias support that enables use of the following
well-known command. To enable the alias, run the following prior to
using the command:

    sudo snap alias {{ cookiecutter.snap_name }}.manage {{ cookiecutter.snap_name }}-manage

## Restarting {{ cookiecutter.snap_name }} services

To restart all {{ cookiecutter.snap_name }} services:

    sudo systemctl restart snap.{{ cookiecutter.snap_name }}.*

or an individual service can be restarted by dropping the wildcard and
specifying the full service name.

## Building the {{ cookiecutter.snap_name }} snap

Simply clone this repository and then install and run snapcraft:

    git clone https://github.com/{{ cookiecutter.repo_group }}/{{ cookiecutter.repo_name }}
    sudo apt install snapcraft
    cd {{ cookiecutter.repo_name }}
    snapcraft

## Support

Please report any bugs related to this snap at:
[Launchpad](https://bugs.launchpad.net/{{ cookiecutter.launchpad_project }}/+filebug).

Alternatively you can find the OpenStack Snap team in `#openstack-snaps` on
Freenode IRC.
