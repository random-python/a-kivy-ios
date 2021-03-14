#
#
#

from kivy_ios.toolchain import PythonRecipe


class KivyMD_Recipe(PythonRecipe):

    name = 'kivymd'

    site_packages_name = 'kivymd'

    version = 'ba2ae628a2c2f25d1499c6eeaac96fbb6ff7c48a'
    url = "https://github.com/kivymd/KivyMD/archive/{version}.zip"

    depends = ['kivy', 'pillow']

    # call_hostpython_via_targetpython = False
    # install_in_hostpython = True


recipe = KivyMD_Recipe()
