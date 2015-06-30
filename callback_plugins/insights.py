# (C) 2012-2014, Michael Dumont <michaeldumont@gmail.com>

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
import requests
import json
import logging
import getpass
import os

from ansible import utils

logging.captureWarnings(True)

class CallbackModule(object):

    def __init__(self):
        #if foo:
        #    self.disabled = True
        self.insights_token = os.getenv('NR_INSIGHTS_TOKEN')
        self.post_uri = os.getenv('NR_INSIGHTS_URI')
        self.user = getpass.getuser()

        if self.insights_token is None or self.post_uri is None:
            self.disabled = True
            utils.warning('New Relic Insights token or Post URI could not be loaded. The NR Insights '
                          'token and URI can be provided using the `NR_INSIGHTS_TOKEN` and `NR_INSIGHTS_URI`'
                          'environment variables.')

    def __send_to_nr__(self, data):
        headers = { 'Content-Type':'application/json', 'X-Insert-Key': self.insights_token}
        requests.post(self.post_uri, headers=headers, data=json.dumps(data))

    def runner_on_ok(self, host, res):
        data = { 'eventType' : 'ansible_run', 'host': host, 'module_name': res['invocation']['module_name'], "changed" : str(res.get('changed', 'False')), "user" : self.user}
        self.__send_to_nr__(data)




