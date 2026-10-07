import pytest

import ShortLanguageDetection

detector = ShortLanguageDetection.Detector()

CASES = [
    ('hello how are you today', 'en'), ('bonjour tout le monde', 'fr'), ('hola amigos como estan', 'es'),
    ('guten morgen zusammen', 'de'), ('これは日本語のテストです', 'ja'), ('привет всем как дела', 'ru'),
    ('olá pessoal tudo bem', 'pt'), ('안녕하세요 여러분', 'ko'), ('你好大家', 'zh'), ('wie geht es dir heute', 'de'),
]


@pytest.mark.parametrize('text,expected', CASES)
def test_detects_language(text, expected):
    code, reliable = detector.detect(text)
    assert code == expected


def test_returns_tuple_for_tiny_text():
    code, reliable = detector.detect('ah')
    assert isinstance(code, str) and isinstance(reliable, bool)
