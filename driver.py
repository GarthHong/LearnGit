from abc import ABC, abstractmethod


class Driver(ABC):
    @abstractmethod
    def do1(self, text: str) -> str:
        pass

    def do2(self, text: str) -> str:
        pass


class Adriver(Driver):
    def do1(self, text: str) -> str:
        return "Adriver.do1: {}".format(text)

    def do2(self, text: str) -> str:
        return "Adriver do2"


class Bdriver(Driver):
    def do1(self, text: str) -> str:
        return "Bdriver.do1: {}".format(text)

    def do2(self, text: str) -> str:
        return "Bdriver do2: {}".format(text)


class Inter(ABC):
    def __init__(self, driver: Driver):
        self._driver = driver

    @abstractmethod
    def func1(self):
        pass

    @abstractmethod
    def func2(self):
        pass


class Ainter(Inter):
    AINTER_FUNC1 = "Ainter.func1"

    def __init__(self, driver: Driver):
        super().__init__(driver)

    def func1(self):
        return self._driver.do1(self.AINTER_FUNC1)

    def func2(self):
        return self._driver.do2("Ainter.func2")


class Binter(Inter):
    def __init__(self, driver: Driver):
        super().__init__(driver)

    def func1(self):
        return self._driver.do1("Binter.func1")

    def func2(self):
        return self._driver.do2("Binter.func2")
