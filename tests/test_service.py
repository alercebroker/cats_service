import pytest
from unittest import mock, TestCase
from tests.results_service import *
from src.services.service import (
    service_get_conesearch,
    service_get_conesearch_all,
    service_get_crossmatch,
    service_get_crossmatch_all
)
from src.controllers.constants import map_ra_dec, radius_dict, catalog_map
from math import radians
from tests.truncar import round_cone_search, round_cross_match, round_cross_match_all, round_cone_search_all
from src.models.model_cross_match import ModelCrossMatch


class TestServiceConesearch(TestCase):
    @mock.patch("src.services.service.cone_search")
    def test_case1(self, cone_search_mock):
        cone_search_mock.return_value = cone_search_result1_1, cone_search_result1_2, cone_search_result1_3
        
        result = service_get_conesearch(
            catalog="FIRST", request={"ra":radians(float(1)), "dec": radians(float(0)) ,"radius": float(200)}, path="/data"
        )

        result = round_cone_search(result)
        service_cone_search_result1_2 = round_cone_search(service_cone_search_result1)
        self.assertEqual(service_cone_search_result1_2, result)

    @mock.patch("src.services.service.cone_search")
    def test_case2(self, cone_search_mock2):
        with pytest.raises(Exception):
            cone_search_mock2.return_value = cone_search_result2_1, cone_search_result2_2, cone_search_result2_3
            result = service_get_conesearch(
                catalog="FIRST", request={"ra":radians(float(1)), "dec": radians(float(0)) ,"radius": float(0)}, path="/data"
            )
            self.assertEqual(service_cone_search_result2, result)


class TestServiceConesearchAll(TestCase):
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
        result = service_get_conesearch_all(
            catalogs, request={"ra":radians(float(1)), "dec": radians(float(0)) ,"radius": float(200)}, path="/data"
        )

        result = round_cone_search_all(result)
        service_cone_search_all_result1_2 = round_cone_search_all(service_cone_search_all_result1)
        self.assertEqual(service_cone_search_all_result1_2, result)

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
        result = service_get_conesearch_all(
            catalogs, request={"ra":radians(float(1)), "dec": radians(float(0)) ,"radius": float(0)}, path="/data"
        )
        self.assertEqual(service_cone_search_all_result2, result)


class TestServiceCrossmach(TestCase):

    def fake_get_min_distance(self,*args, **kwargs):
        return distance_result



    @mock.patch.object(ModelCrossMatch, 'get_min_distance', new = fake_get_min_distance)
    #@mock.patch("src.models.model_cross_match.ModelCrossMatch.get_min_dist")
    @mock.patch("src.services.service.cone_search")
    def test_case1(self, cone_search_mock):
        #get_min_distance_mock.return_value = distance_result
        cone_search_mock.return_value = (
            cross_match_result1_1,
            cross_match_result1_2,
            cross_match_result1_3,
        )

        result = service_get_crossmatch(
            catalog="FIRST",
            request={"ra":radians(float(1)), "dec": radians(float(0)) ,"radius": float(200)},
            path="/data",
            map_ra_dec=map_ra_dec,
            radius_dict=radius_dict,
        )
        result = round_cross_match(result)
        service_cross_match_result1_2 = round_cross_match(service_cross_match_result1)

        self.assertEqual(service_cross_match_result1_2, result)

    @mock.patch.object(ModelCrossMatch, 'get_min_distance', new = fake_get_min_distance)
    @mock.patch("src.services.service.cone_search")
    def test_case2(self, cone_search_mock2):
        cone_search_mock2.return_value = (
            cross_match_result2_1,
            cross_match_result2_2,
            cross_match_result2_3,
        )
        result = service_get_crossmatch(
            catalog="FIRST",
            request={"ra":radians(float(1)), "dec": radians(float(0)) ,"radius": float(0)},
            path="/data",
            map_ra_dec=map_ra_dec,
            radius_dict=radius_dict,
        )
        result = round_cross_match(result)
        service_cross_match_result2_2 = round_cross_match(service_cross_match_result2)

        self.assertEqual(service_cross_match_result2_2, result)


    @mock.patch.object(ModelCrossMatch, 'get_min_distance', new = fake_get_min_distance)    
    @mock.patch("src.services.service.cone_search")
    def test_case3(self, cone_search_mock2):
        cone_search_mock2.return_value = (
            cross_match_result3_1,
            cross_match_result3_2,
            cross_match_result3_3,
        )
        result = service_get_crossmatch(
            catalog="FIRST",
            request={"ra":radians(float(1)), "dec": radians(float(0)) ,"radius": None},
            path="/data",
            map_ra_dec=map_ra_dec,
            radius_dict=radius_dict,
        )
        result = round_cross_match(result)
        service_cross_match_result3_2 = round_cross_match(service_cross_match_result3)

        self.assertEqual(service_cross_match_result3_2, result)


class TestServiceCrossmatchAll(TestCase):
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
        result = service_get_crossmatch_all(
            catalogs, request={"ra":radians(float(1)), "dec": radians(float(0)) ,"radius": float(200)}, path="/data", map_ra_dec=map_ra_dec, radius_dict=radius_dict
        )
        service_cross_match_all_result1_1 = round_cross_match_all(service_cross_match_all_result1)
        result = round_cross_match_all(result)
        self.assertEqual(service_cross_match_all_result1_1,result)