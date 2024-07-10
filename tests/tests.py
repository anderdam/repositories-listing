# import unittest
# from unittest.mock import patch
#
# from repositoriesList.GithubRepos import GithubRepos
#
#
# class TestCheckRateLimit(unittest.TestCase):
#
#     @patch("requests.get")
#     def test_check_rate_limit_success(self, mock_get):
#         # Mock successful API response
#         mock_response = mock_get.return_value
#         mock_response.json.return_value = {"rate": {"limit": 5000, "remaining": 4999}}
#
#         # Call the function with a mock token
#         result = GithubRepos("dummy_token").check_rate_limit()
#
#         # Verify the function returns the correct rate limit info
#         self.assertEqual(result, {"rate": {"limit": 5000, "remaining": 4999}})
#
#     @patch("requests.get")
#     def test_check_rate_limit_failure(self, mock_get):
#         # Mock API failure response
#         mock_response = mock_get.return_value
