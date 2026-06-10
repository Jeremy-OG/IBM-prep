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

            client = RedfishClient("https://fakeip","admin","admin")
            result = client.get("/redfish/v1/")
            assert result == MOCK_SYSTEMS