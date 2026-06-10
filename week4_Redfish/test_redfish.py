from unittest.mock import patch, MagicMock
from week4_Redfish.redfish_work import DriveHealth, RedfishClient
from week4_Redfish.test_redfish_client import MOCK_SYSTEMS,MOCK_DRIVE,MOCK_DRIVE_COLLECTION,MOCK_STORAGE
import unittest


class TestRedfish(unittest.TestCase):
    
    def test_get(self):
        with patch("requests.get") as mock_get:
            mock_response = MagicMock()
            mock_response.json.return_value = MOCK_SYSTEMS
            mock_get.return_value = mock_response

            client = RedfishClient("https://fakeip","admin","password")
            result = client.get("/redfish/v1/")
            assert result == MOCK_SYSTEMS


    def _make_response(self,data):
            mock_response = MagicMock()
            mock_response.json.return_value = data
            return mock_response

    def test_get_drives(self):
        with patch("requests.get") as mock_get:
            mock_get.side_effect=[
                self._make_response(MOCK_SYSTEMS),
                self._make_response(MOCK_STORAGE),
                self._make_response(MOCK_DRIVE_COLLECTION),
                self._make_response(MOCK_DRIVE),
            ]

            client = RedfishClient("http://fakeip","admin","password")
            drives = client.get_drives()

            assert len(drives)==1
            assert drives[0].name == "Drive 1"
            assert drives[0].health =="OK"
            assert drives[0].protocol == "NVMe"
            

    