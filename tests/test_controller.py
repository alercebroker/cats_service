import os

os.environ["DATA_PATH"] = "/home/usuario/Documentos/data"
os.environ[
    "CATALOGS"
] = "TMASSxsc,AAVSO_VSX,AKARI,CRTS_per_var,FIRST,NVSS,ROSATfsc,SWIREz"
from unittest import TestCase, mock
from src.controllers.controller import (
    controller_conesearch,
    controller_crossmatch,
    controller_conesearch_all,
    controller_crossmatch_all,
)
from tests.results_controller import *
from tests.utils import round_controller_conesearch, round_controller_crossmatch
from tests.results_service import *
from src.models.model_cross_match import ModelCrossMatch


class TestControllerConesearch(TestCase):
    @mock.patch("src.services.service.cone_search")
    def test_case1(self, cone_search_mock):
        cone_search_mock.return_value = (
            cone_search_result1_1,
            cone_search_result1_2,
            cone_search_result1_3,
        )
        result = controller_conesearch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 200}
        )
        result = round_controller_conesearch(result)
        controller_conesearch_result1_1 = round_controller_conesearch(
            controller_conesearch_result1
        )
        self.assertEqual(result, controller_conesearch_result1_1)

    @mock.patch("src.services.service.cone_search")
    def test_case2(self, cone_search_mock):
        cone_search_mock.return_value = (
            cone_search_result2_1,
            cone_search_result2_2,
            cone_search_result2_3,
        )
        result = controller_conesearch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 0}
        )
        result = round_controller_conesearch(result)
        controller_conesearch_result2_1 = round_controller_conesearch(
            controller_conesearch_result2
        )
        self.assertEqual(result, controller_conesearch_result2_1)


class TestControllerCrossmatch(TestCase):
    def fake_get_min_distance(self, *args, **kwargs):
        return distance_result

    @mock.patch.object(ModelCrossMatch, "get_min_distance", new=fake_get_min_distance)
    @mock.patch("src.services.service.cone_search")
    def test_case1(self, cone_search_mock):
        cone_search_mock.return_value = (
            cone_search_result1_1,
            cone_search_result1_2,
            cone_search_result1_3,
        )
        result = controller_crossmatch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 200}
        )

        result = round_controller_crossmatch(result)
        controller_crossmatch_result1_1 = round_controller_crossmatch(
            controller_crossmatch_result1
        )

        self.assertEqual(result, controller_crossmatch_result1_1)

    @mock.patch.object(ModelCrossMatch, "get_min_distance", new=fake_get_min_distance)
    @mock.patch("src.services.service.cone_search")
    def test_case2(self, cone_search_mock):
        cone_search_mock.return_value = (
            cone_search_result2_1,
            cone_search_result2_2,
            cone_search_result2_3,
        )
        result = controller_crossmatch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 0}
        )
        result = round_controller_crossmatch(result)
        controller_crossmatch_result2_1 = round_controller_crossmatch(
            controller_crossmatch_result2
        )
        self.assertEqual(result, controller_crossmatch_result2_1)

    @mock.patch.object(ModelCrossMatch, "get_min_distance", new=fake_get_min_distance)
    @mock.patch("src.services.service.cone_search")
    def test_case3(self, cone_search_mock):
        cone_search_mock.return_value = (
            cone_search_result2_1,
            cone_search_result2_2,
            cone_search_result2_3,
        )
        result = controller_crossmatch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": None}
        )
        result = round_controller_crossmatch(result)
        controller_crossmatch_result3_1 = round_controller_crossmatch(
            controller_crossmatch_result3
        )

        self.assertEqual(result, controller_crossmatch_result3_1)


class TestControllerConesearchAll(TestCase):
    @mock.patch("src.services.service.service_get_conesearch")
    def test_case1(self, service_get_conesearch_mock):
        service_get_conesearch_mock.side_effect = [
            service_cone_search_result1_1,
            service_cone_search_result1_2,
            service_cone_search_result1_3,
            service_cone_search_result1_4,
            service_cone_search_result1_5,
            service_cone_search_result1_6,
            service_cone_search_result1_7,
            service_cone_search_result1_8,
        ]
        result = controller_conesearch_all(request={"ra": 1, "dec": 0, "radius": 200})
        self.assertEqual(result, controller_conesearch_all_result1)

    @mock.patch("src.services.service.service_get_conesearch")
    def test_case2(self, service_get_conesearch_mock2):
        service_get_conesearch_mock2.side_effect = [
            service_cone_search_result2_1,
            service_cone_search_result2_2,
            service_cone_search_result2_3,
            service_cone_search_result2_4,
            service_cone_search_result2_5,
            service_cone_search_result2_6,
            service_cone_search_result2_7,
            service_cone_search_result2_8,
        ]
        result = controller_conesearch_all(request={"ra": 1, "dec": 0, "radius": 0})
        self.assertEqual(result, controller_conesearch_all_result2)


class TestControllerCrossmatchAll(TestCase):
    @mock.patch("src.services.service.service_get_crossmatch")
    def test_case1(self, service_get_crossmatch_mock):
        service_get_crossmatch_mock.side_effect = [
            service_cross_match_result1_1,
            service_cross_match_result1_2,
            service_cross_match_result1_3,
            service_cross_match_result1_4,
            service_cross_match_result1_5,
            service_cross_match_result1_6,
            service_cross_match_result1_7,
            service_cross_match_result1_8,
        ]
        result = controller_crossmatch_all(request={"ra": 1, "dec": 0, "radius": 200})
        self.assertEqual(result, controller_crossmatch_all_result1)

    @mock.patch("src.services.service.service_get_crossmatch")
    def test_case2(self, service_get_crossmatch_mock2):
        service_get_crossmatch_mock2.side_effect = [
            service_cross_match_result2_1,
            service_cross_match_result2_2,
            service_cross_match_result2_3,
            service_cross_match_result2_4,
            service_cross_match_result2_5,
            service_cross_match_result2_6,
            service_cross_match_result2_7,
            service_cross_match_result2_8,
        ]
        result = controller_crossmatch_all(request={"ra": 1, "dec": 0, "radius": 0})
        self.assertEqual(result, controller_crossmatch_all_result2)

    @mock.patch("src.services.service.service_get_crossmatch")
    def test_case3(self, service_get_crossmatch_mock3):
        service_get_crossmatch_mock3.side_effect = [
            service_cross_match_result3_1,
            service_cross_match_result3_2,
            service_cross_match_result3_3,
            service_cross_match_result3_4,
            service_cross_match_result3_5,
            service_cross_match_result3_6,
            service_cross_match_result3_7,
            service_cross_match_result3_8,
        ]
        result = controller_crossmatch_all(request={"ra": 1, "dec": 0, "radius": None})
        self.assertEqual(result, controller_crossmatch_all_result3)
