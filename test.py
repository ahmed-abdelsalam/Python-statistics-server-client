import unittest
from read_xml import Read_xml
import os.path
from xmltest import XMLAssertions


#test cases
class TestStringMethods(unittest.TestCase ,XMLAssertions ):
    def test_Read_xml(self):
        self.assertTrue(Read_xml.ips)
        self.assertTrue(Read_xml.ports)
        self.assertTrue(Read_xml.usernames)
        self.assertTrue(Read_xml.passwords)
        self.assertTrue(Read_xml.alerts)

    def test_files(self):
        self.assertTrue(os.path.isfile('data.sqlite3'))
        self.assertTrue(os.path.isfile('config.py'))
        self.assertTrue(os.path.isfile('config.xml'))




if __name__ == '__main__':
    unittest.main()