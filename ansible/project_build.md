# Project Build

Here is a template for project specific. To start using it, run:

```bash
# Pass in --aws-key=YOUR_KEY --aws-secret=YOUR_SECRET if your .env doesn't have them in AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID.
php artisan cd:setup
```

  1. Publish template project_build.yml to <root>/server_config/ansible/build.yml
  2. Publish deployment scripts to <root>/deployment/scripts and appspec.yml to <root>/appspec.yml
  
## Steps for Adding to the Setup and Updates:


**Steps:**  

1. Update the `build.yml` that is in your `server_config/ansible` folder.
1. Run the Artisan command to upload it

~~~bash
# Pass in --aws-key=YOUR_KEY --aws-secret=YOUR_SECRET if your .env doesn't have them in AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID.
php artisan cd:provision:upload
~~~



1. What is going to happen:
    * CloudFormation script will download `s3://cat-provision-config/{AppName}/provision/build.yml` from S3 to `/home/ubuntu/project-ec2`
    * CloudFormation script will download `s3://cat-provision-config/{AppName}/provision/{AppEnv}` from S3 to `/home/ubuntu/project-ec2/{AppEnv}`
    * On CloudFormation stack creation, the `build.yml` script will run after the base EC2 scripts are done (`ubuntu.yml`, `global_system_settings.yml`, `nginx_ubuntu.yml`)
    * On CloudFormation stack update, the `build.yml` script will run after `global_system_settings.yml`
    * The script will receive variables `app_env={AppEnv} app_name={AppName} should_seed={ShouldRunSeed}`
    * You can make use of the file `/home/ubuntu/.CFN_INFO` that contains the information of the stack:

        ```
        Stack=teamhub-stage
        BuildVersion=1.0.2
        AppEnv=stage
        ```
1. [Skip this if you don't have any custom env variables] As seen in the [template](project_build.yml), it is setting additional env variables to the `.env` file.
    1. Determine what custom env variables you need to set by checking the [default ENV variables](../README.md#env-and-how-we-handle-that).
    1. Run command below to set the custom env variables:

    ```bash
    # Pass in --aws-key=YOUR_KEY --aws-secret=YOUR_SECRET if your .env doesn't have them in AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID.
    php artisan cd:config:set --key-value=ORG=github,ORG_KEY=foobar,ORG_SECRET=foobar --app-env=stage
    ```

1. Proceed with your CloudFormation steps. After the CloudFormation is created/updated, if you have any custom ENV settings setup from above, you should see something like this in the `/home/ubuntu/app/.env` file:

    ```
    APP_NAME=teamhub
    APP_KEY=foobarfoo
    # BEGIN ANSIBLE MANAGED BLOCK
    ORG_KEY=secret
    ORG_USER=user
    ORG_NAME=pfizer
    # END ANSIBLE MANAGED BLOCK
    ```

    Where the content between the `ANSIBLE MANAGED BLOCK` comes from your custom variables you set above.
