import pytest
import unittest
from tests.results_service import csr1_1,csr1_2,csr1_3,scsr1
from src.services.service import service_get_conesearch
    
class TestServiceConesearch(unittest.TestCase):
    @pytest.patch('src.services.service.catsHTM.cone_search')
    def test_case1(self,cone_search_mock):
        cone_search_mock.return_value = csr1_1, csr1_2, csr1_3
        result = service_get_conesearch(catalog = "", request = {"ra": 0, "dec" : 0, "radius": 0}, path = "/data")
        self.assertEquals(scsr1,result) 


