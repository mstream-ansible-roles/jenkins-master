#!/usr/bin/env python

import argparse
import subprocess
import shlex

def run_command(command):
    process = subprocess.Popen(
        shlex.split(command),
        stdout=subprocess.PIPE
    )
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print output.strip()
    rc = process.poll()
    return rc

    
parser = argparse.ArgumentParser(
    description='Runs the role tests'
)

tag_actions = ['provision',
	       'configure',
	       'verify']

actions = list(tag_actions)
actions.append('clean')
actions.append('test')

parser.add_argument(
    'action',
    choices=actions
)

args = parser.parse_args()

tags = ','.join(tag_actions) if args.action == 'test' else args.action

cmdFmt = 'ansible-playbook --tags {tags} -e "test_container_name={container_name}" test.yml'

cmd = cmdFmt.format(
    tags=tags,
    container_name='jenkins-master-test'
)

print(cmd)

run_command(cmd)

