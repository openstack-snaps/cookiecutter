import unittest

from snapstack import Plan, Step

class SnapstackTest(unittest.TestCase):

    def test_snapstack(self):
        '''
        _test_snapstack_

        Run a basic smoke test, utilizing our snapstack testing harness.

        '''
        step = Step(
            snap='{{ cookiecutter.repo_name }}',
            script_loc='./tests/',
            scripts=['{{ cookiecutter.repo_name }}.sh'],
            snap_store=False
        )
        plan = Plan(scripts=[step])
        plan.run()
