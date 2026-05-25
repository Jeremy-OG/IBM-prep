from week2_PyDepth.storage_devoop import StorageDevice, DiskHealth
from unittest.mock import patch, mock_open, AsyncMock, MagicMock
import unittest
import asyncio



class TestStorageclass(unittest.TestCase):




    def test_capacity_returns_float(self): # happy
        with patch("builtins.open",mock_open(read_data="976773168")):
            device = StorageDevice("sda")
            result = device.capacity
            assert isinstance(result,float)

    def test_capacity_file_not_found(self):# error
        with patch("builtins.open", side_effect=FileNotFoundError):
            device = StorageDevice("fakepath")
            with self.assertRaises(FileNotFoundError):
                _ = device.capacity

    def test_capacity_large_sector_count(self): #edge
        with patch("builtins.open", mock_open(read_data="99999999999999\n")):
            device = StorageDevice("sda")
            result = device.capacity
            assert isinstance(result, float)
            assert result > 1000



    def test_ssd(self):
        with patch("builtins.open", mock_open(read_data="0\n")):
            device = StorageDevice("sda")
            assert device.is_ssd == True

    def test_is_ssd_returns_false_for_hdd(self):
        with patch("builtins.open", mock_open(read_data="1\n")):
            device = StorageDevice("sda")
            assert device.is_ssd == False




    def test_name(self):
        with patch("builtins.open",mock_open(read_data="Samsung SSD 870\n")):
            device = StorageDevice("sda")
            assert device.name == "Samsung SSD 870"

    def test_name_returns_none_when_empty(self):
        with patch("builtins.open",mock_open(read_data='')):
            device = StorageDevice("sda")
            result = device.name
            assert result is None

    def test_get_smart_health(self):
        mock_data = {
            "temperature": {"current": 38},
            "power_on_time": {"hours": 4821},
            "ata_smart_attributes": {"table": [{"raw": {"value": 0}}]},
            "smart_status": {"passed": True}
        }
        mock_file = AsyncMock()
        mock_file.__aenter__.return_value.read = AsyncMock(return_value='placeholder')

        with patch("aiofiles.open", return_value=mock_file):
            with patch("json.loads", return_value=mock_data):
                device = StorageDevice("fake.json")
                result = asyncio.run(device.get_smart_health())
                assert isinstance(result, DiskHealth)

    def test_get_smart_health_invalid_data(self):
        mock_file = AsyncMock()
        mock_file.__aenter__.return_value.read = AsyncMock(return_value='placeholder')
        
        with patch("aiofiles.open", return_value=mock_file):
            with patch("json.loads", side_effect=KeyError):
                device = StorageDevice("fake.json")
                with self.assertRaises(KeyError):
                    asyncio.run(device.get_smart_health())


