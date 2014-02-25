#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#########################################
"""
Usage: adblock diff [--help]

Shows the differences between the local hosts file against the remote one

"""
#########################################

"""
Copyright (c) 2013, David Silva
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
        notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
        notice, this list of conditions and the following disclaimer in the
        documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
        names of its contributors may be used to endorse or promote products
        derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from docopt import docopt
import adblock_io
import adblock_utils

# differences keys
ADDED_KEY = "a"
DELETED_KEY = "d"

def show_diff():
    """
    Shows the differences between the local and the remote
    MVPS hosts file
    """
    # local
    local_contents = adblock_io.read_local_hosts()
    # remote
    remote_contents = adblock_io.read_remote_hosts()
    if remote_contents is None:
        adblock_utils.print_error("No remote contents were found")
    else:
        # compare
        result = compare_diff(local_contents, remote_contents)
        print "No differences were found" if len(result) == 0 \
                else format_diff_result(result)

def compare_diff(local, remote):
    """
    Compares the local and remote MVPS hosts against each other
    It an dictionary with two keys:
      - ADDED_KEY (="a"): an array with the added hosts from the remote side
      - DELETED_KEY (="d"): an array with the deleted hosts form the remote side
    """
    if local is None:
        added = [("+ %s" % x.strip()) for x in remote.split('\n')]
        deleted = []
    else:
        local = local.split('\n')
        remote = remote.split('\n')
        added = [("+ %s" % x.strip()) for x in remote if x not in local]
        deleted = [("- %s" % x.strip()) for x in local if x not in remote]
    return {ADDED_KEY: added, DELETED_KEY: deleted}

def format_diff_result(result):
    """
    formats the output of the compare_diff function.
    It returns a string representation of the result with the following order:
      - 1st the deleted entries
      - 2nd the new entries
    """
    diff = '\n'.join(result[DELETED_KEY])
    diff += '\n' if len(diff) > 0 else ''
    diff += '\n'.join(result[ADDED_KEY])
    return diff

# concrete module function
def execute(args=None):
    """
    Updates the current local hosts file with the Updates
    from the remote MVPS hosts file
    """
    docopt(__doc__, args)
    show_diff()
