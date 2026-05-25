from week2_PyDepth.storage_devoop import StorageDevice, DiskHealth
from unittest.mock import patch, mock_open
import unittest


class TestStorageclass(unittest.TestCase):




    def test_capacity_returns_float(self):
        with patch("builtins.open",mock_open(read_data="976773168")):
            device = StorageDevice("sda")
            result = device.capacity
            assert isinstance(result,float)
    def test_ssd(self):
        with patch("builtins.open",mock_open(read_data="0\n")):
            device = StorageDevice("sda")
            assert device.is_ssd == True