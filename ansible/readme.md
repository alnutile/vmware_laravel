# Ansible Scripts

## Dependencies

* [ansible 2.x](http://docs.ansible.com/ansible/intro_getting_started.html)
* More read:
    * https://alfrednutile.info/posts/167
    * https://serversforhackers.com/an-ansible-tutorial

## AWS

Make sure your AWS Roles lets you connect. These ansible scripts are uploaded to `s3://cat-provision-config/base-ec2`

## Main scripts

* `ubuntu.yml`
* `global_system_settings.yml`
* `nginx_ubuntu.yml`

## Custom modules

The custom module `env_facts` will give the env values for the given variables by reading the file `.env`. Example usage:

```
  # Get env values the APP_KEY and APP_DEBUG. The values will be available in the current_envs variable.
  tasks:
    - env_facts: src=env vars="APP_KEY,APP_DEBUG"

    - debug: msg={{ current_envs }}
```

## References:

* [LEMP stack on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-on-centos-7)

* [Install Nginx PHP-Fpm on CentOS/Redhat](http://www.if-not-true-then-false.com/2011/install-nginx-php-fpm-on-fedora-centos-red-hat-rhel/)

* [Nginx and CentOS](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-on-centos-7)

* [SSL](https://www.digitalocean.com/community/tutorials/how-to-create-a-ssl-certificate-on-nginx-for-centos-6)

* [Overview Of Using Ansible](https://serversforhackers.com/an-ansible-tutorial)

* [Yaml Lint](http://www.yamllint.com/)

## FAQ

* Where are the logs?

    Check `/var/log/nginx/default-error.log` as sudo su

* BadGateway

    Check `/var/run/php-fpm/php-fpm.sock` make sure it is read writable by the user of the system and the group nginx