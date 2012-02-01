from django.conf import settings

import sys

try:
    TEX_REPORT_TMP_PATH = settings.TEX_REPORT_TMP_PATH
except AttributeError:
    print "Please configure the 'TEX_REPORT_TMP_PATH' variable"
    sys.exit(1)
