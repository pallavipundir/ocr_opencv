import tesseract

api = tesseract.TessBaseAPI()
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyz")
api.SetPageSegMode(tesseract.PSM_AUTO)
# Qhull installation 
#if config_parser.has_option('qhull','install-dir'):
 #   _qhulldir = config_parser.get('qhull','install-dir').strip()
#else:
# Ask user for qhull directory
 #   qstr = 'Please enter the path to an existing directory where qhull should be installed:- '
  #  qstr = 'C:/Users/pallavi.pundir/Downloads/countries'
##    _qhulldir = os.path.expanduser(raw_input(qstr).strip())
   # _qhulldir = os.path.expanduser(qstr)
mImgFile = "C:/Users/pallavi.pundir/Downloads/countries/alabama/formatted images/IDI(1).jpg"
mBuffer=open(mImgFile,"rb").read()
result = tesseract.ProcessPagesBuffer(mBuffer,len(mBuffer),api)
print "result(ProcessPagesBuffer)=",result