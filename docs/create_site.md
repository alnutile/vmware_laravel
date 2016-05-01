# Create Site

The goal is to create a defail nginx site.

This setup assumes you have downloaded your github repo in the the `/home/username/Code/repo_name` folder

~~~
ansible-playbook -i "local," -c local create_site.yml --extra-vars="sitefolder=foo2 sitename=baz.dev"
~~~

Will build our your site, database, setup your internal hosts file.



## Roadmap / TODO

Local DynamoDB Dev Setup
