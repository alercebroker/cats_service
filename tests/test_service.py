import pytest
from unittest import mock, TestCase
from tests.results_service import *
from src.services.service import service_get_conesearch, service_get_conesearch_all


class TestServiceConesearch(TestCase):
    @mock.patch("src.services.service.cone_search")
    def test_case1(self, cone_search_mock):
        cone_search_mock.return_value = csr1_1, csr1_2, csr1_3
        result = service_get_conesearch(
            catalog="FIRST", request={"ra": 1, "dec": 0, "radius": 200}, path="/data"
        )
        self.assertEqual(scsr1, result)

    @mock.patch("src.services.service.cone_search")
    def test_case2(self, cone_search_mock2):
        with pytest.raises(Exception):
            cone_search_mock2.return_value = csr2_1, csr2_2, csr2_3
            result = service_get_conesearch(
                catalog="FIRST", request={"ra": 0, "dec": 0, "radius": 0}, path="/data"
            )
            self.assertEqual(scsr2, result)


class TestServiceConesearchAll(TestCase):
    @mock.patch("src.services.service.service_get_conesearch")
    def test_case1(self, service_get_conesearch_mock):
        service_get_conesearch_mock.side_effect = [
            scsr1_1,
            scsr1_2,
            scsr1_3,
            scsr1_4,
            scsr1_5,
            scsr1_6,
            scsr1_7,
            scsr1_8,
        ]
        result = service_get_conesearch_all(
            catalogs, request={"ra": 1, "dec": 0, "radius": 200}, path="/data"
        )
        self.assertEqual(scsar1, result)

    @mock.patch("src.services.service.service_get_conesearch")
    def test_case2(self, service_get_conesearch_mock2):
        service_get_conesearch_mock2.side_effect = [
            scsr2_1,
            scsr2_2,
            scsr2_3,
            scsr2_4,
            scsr2_5,
            scsr2_6,
            scsr2_7,
            scsr2_8,
        ]
        result = service_get_conesearch_all(
            catalogs, request={"ra": 0, "dec": 0, "radius": 0}, path="/data"
        )
        self.assertEqual(scsar2, result)
