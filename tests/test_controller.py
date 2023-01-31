import pytest
from unittest import TestCase, mock
from ..src.controllers.controler import (
    controller_conesearch,
    controller_crossmatch,
    controller_conesearch_all,
    controller_crossmatch_all,
)
from results_controller import *
from test_controller import *
from ..src.controllers.constants import map_ra_dec, radius_dict


class TestControllerConesearch(TestCase):
    def test_case1(self):
        result = controller_conesearch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 200}
        )
        self.assertEqual(result, controller_conesearch_result1)

    def test_case2(self):
        result = controller_conesearch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 0}
        )
        self.assertEqual(result, controller_conesearch_result2)

    def test_case3(self):
        result = controller_conesearch(catalog="FIRST", request={"ra": 1, "dec": 0})
        self.assertEqual(result, controller_conesearch_result3)


class TestControllerCrossmatch(TestCase):
    def test_case1(self):
        result = controller_crossmatch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 200}
        )
        self.assertEqual(result, controller_crossmatch_result1)

    def test_case2(self):
        result = controller_crossmatch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 0}
        )
        self.assertEqual(result, controller_crossmatch_result2)

    def test_case3(self):
        result = controller_crossmatch(catalog="FIRST", request={"ra": 1, "dec": 0})
        self.assertEqual(result, controller_crossmatch_result3)

    def test_case4(self):
        result = controller_crossmatch(
            catalog="FIRST", request={"ra": 1, "radius": 200}
        )
        self.assertEqual(result, controller_crossmatch_result4)


class TestControllerConesearchAll(TestCase):
    def test_case1(self):
        result = controller_conesearch_all(
            catalogs, request={"ra": 1, "dec": 0, "radius": 200}, path="/data"
        )
        self.assertEqual(result, controller_conesearch_all_result1)

    def test_case2(self):
        result = controller_conesearch_all(
            catalogs, request={"ra": 1, "dec": 0, "radius": 0}, path="/data"
        )
        self.assertEqual(result, controller_conesearch_all_result2)

    def test_case3(self):
        result = controller_conesearch_all(
            catalogs, request={"ra": 1, "radius": 200}, path="/data"
        )
        self.assertEqual(result, controller_conesearch_all_result3)


class TestControllerCrossmatchAll(TestCase):
    def test_case1(self):
        result = controller_crossmatch_all(
            catalogs,
            request={"ra": 1, "dec": 0, "radius": 200},
            path="/data",
            map_ra_dec=map_ra_dec,
            radius_dict=radius_dict,
        )
        self.assertEqual(result, controller_crossmatch_all_result1)

    def test_case2(self):
        result = controller_crossmatch_all(
            catalogs,
            request={"ra": 1, "dec": 0, "radius": 0},
            path="/data",
            map_ra_dec=map_ra_dec,
            radius_dict=radius_dict,
        )
        self.assertEqual(result, controller_crossmatch_all_result2)

    def test_case3(self):
        result = controller_crossmatch_all(
            catalogs,
            request={"ra": 1, "dec": 0},
            path="/data",
            map_ra_dec=map_ra_dec,
            radius_dict=radius_dict,
        )
        self.assertEqual(result, controller_crossmatch_all_result3)

    def test_case4(self):
        result = controller_crossmatch_all(
            catalogs,
            request={"ra": 1, "radius": 200},
            path="/data",
            map_ra_dec=map_ra_dec,
            radius_dict=radius_dict,
        )
        self.assertEqual(result, controller_crossmatch_all_result4)
