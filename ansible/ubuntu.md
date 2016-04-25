# Ubuntu

Note the default user name :(

And you have to let this user have password sudo access using visudo and adding

~~~
alfrednutile ALL=(ALL) NOPASSWD:ALL
~~~

~~~
ansible-playbook -i "local," -c local ubuntu.yml
~~~

Then nginx and mysql and you should be set