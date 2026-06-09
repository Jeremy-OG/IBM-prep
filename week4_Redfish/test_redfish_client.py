

MOCK_SYSTEMS = {
    "Members": [{"@odata.id": "/redfish/v1/Systems/1"}],
    "Members@odata.count": 1
}

MOCK_STORAGE = {
    "Members": [{"@odata.id": "/redfish/v1/Systems/1/Storage/1"}],
    "Members@odata.count": 1
}

MOCK_DRIVE_COLLECTION = {
    "Members": [{"@odata.id": "/redfish/v1/Systems/1/Storage/1/Drives/1"}],
    "Members@odata.count": 1
}

MOCK_DRIVE = {
    "Name": "Drive 1",
    "Status": {"State": "Enabled", "Health": "OK"},
    "CapacityBytes": 960197124096,
    "Protocol": "NVMe"
}