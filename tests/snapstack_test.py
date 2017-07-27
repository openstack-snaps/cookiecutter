import unittest

from snapstack import Plan, Step

class SnapstackTest(unittest.TestCase):

    def test_snapstack(self):
        '''
        _test_snapstack_

        Run a basic smoke test, utilizing our snapstack testing harness.

        snapstack will install a "base" set of snaps, including
        keystone, nova and neutron, then run the step/s you specify
        below. You can modify the base if needed, per the instructions
        in the snapstack
        docs. (https://github.com/openstack-snaps/snapstack)

        '''
        step = Step(
            snap='{{ cookiecutter.repo_name }}',
            script_loc='./tests/',
            scripts=['{{ cookiecutter.repo_name }}.sh'],
            snap_store=False
        )
        plan = Plan(scripts=[step])
        plan.run()
