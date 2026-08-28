from budget.service import GetInputService


class TestGetInputService:
    def test_should_return_correct_input_data(self, monkeypatch):
        get_input_service = GetInputService()

        def fake_get_input_from_keyboard() -> str:
            return "aaa -b --cc --dd=ee fff -g --hh --ii=jj"

        monkeypatch.setattr(
            get_input_service,
            "_get_input_from_keyboard",
            fake_get_input_from_keyboard
        )
        received = get_input_service.get_input()
        expected = "aaa -b --cc --dd=ee fff -g --hh --ii=jj"
        assert received == expected
