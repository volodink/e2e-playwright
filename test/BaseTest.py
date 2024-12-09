import pytest
from abc import ABC


class BaseTest(ABC):
    def __init__(self):
        self._playwright = None
        self._browser = None
        self._browser_context = None
        self._page = None
        self.__need_video = False
    
    @pytest.fixture(autouse=True)
    def close(self):
        self._browser.close()
        self._playwright.close()
    