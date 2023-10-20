import unittest
from trends import parse_trending_repos


class TestGithubTrendAnalysis(unittest.TestCase):

    def test_parse_trending_repos(self):
        sample_html = '''
        <html>
            <body>
                <div class="Box-row">
                    <h1 class="h3 lh-condensed">
                        <a href="/owner1/repo1">owner1 / repo1</a>
                    </h1>
                    <p class="col-9 text-gray my-1">Description 1</p>
                    <span class="float-sm-right">123 stars today</span>
                    <span class="d-inline-block ml-0 mr-3">Language 1</span>
                </div>
                <!-- More repository elements can be added here for more thorough testing -->
            </body>
        </html>
        '''
        expected_result = [
            {
                'owner': 'owner1',
                'name': 'repo1',
                'description': 'Description 1',
                'stars_per_day': 123,
                'language': 'Language 1'
            }
        ]
        result = parse_trending_repos(sample_html)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
