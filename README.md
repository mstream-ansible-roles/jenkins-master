Jenkins Master
=========

A role to create jenkins master in version 2.73.x.

Requirements
------------

* ansible 2.0+
* docker daemon

Role Variables
--------------

admin_username: admin username

admin_password: admin password

plugins: list of plugins to be installed

seed_job_path: path to the job-dsl plugin script to bootstrap other jobs (optional)

seed_job_name: name of the seed job (optional, defaults to 'seed')

Dependencies
------------

None.

Example Playbook
----------------

```
- hosts: servers
  roles:
    - { role: jenkins-master, admin_username: 'admin', admin_password: 'admin' }
```

License
-------

MIT

Author Information
------------------

[GitHub](https://github.com/mstream)
