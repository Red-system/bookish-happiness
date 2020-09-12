import unittest
from unittest.mock import builtins
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base

class DataBaseTest(unittest.TestCase):
    original_input = builtins.input

    def fake_input(self, entry):
        builtins.input = lambda _: entry
    
    def real_input(self):
        builtins.input = self.original_input

    def tearDown(self):
        self.real_input()
    
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)

        # set up output

