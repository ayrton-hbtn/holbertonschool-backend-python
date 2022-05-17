#!/usr/bin/env python3
""" Unittest module """

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
import requests


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """ method to check the GithubClient org method """
        endpoint = 'https://api.github.com/orgs/{}'.format(org_name)
        spec = GithubOrgClient(org_name)
        spec.org()
        mock_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """ Test method returns correct output """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ Tests that test_public_repos returns a known payload.
        """
        get_json_mock.return_value = [
            {'name': 'repo_0'},
            {'name': 'repo_1'},
            {'name': 'repo_2'}
        ]
        get_json_mock()
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            mock.return_value = [
                {'name': 'repo_0'},
                {'name': 'repo_1'},
                {'name': 'repo_2'}
            ]
            ghc = GithubOrgClient('xyz')
            r = ghc._public_repos_url
            self.assertEqual(r, mock.return_value)
            mock.assert_called_once()
            get_json_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ Tests that has_license returns the correct values.
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected_result
        )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration class to test GithubOrgClient.public_repos method
    """
    @classmethod
    def setUpClass(cls):
        """setUpClass method"""
        cls.get_patcher = patch(
            'requests.get',
            side_effect=[
                org_payload,
                repos_payload
            ]
        )
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass method"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Testing GithubOrgClient.public_repos """
        ghc = GithubOrgClient('random')
        self.assertEqual(ghc.org, self.org_payload)
        self.assertEqual(ghc.repos_payload, self.repos_payload)


if __name__ == "__main__":
    unittest.main()