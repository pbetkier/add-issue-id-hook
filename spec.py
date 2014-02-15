#!/usr/bin/env python

import os
import subprocess
import unittest


class AddIssueIdHookTest(unittest.TestCase):

    def setUp(self):
        self.execute('git init tmp_repo', 'cp commit-msg tmp_repo/.git/hooks/.')
        os.chdir('tmp_repo')

    def test_prepends_issue_id_from_branch_name_prefix_to_commit_message(self):
        # given
        self.on_branch("EXAMPLE-1337_some_feature")
        self.with_changes_to_be_committed()

        # when
        self.commit_with_message("Added some file.")

        # then
        self.assert_last_commit_message_is("EXAMPLE-1337 Added some file.")

    def test_doesnt_modify_commit_message_if_issue_id_not_in_branch_name(self):
        # given
        self.on_branch("some_feature")
        self.with_changes_to_be_committed()

        # when
        self.commit_with_message("Added some file.")

        # then
        self.assert_last_commit_message_is("Added some file.")

    def test_doesnt_modify_commit_message_if_issue_id_in_branch_name_but_not_as_prefix(self):
        # given
        self.on_branch("some_EXAMPLE-1337_feature")
        self.with_changes_to_be_committed()

        # when
        self.commit_with_message("Added some file.")

        # then
        self.assert_last_commit_message_is("Added some file.")

    def test_doesnt_modify_commit_message_if_it_already_starts_with_issue_id(self):
        # given
        self.on_branch("EXAMPLE-1337_some_feature")
        self.with_changes_to_be_committed()

        # when
        self.commit_with_message("EXAMPLE-1337 Added some file.")

        # then
        self.assert_last_commit_message_is("EXAMPLE-1337 Added some file.")

    def test_doesnt_modify_commit_message_if_in_detached_HEAD_state(self):
        # given
        self.with_initial_commit()
        self.in_detached_head_state()
        self.with_changes_to_be_committed()

        # when
        self.commit_with_message("Added some file.")

        # then
        self.assert_last_commit_message_is("Added some file.")

    def on_branch(self, branch_name):
        self.execute('git checkout -b {}'.format(branch_name))

    def with_changes_to_be_committed(self):
        self.execute('echo . >> some_file', 'git add some_file')

    def commit_with_message(self, message):
        self.execute('git commit -m "{}"'.format(message))

    def with_initial_commit(self):
        self.on_branch("EXAMPLE-1337_some_feature")
        self.with_changes_to_be_committed()
        self.commit_with_message("Some commit")

    def in_detached_head_state(self):
        self.execute('git checkout --detach')

    def execute(self, *commands):
        return subprocess.check_output('; '.join(commands), shell=True)

    def assert_last_commit_message_is(self, expected):
        self.assertEqual(self.execute('git log -1 --pretty=format:"%s"'), expected)

    def tearDown(self):
        os.chdir('..')
        self.execute('rm -rf tmp_repo/')


if __name__ == '__main__':
    unittest.main()
