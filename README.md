# dedrm
Windows script to help automate removing drm using Adobe Digital Editions, Calibre (with DeDRM), and NewFileGo.

 - Use [NewFileGo](http://www.joejoesoft.com/vcms/170/) to monitor desired directory for new ascm files, and "My Digital Editions" directory for new epub files
 - Set NewFileGo to call `python <path_to_dedrm.py> "%s"` (%s passes new file path to script)
 - dedrm.py will open ascm files using Adobe Digital Editions, and epub files using Calibre(with [DeDRM tools](https://github.com/apprenticeharper/DeDRM_tools) plugin)
