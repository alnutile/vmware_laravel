# Setup VMWare Box for Laravel

## Manual Steps

  * Setup VMWare using Ubuntu 14.04
  * Make sure user has password free sudu
  * Set Network to Bridge
  * Make sure you setup Ansible 2 in the VM

### Sudo Setup

Using visudo add

~~~
alfrednutile ALL=(ALL) NOPASSWD:ALL
~~~

## Network to Bridge

Under Edit there is Virtual Network Manager there you will see Bridged, then just
make sure it references your Wireless card.

## Folder Share

Click on the VM (After you install the VM Tools)
And click Settings-->Options-->Shared Folder

This will be in your linux box (maybe need to reboot) under `/mnt/hsgf`

Then I symlink `/mnt/msgf/Users/ubuntu/Code ~/Code` so it is in my home folder.

## Windows Host File

http://www.sysprobs.com/how-to-edit-host-file-in-windows-8-1-8


## Ansible

Setup 2.x

~~~
$ sudo apt-get install software-properties-common
$ sudo apt-add-repository ppa:ansible/ansible
$ sudo apt-get update
$ sudo apt-get install ansible
~~~


  * ubuntu.yml
  * nginx_ubuntu.yml
  * mysql.yml

Here is an example command, you can replace the name for any of these

~~~
ansible-playbook -i "local," -c local ubuntu.yml
~~~

Then nginx and mysql and you should be set

## MySQL

It is root/password so just keep that in mind as you go

## TODO
Move most of this into vagrant
Set around a generic user name
Get Folder Sharing setup