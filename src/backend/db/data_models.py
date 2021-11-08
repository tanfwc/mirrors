# coding=utf-8
from typing import (
    Dict,
    AnyStr,
    List,
    Optional
)
from dataclasses import (
    dataclass,
    field,
)
import json


@dataclass
class LocationData:
    latitude: float
    longitude: float


@dataclass
class _MirrorYamlDataBase:
    name: AnyStr
    update_frequency: AnyStr
    sponsor_name: AnyStr
    sponsor_url: AnyStr
    email: AnyStr
    geolocation: Optional[dict] = field(default_factory=dict)


@dataclass
class _MirrorYamlDataDefaultBase:
    urls: Dict[AnyStr, AnyStr] = field(default_factory=dict)
    subnets: List[AnyStr] = field(default_factory=list)
    asn: Optional[AnyStr] = None
    cloud_type: AnyStr = ''
    cloud_region: AnyStr = ''
    private: bool = False


@dataclass
class MirrorYamlData(_MirrorYamlDataDefaultBase, _MirrorYamlDataBase):
    pass


@dataclass
class _MirrorDataBase:
    continent: AnyStr
    country: AnyStr
    state: AnyStr
    city: AnyStr
    ip: AnyStr
    ipv6: bool
    location: LocationData


@dataclass
class _MirrorDataDefaultBase:
    status: AnyStr = "ok"
    isos_link: Optional[AnyStr] = None


@dataclass
class MirrorData(
    _MirrorDataDefaultBase,
    _MirrorYamlDataDefaultBase,
    _MirrorYamlDataBase,
    _MirrorDataBase,
):

    @staticmethod
    def load_from_json(dct: Dict):
        return MirrorData(
            name=dct['name'],
            continent=dct['continent'],
            country=dct['country'],
            state=dct['state'],
            city=dct['city'],
            ip=dct['ip'],
            ipv6=dct['ipv6'],
            location=LocationData(
                latitude=dct['location']['latitude'],
                longitude=dct['location']['longitude'],
            ),
            status=dct['status'],
            update_frequency=dct['update_frequency'],
            sponsor_name=dct['sponsor_name'],
            sponsor_url=dct['sponsor_url'],
            email=dct['email'],
            asn=dct['asn'],
            urls=dct['urls'],
            subnets=dct['subnets'],
            cloud_type=dct['cloud_type'],
        )

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

@dataclass
class RepoData:
    name: AnyStr
    path: AnyStr
    arches: List[AnyStr] = field(default_factory=list)


@dataclass
class MainConfig:
    allowed_outdate: AnyStr
    mirrors_dir: AnyStr
    versions: List[AnyStr] = field(default_factory=list)
    duplicated_versions: List[AnyStr] = field(default_factory=list)
    arches: List[AnyStr] = field(default_factory=list)
    required_protocols: List[AnyStr] = field(default_factory=list)
    repos: List[RepoData] = field(default_factory=list)