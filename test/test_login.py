import pytest
from test.BaseTest import BaseTest

class TestLogin:
    @pytest.fixture
    def set_up(self):
        self.b = BaseTest()

    def test_correct_login_credentials(self):
        print(self.b)
        assert 1 == 1
    