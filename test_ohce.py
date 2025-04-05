from ohce import Ohce

def test_reverses_input():
    ohce = Ohce()
    result = ohce.process("hello")
    assert result == "olleh"

def test_greeting_buenos_dias():
    ohce = Ohce(user="User", hour=8)
    assert ohce.greet() == "¡Buenos días User!"

def test_greeting_buenas_tardes():
    ohce = Ohce(user="User", hour=15)
    assert ohce.greet() == "¡Buenas tardes User!"

def test_greeting_buenas_noches():
    ohce = Ohce(user="User", hour=22)
    assert ohce.greet() == "¡Buenas noches User!"

def test_palindrome_input():
    ohce = Ohce()
    result = ohce.process("madam")
    assert result == "madam\n¡Bonita palabra!"

def test_stop_command():
    ohce = Ohce(user="User")
    result = ohce.process("Stop!")
    assert result == "¡Adiós User!"
