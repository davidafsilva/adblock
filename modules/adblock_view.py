#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#########################################
"""
Usage: adblock view [local | remote] [--help]

View the local/remote hosts file contents

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
import adblock_utils
import adblock_io

# view local
def view_local():
    """
    Views the local /etc/hosts file contents
    """
    contents = adblock_io.read_local_hosts()
    print "No local MVPS filters were found" if contents is None else contents

# view remote
def view_remote():
    """
    Views the remote hosts file contents
    """
    contents = adblock_io.read_remote_hosts()
    print "No remote MVPS filters were found" if contents is None else contents

# concrete module function
def execute(args=None):
    """
    View the local/remote hosts file contents
    """
    for (key, val) in docopt(__doc__, args).items():
        if val:
            if key == "local":
                view_local()
                exit()
            elif key == "remote":
                view_remote()
                exit()
    adblock_utils.print_help(__doc__)
