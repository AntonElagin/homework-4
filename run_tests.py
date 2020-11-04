import sys
import unittest
from cases.SecurityCase import SecurityTest
from cases.PasswordCase import PasswordTest
from cases.ContactsCase import ContactsTest

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
        unittest.makeSuite(PasswordTest),
        unittest.makeSuite(ContactsTest),
        unittest.makeSuite(SecurityTest)
    )
    )

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())