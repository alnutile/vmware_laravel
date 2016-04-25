# Nginx on Ubuntu

## What it does

* Update apt
* Remove Apache
* Setup Nginx
* Setup docroot (`/home/ubuntu/app`) permissions
* Setup Supervisor
* Setup cron for running `artisan schedule:run`
* Reload Nginx based on the flag `restart`

## Help

* For remote server

```bash
cd ~/base-ec2
ansible-playbook --limit base-ubuntu nginx_ubuntu.yml -u ubuntu -i /etc/ansible/hosts --private-key=~/.ssh/Alfred.pem
```

* For localhost, when you ssh in the server

```bash
cd ~/base-ec2
ansible-playbook --limit localhost nginx_ubuntu.yml -u ubuntu -i 'localhost'
```