# Setup VMWare Box for Laravel

Homestead is amazing but I need something more inline with the servers we work on.

The scripts that follow are like the ones we use to buidl the servers, nginx etc. So we can know that our local
VM is setup the same way.

Some feature missing for now 

  * Port forwarding on VM to Windows/Mac/Linux
  * Vagrant install script

Here is an example of a workflows

 
#### Step 1) Setup the VM Once
Download and install VM (Virtual box or VMWare)
Setup it up per the notes below
Once in there run, only needed once, the ansible scripts to set it all up

  * ubuntu.yml
  * nginx.yml
  * mmysql.yml

#### Step 2) Add Sites when you need them
Finally when you want to work on a site

  * log in to the vm
  * git clone your site into the ~/Code folder
  * run `create_site.yml' with the needed vars 
  * point your Windows/Mac/Linux box host file to the ip of the Vm


## Now for the detail install workflow

## VM Setup Manual Steps

  * Setup VMWare using Ubuntu 14.04 (username ubuntu)
  * Make sure user has passwordless sudu
  * apt-get install openssh-server
  * Set Network to Bridge
  * Make sure you setup Ansible 2 in the VM

### Sudo Setup

Using visudo add

~~~
alfrednutile ALL=(ALL) NOPASSWD:ALL
~~~

Of course @TODO alfrednutile === ubuntu like our servers

## Network to Bridge

Under Edit in the top menu of the VM Software (VMWare) or in settings of the VM (VMWare) there is Virtual Network Manager there you will see Bridged, then just make sure it references your Wireless card.

## VMWare install tools

In the menu of VMWare VM click Install Tools

then in the vm mkdir /mnt/foo

then `mount /dev/cdrom /mnt/foo`

cp /mnt/foo/VMWareTools* /opt

tar xzvf VMWare*

then cd vmware-tools-distrib




## Folder Share

Click on the VM (After you install the VM Tools)

### VMWare
And click Settings-->Options-->Shared Folder

This will be in your linux box (maybe need to reboot) under `/mnt/hsgf`

Then I symlink `/mnt/msgf/Users/ubuntu/Code ~/Code` so it is in my home folder.

### VirtualBox
@TODO write this up

## Windows Host File

http://www.sysprobs.com/how-to-edit-host-file-in-windows-8-1-8

## Ansible

On the VM

Setup 2.x version

~~~
$ sudo apt-get install software-properties-common
$ sudo apt-add-repository ppa:ansible/ansible
$ sudo apt-get update
$ sudo apt-get install ansible
~~~

As noted above there are several files this is how your run each one, except the `create_site.yml` since
that one needs more settings.

~~~
ansible-playbook -i "local," -c local ubuntu.yml
~~~

  * ubuntu.yml
  * nginx.yml
  * mmysql.yml

## MySQL

It is root/password so just keep that in mind as you go

## Create Site

The goal is to create a defail nginx site.

This setup assumes you have downloaded your github repo in the the `/home/username/Code/repo_name` folder

~~~
ansible-playbook -i "local," -c local create_site.yml --extra-vars="sitefolder=foo2 sitename=baz.dev"
~~~

Will build our your site, database, setup your internal hosts file.


## Roadmap / TODO

Local DynamoDB Dev Setup

## TODO
Move most of this into vagrant
Set around a generic user name
Get Folder Sharing setup
Better sharing of ssh keys
