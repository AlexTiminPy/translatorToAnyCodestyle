import argparse

from main import \
    transform_to_camel_case, \
    transform_to_pascal_case, \
    transform_to_snake_case, \
    transform_to_kebab_case, \
    start_transform


def test_camel_case():
    assert 'someTextWithReturn' == transform_to_camel_case(['Some', 'text', 'with', 'RETURN'])


def test_pascal_case():
    assert 'SomeTextWithReturn' == transform_to_pascal_case(['Some', 'text', 'with', 'RETURN'])


def test_snake_case():
    assert 'some_text_with_return' == transform_to_snake_case(['Some', 'text', 'with', 'RETURN'])


def test_kebab_case():
    assert 'some-text-with-return' == transform_to_kebab_case(['Some', 'text', 'with', 'RETURN'])


def test_start_transform():

    namespace = argparse.Namespace(string='Some text with , . RETURN')
    assert start_transform(namespace) == ['Some', 'text', 'with', 'RETURN']

    namespace = argparse.Namespace(string='hj fhskdfh kh .,,..,  d,, . ')
    assert start_transform(namespace) == ['hj', 'fhskdfh', 'kh', 'd']
