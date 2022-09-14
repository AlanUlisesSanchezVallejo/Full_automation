from test.test_FLow1 import *
from test.test_Flow2 import *

import HtmlTestRunner

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Test Reports'))