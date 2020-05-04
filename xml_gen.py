import unittest


def my_xml(tag_name: str, content: str = '', **kwargs: int) -> str:
    attrs = ''.join([f' {k}="{v}"' for k, v in kwargs.items()])
    
    return f'<{tag_name}{attrs}>{content}</{tag_name}>'


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual('<foo></foo>', my_xml('foo'))
        self.assertEqual('<foo>bar</foo>', my_xml('foo', 'bar'))
        self.assertEqual('<foo a="1" b="2" c="3">bar</foo>', my_xml('foo', 'bar', a=1, b=2, c=3))


if __name__ == '__main__':
    unittest.main()
