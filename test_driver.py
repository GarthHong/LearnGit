from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch

from driver import Ainter, Adriver, Binter


class TestAinter(TestCase):
    # 아직 구현이 안 된 모듈을 Mock으로 정의한다.
    def test_func1_inter_driver2(self):

        with patch('driver.Adriver') as adriver:
            mock_adriver_inst = adriver.return_value

            def mock_adriver_do1(text: str) -> str:
                return "Adriver.do1: {}".format(text)

            mock_adriver_inst.do1.side_effect = mock_adriver_do1
            ainter = Ainter(mock_adriver_inst)

            self.assertEqual("Adriver.do1: Ainter.func1", ainter.func1())

    def test_func1_inter_driver(self):
        adriver = Mock()

        # Ainter는 테스트 대상 모듈
        # adriver는 Mock이라 type이 Driver는 아니지만
        # python의 특성 상 문제없이 injection된다.
        ainter = Ainter(adriver)

        # 아직 구현이 안 된 adriver에 대한
        # 동작을 아래와 같이 정의해준다.
        # 1. 메서드 동작을 내부 함수로 정의
        # '메서드명'.side_effect = '내부함수명' 으로 할당
        def mock_adriver_do1(text: str) -> str:
            return "Adriver.do1: {}".format(text)

        adriver.do1.side_effect = mock_adriver_do1

        # 2. 메서드 리턴값을 고정된 값으로 미리 할당
        # '메서드명'.return_value = '고정된 값'
        new_v = "Mock do2 ret"
        adriver.do2.return_value = new_v

        # Act & Assert
        self.assertEqual("Adriver.do1: Ainter.func1", ainter.func1())
        self.assertEqual("Mock do2 ret", ainter.func2())

    def test_func1_inter_driver2_using_mock(self):
        adriver = Mock()

        def mock_adriver_do1(text: str) -> str:
            return "Adriver.do1: {}".format(text)

        adriver.do1.side_effect = mock_adriver_do1
        ainter = Ainter(adriver)
        self.assertEqual("Adriver.do1: Ainter.func1", ainter.func1())
