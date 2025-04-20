from typing import List
from pydantic import BaseModel, RootModel, Field, NaiveDatetime


class SystemConnection(BaseModel):
    SystemConnectionId: str = Field(min_length=65)
    ConnectingId: str = Field(min_length=32)


class System(BaseModel):
    SystemId: str = Field(min_length=32)
    Name: str
    NaturalId: str
    Type: str
    PositionX: float
    PositionY: float
    PositionZ: float
    SectorId: str
    SubSectorId: str
    UserNameSubmitted: str
    Timestamp: NaiveDatetime
    Connections: List[SystemConnection] = []


class SystemList(RootModel):
    root: List[System]

    def __iter__(self):
        return iter(self.root)

"""
{
    "Connections": [
      {
        "SystemConnectionId": "014421a50088da622befe22fe1b12e7e-1ef59a64aa3e127f820a71be9b4d6716",
        "ConnectingId": "1ef59a64aa3e127f820a71be9b4d6716"
      },
      {
        "SystemConnectionId": "014421a50088da622befe22fe1b12e7e-58352be19029146f3fde30b40fb550eb",
        "ConnectingId": "58352be19029146f3fde30b40fb550eb"
      },
      {
        "SystemConnectionId": "014421a50088da622befe22fe1b12e7e-4727759ffab50eab2b80554310d5e5c4",
        "ConnectingId": "4727759ffab50eab2b80554310d5e5c4"
      },
      {
        "SystemConnectionId": "014421a50088da622befe22fe1b12e7e-ba7cd5859833d6035d305fb691e08af3",
        "ConnectingId": "ba7cd5859833d6035d305fb691e08af3"
      }
    ],
    "SystemId": "014421a50088da622befe22fe1b12e7e",
    "Name": "YK-024",
    "NaturalId": "YK-024",
    "Type": "K",
    "PositionX": 409.50921630859375,
    "PositionY": -16.564367294311523,
    "PositionZ": 92.88360595703125,
    "SectorId": "sector-46",
    "SubSectorId": "subsector-46-9",
    "UserNameSubmitted": "SAGANAKI",
    "Timestamp": "2025-04-19T16:52:00.648052"
  },
  {
    "Connections": [
      {
        "SystemConnectionId": "01616c4dc3d9d62eeb16bb863ccb3e0e-0b6bd15be768750c4e030edbcb402e87",
        "ConnectingId": "0b6bd15be768750c4e030edbcb402e87"
      },
      {
        "SystemConnectionId": "01616c4dc3d9d62eeb16bb863ccb3e0e-e7b7b113e1ff4a587f8159b92018619e",
        "ConnectingId": "e7b7b113e1ff4a587f8159b92018619e"
      }
    ],
    "SystemId": "01616c4dc3d9d62eeb16bb863ccb3e0e",
    "Name": "XU-753",
    "NaturalId": "XU-753",
    "Type": "G",
    "PositionX": -808.9539794921875,
    "PositionY": -183.02001953125,
    "PositionZ": 141.99322509765625,
    "SectorId": "sector-97",
    "SubSectorId": "subsector-97-22",
    "UserNameSubmitted": "SAGANAKI",
    "Timestamp": "2025-04-19T16:52:00.648052"
  }
"""

