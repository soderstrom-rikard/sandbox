#!/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import platform
import os
import shlex
import shutil
import sys
import subprocess

# bake rules
import external

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
BUILD_DIR = os.path.join(SCRIPT_DIR, 'build', platform.platform())


def shell(cmd, stdout=None, stderr=None, cwd=None):
    docker_cmd = ' '.join([
        'docker run -it',
        '--workdir={CWD}'.format(CWD=shlex.quote(cwd)),
        '--volume {S}:{S}'.format(S=shlex.quote(SCRIPT_DIR)),
        'debian:buster-ada',
        cmd
        ])

    print(docker_cmd)
    return subprocess.run(docker_cmd,
                          shell=True,
                          check=True,
                          stdout=stdout,
                          stderr=stderr,
                          cwd=cwd)

def world(args):

    for dep in external.rules:
        print("building", dep['description'])

        source_dir = os.path.join(SCRIPT_DIR, 'external', dep['source'])
        target_dir = os.path.join(BUILD_DIR, 'external', dep['name'])
        for command in dep['world']:
            shell(command.format(TARGET=target_dir), cwd=source_dir)

def package(args):
    print("not implemented")
    pass

def test(args):
    print("not implemented")
    pass

def parse_commandline():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='creation, inspection and extraction of .arc files',
            epilog='''
Example usage(s):

Build project
python3 %(prog)s world'''
    )

    # Define parsers
    subparsers = parser.add_subparsers(dest='command')

    parser_world = subparsers.add_parser('world',
            description="bakes the world, e.g. 'make all'")
    parser_package = subparsers.add_parser('package',
            description="packages (adds sources, documentation and built binaries into a package)")
    parser_test = subparsers.add_parser('test',
            description="runs unit tests on baked world")

    args = parser.parse_args()

    if args.command is None:
        parser.print_usage()

    return args

if __name__ == "__main__":
    args = parse_commandline()
    if args.command:
        locals()[args.command](args)
