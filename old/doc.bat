del /q /s  "./doc/source/cpmel/"
rd  /s /q  "./doc/source/cpmel/"
del /q /s  "./doc/build/"
rd  /s /q  "./doc/build/"
"C:\Program Files\Autodesk\Maya2018\Python\Scripts\sphinx-apidoc" -l -f -o ./doc/source/cpmel/ ./build/debug/ -d 4
"C:\Program Files\Autodesk\Maya2018\Python\Scripts\sphinx-build" -b html ./doc/source/ ./doc/build/ 