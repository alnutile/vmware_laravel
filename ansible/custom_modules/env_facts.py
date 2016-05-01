#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Ansible module to give current values for the given env variables.

This only works for local file.

Example (make sure run with --module-path=./custom_modules)

- hosts: localhost

  tasks:
    - env_facts: src=env vars="APP_KEY,APP_DEBUG"

    - debug: msg={{ current_envs }}

"""

import os
import ConfigParser

SECTION_HEAD = 'asection'

class FakeSectionHead(object):
    def __init__(self, fp):
        self.fp = fp
        self.sechead = '[%s]\n' % (SECTION_HEAD)

    def readline(self):
        if self.sechead:
            try:
                return self.sechead
            finally:
                self.sechead = None
        else:
            return self.fp.readline()

def main():

    module = AnsibleModule(
        argument_spec = dict(
            src         = dict(required=True),
            vars        = dict(required=True, type='list')
        )
    )

    src = os.path.expanduser(module.params['src'])
    vars = module.params['vars']

    current_envs = {}

    if not os.path.exists(src):
        module.exit_json(
            changed = False,
            ansible_facts = dict(
                current_envs = current_envs
            )
        )

    if not os.access(src, os.R_OK):
        module.fail_json(msg="Source %s not readable" % (src))

    config = ConfigParser.SafeConfigParser()

    config.readfp(FakeSectionHead(open(src)))

    for var in vars:
        if config.has_option(SECTION_HEAD, var):
            current_envs[var] = config.get(SECTION_HEAD, var)

    res_args = dict(
        changed = True,
        ansible_facts = dict(
            current_envs = current_envs
        )
    )

    module.exit_json(**res_args)

from ansible.module_utils.basic import *
main()
