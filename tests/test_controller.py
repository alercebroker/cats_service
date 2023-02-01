import pytest
import os
from unittest import TestCase, mock
from src.controllers.controler import (
    controller_conesearch,
    controller_crossmatch,
    controller_conesearch_all,
    controller_crossmatch_all,
)
from tests.results_controller import *
from src.controllers.constants import map_ra_dec, radius_dict
from tests.truncar import round_controller_conesearch, round_controller_crossmatch


class TestControllerConesearch(TestCase):

    @mock.patch.dict(os.environ, {"DATA_PATH": "/home/usuario/Documentos/data"})
    def test_case1(self):
        result = controller_conesearch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 200}
        )
        print(result)

        result = round_controller_conesearch(result)
        controller_conesearch_result1_1 = round_controller_conesearch(controller_conesearch_result1)
        self.assertEqual(result,controller_conesearch_result1_1)
    @mock.patch.dict(os.environ, {"DATA_PATH": "/home/usuario/Documentos/data"})
    def test_case2(self):
        result = controller_conesearch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 0}
        )
        result = round_controller_conesearch(result)
        controller_conesearch_result2_1 = round_controller_conesearch(controller_conesearch_result2)
        self.assertEqual(result, controller_conesearch_result2_1)



class TestControllerCrossmatch(TestCase):
    @mock.patch.dict(os.environ, {"DATA_PATH": "/home/usuario/Documentos/data"})
    def test_case1(self):
        result = controller_crossmatch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 200}
        )
        result = round_controller_crossmatch(result)
        controller_crossmatch_result1_1 = round_controller_crossmatch(controller_crossmatch_result1)


        self.assertEqual(result, controller_crossmatch_result1_1)
    @mock.patch.dict(os.environ, {"DATA_PATH": "/home/usuario/Documentos/data"})
    def test_case2(self):
        
        result = controller_crossmatch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 0}
        )
        result = round_controller_crossmatch(result)
        controller_crossmatch_result2_1 = round_controller_crossmatch(controller_crossmatch_result2)
        self.assertEqual(result, controller_crossmatch_result2_1)

    @mock.patch.dict(os.environ, {"DATA_PATH": "/home/usuario/Documentos/data"})
    def test_case3(self):
        result = controller_crossmatch(catalog="FIRST", request={"ra": 1, "dec": 0, "radius": None})
        result = round_controller_crossmatch(result)
        controller_crossmatch_result3_1 = round_controller_crossmatch(controller_crossmatch_result2)

        self.assertEqual(result, controller_crossmatch_result3_1)



class TestControllerConesearchAll(TestCase):
    a = "".join(catalogs)
    os.environ["CATALOGS"] = a
    @mock.patch.dict(os.environ, {"DATA_PATH": "/home/usuario/Documentos/data"})
    def test_case1(self):
        result = controller_conesearch_all(
            request={"ra": 1, "dec": 0, "radius": 200}
        )
        f = open("resultmock",'w')
        print(result, file = f)
        f.close
        f = open("resultmock2",'w')
        print(controller_conesearch_all_result1, file = f)
        f.close

        self.assertEqual(result, controller_conesearch_all_result1)
    @mock.patch("src.controllers.controler.os")
    def test_case2(self,catalogs_mock):
        catalogs_mock.return_value = catalogs
        result = controller_conesearch_all(
            request={"ra": 1, "dec": 0, "radius": 0}
        )
        self.assertEqual(result, controller_conesearch_all_result2)



class TestControllerCrossmatchAll(TestCase):
    @mock.patch("src.controllers.controler.os")
    def test_case1(self,mock_catalogs):
        mock_catalogs.return_value = catalogs
        result = controller_crossmatch_all(
            request={"ra": 1, "dec": 0, "radius": 200}
        )
        self.assertEqual(result, controller_crossmatch_all_result1)
    @mock.patch("src.controllers.controler.os")
    def test_case2(self,mock_catalogs):
        mock_catalogs.return_value = catalogs
        result = controller_crossmatch_all(
            request={"ra": 1, "dec": 0, "radius": 0}
        )
        self.assertEqual(result, controller_crossmatch_all_result2)
    @mock.patch("src.controllers.controler.os")
    def test_case3(self,mock_catalogs):
        mock_catalogs.return_value = catalogs
        result = controller_crossmatch_all(
            request={"ra": 1, "dec": 0, "radius": None}
        )
        self.assertEqual(result, controller_crossmatch_all_result3)

