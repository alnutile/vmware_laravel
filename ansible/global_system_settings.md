# Global System Settings

## What it does

* Utilize the custom Ansible module [`env_facts`](custom_modules/env_facts.py) to collect current env variables.
* Update AWS CLI
* Set up SSH `authorized_keys`
* Create `/home/{{ user }}/app`
* Build `.env` file
* Cron is setup to run this script every hour with the flag `rebuild_env=false`


## Help

* For remote server

```bash
cd ~/base-ec2
ansible-playbook --limit base-ubuntu global_system_settings.yml -u ubuntu -i /etc/ansible/hosts --private-key=~/.ssh/Alfred.pem --extra-vars "app_env=production rebuild_env=false"  --module-path=./custom_modules
```

* For localhost, when you ssh in the server

```bash
cd ~/base-ec2
ansible-playbook --limit localhost global_system_settings.yml -u ubuntu -i 'localhost' --extra-vars "app_env=production rebuild_env=false" --module-path=./custom_modules
```

* To build `.env` however this should be taken care of by the CloudFormation template

```bash
cd ~/base-ec2
ansible-playbook --limit localhost global_system_settings.yml -u ubuntu -i 'localhost' --extra-vars \
"{'app_env': 'production', 'env_vars': [['APP_DEBUG', 'false']], 'fixed_envs': ['APP_KEY', 'DB_PASSWORD', 'DB_DATABASE', 'DB_USERNAME'] }" --module-path=./custom_modules
```

Here we pass a list of env variables and it will build the `.env` file in the root directory (e.g. `/home/{{ user }}/app`). Note that `extra-vars` will need to be a valid JSON
