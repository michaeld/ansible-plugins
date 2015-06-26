# (C) 2012-2014, Michael DeHaan, <michael.dehaan@gmail.com>

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

logging.captureWarnings(True)

class CallbackModule(object):

    """
    this is an example ansible callback file that does nothing.  You can drop
    other classes in the same directory to define your own handlers.  Methods
    you do not use can be omitted. If self.disabled is set to True, the plugin
    methods will not be called.

    example uses include: logging, emailing, storing info, etc
    """

    def __init__(self):
        #if foo:
        #    self.disabled = True
        self.insights_key = 'Z31g8m6XsyqnYwouvzTk0PzBoitdDXDh'
        self.post_url = 'https://insights-collector.newrelic.com/v1/accounts/127903/events'

        """
        cat example_events.json
         | curl -d @- -X POST -H "Content-Type: application/json" -H "X-Insert-Key: YOUR_KEY_HERE" https://insights-collector.newrelic.com/v1/accounts/127903/events
        """
    def __send_to_nr__(self, data):
        headers = { 'Content-Type':'application/json', 'X-Insert-Key': self.insights_key}
        requests.post(self.post_url, headers=headers, data=json.dumps(data))

    def on_any(self, *args, **kwargs):
        pass

    def runner_on_failed(self, host, res, ignore_errors=False):
        pass

    def runner_on_ok(self, host, res):
        data = { 'eventType' : 'ansible_run', 'host': host, 'module_name': res['invocation']['module_name'], "changed" : str(res['changed'])}
        self.__send_to_nr__(data)
        #pass

    def runner_on_skipped(self, host, item=None):
        pass

    def runner_on_unreachable(self, host, res):
        pass

    def runner_on_no_hosts(self):
        pass

    def runner_on_async_poll(self, host, res, jid, clock):
        pass

    def runner_on_async_ok(self, host, res, jid):
        pass

    def runner_on_async_failed(self, host, res, jid):
        pass

    def playbook_on_start(self):
        pass

    def playbook_on_notify(self, host, handler):
        pass

    def playbook_on_no_hosts_matched(self):
        pass

    def playbook_on_no_hosts_remaining(self):
        pass

    def playbook_on_task_start(self, name, is_conditional):
        #self.__send_to_nr__({"eventType": "ansible_run", "task" : name })
        pass

    def playbook_on_vars_prompt(self, varname, private=True, prompt=None, encrypt=None, confirm=False, salt_size=None, salt=None, default=None):
        pass

    def playbook_on_setup(self):
        pass

    def playbook_on_import_for_host(self, host, imported_file):
        pass

    def playbook_on_not_import_for_host(self, host, missing_file):
        pass

    def playbook_on_play_start(self, name):
        pass

    def playbook_on_stats(self, stats):
        pass

