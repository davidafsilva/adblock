#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#########################################
"""
Usage: adblock update [--help]

Updates the current local hosts file with the Updates
from the remote MVPS hosts file

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
import adblock_diff

def update():
    """
    Updates the current local hosts file with the Updates
    from the remote MVPS hosts file
    """
    if not adblock_io.has_rw_permission_local_hosts():
        adblock_utils.print_error(__file__, \
            "No read/write permissions on local hosts file.")
        exit()
    changes = adblock_diff.get_diff()
    deleted = changes[adblock_diff.DELETED_KEY]
    added = changes[adblock_diff.ADDED_KEY]
    if len(deleted) == 0 and len(added) == 0:
        print "Local hosts file is currently up-to-date."
    else:
        adblock_io.apply_changes_to_local_hosts(deleted, added)
        print "Local hosts file has been updated!"

# concrete module function
def execute(args=None):
    """
    Updates the current local hosts file with the Updates
    from the remote MVPS hosts file
    """
    docopt(__doc__, args)
    update()
