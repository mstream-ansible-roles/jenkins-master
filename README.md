Jenkins Master
=========

A role to create jenkins master in version 2.73.x.

Requirements
------------

* ansible 2.0+
* docker daemon

Role Variables
--------------

admin_username: admin username (defaults to 'admin')

admin_password: admin password (defaults to 'admin')


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
