from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestJelesJegy(TestCase):
    def test_feladat_kozbe_tobb(self):
        jegyek="4, 5, 3, 5, 3, 2, 3, 5, 5, 2"
        aktualis = feladatok.jeles(jegyek)
        elvart = 4
        print(jegyek)
        self.assertEqual(elvart, aktualis, "Rosszul határozta meg, hogy hány jeles jegy van a jegyek között!")
