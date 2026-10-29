"""Non-regression: the detections must stay identical to the ones of release 0.0.9 (lingua 1.3.1, fasttext-wheel).

parity_cases.json holds synthetic chat messages (several languages, case/spacing/punctuation variants) with the
(language, reliable) pair returned by 0.0.9.
"""
import json
import pathlib

import pytest

import ShortLanguageDetection

CASES = json.loads((pathlib.Path(__file__).parent / 'parity_cases.json').read_text(encoding='utf-8'))
detector = ShortLanguageDetection.Detector()


@pytest.mark.parametrize('text,language,reliable', CASES)
def test_same_detection_as_0_0_9(text, language, reliable):
    assert detector.detect(text) == (language, reliable)
