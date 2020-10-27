rmdir __pycache__ /Q
rmdir build /Q
rmdir dist /Q
del main.spec /Q
pyinstaller main.py --onefile --noconsole --icon=ast\ico\discoxy.ico
