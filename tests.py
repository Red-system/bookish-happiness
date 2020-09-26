import unittest
import io
from app_test.utils import DataBaseTest
from app.models import Product
from app.core import create_product, enter_product
from unittest.mock import patch, builtins


class TestFrigo(DataBaseTest):

    def test_create_product(self):
        name = 'test'
        create_product(self.session, name=name)
        self.assertTrue(Product.exists(self.session, name=name))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enter_product_for_unexisting_product(self, mock_stdout):
        # define new product name
        product_name = 'tagada'
        # if the next function has an input then enter the value 'IDK' stored in the product_name variable
        self.fake_input(product_name)

        # this is the next function
        enter_product(self.session)
        
        # get the output of the fucntion enter_product
        res = mock_stdout.getvalue()
        expected = "Product {} doesn't exist, do you want to add it ?\n".format(
            product_name
        )
        self.assertEqual(res, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enter_product_for_existing_product(self, mock_stdout):
        product_name = 'New product'
        create_product(self.session, name=product_name)
        self.fake_input(product_name)
        enter_product(self.session)
        res = mock_stdout.getvalue()
        self.assertEqual(res, "{} has been added !\n".format(product_name))
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enter_product_with_number(self, mock_stdout):
        product_name = '123'
        self.fake_input(product_name)
        enter_product(self.session)
        res = mock_stdout.getvalue()
        self.assertEqual(res, '{} is not valid\n'.format(product_name))    


if __name__ == '__main__':
    unittest.main()
