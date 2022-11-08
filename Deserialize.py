from typing import List
from typing import Any
from dataclasses import dataclass
import json


class Json:
    pass


@dataclass
class Data:
    json: Json
    html: str

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        _json = Json.from_dict(obj.get("json"))
        _html = str(obj.get("html"))
        return Data(_json, _html)

@dataclass
class Item:
    name: str
    price: int
    quantity: int
    nds: int
    ndsSum: int
    productType: int
    paymentType: int
    sum: int
    itemsQuantityMeasure: int

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        _name = str(obj.get("name"))
        _price = int(obj.get("price"))
        _quantity = int(obj.get("quantity"))
        _nds = int(obj.get("nds"))
        _ndsSum = int(obj.get("ndsSum"))
        _productType = int(obj.get("productType"))
        _paymentType = int(obj.get("paymentType"))
        _sum = int(obj.get("sum"))
        _itemsQuantityMeasure = int(obj.get("itemsQuantityMeasure"))
        return Item(_name, _price, _quantity, _nds, _ndsSum, _productType, _paymentType, _sum, _itemsQuantityMeasure)


class Metadata:
    pass


@dataclass
class Json:
    messageFiscalSign: float
    code: int
    fiscalDocumentFormatVer: int
    fiscalDriveNumber: str
    kktRegId: str
    userInn: str
    fiscalDocumentNumber: int
    dateTime: str
    fiscalSign: int
    shiftNumber: int
    requestNumber: int
    operationType: int
    totalSum: int
    operator: str
    items: List[Item]
    ndsNo: int
    user: str
    retailPlaceAddress: str
    retailPlace: str
    appliedTaxationType: int
    fnsUrl: str
    cashTotalSum: int
    ecashTotalSum: int
    prepaidSum: int
    creditSum: int
    provisionSum: int
    region: str
    numberKkt: str
    redefine_mask: int
    metadata: Metadata

    @staticmethod
    def from_dict(obj: Any) -> 'Json':
        _messageFiscalSign = float(obj.get("messageFiscalSign"))
        _code = int(obj.get("code"))
        _fiscalDocumentFormatVer = int(obj.get("fiscalDocumentFormatVer"))
        _fiscalDriveNumber = str(obj.get("fiscalDriveNumber"))
        _kktRegId = str(obj.get("kktRegId"))
        _userInn = str(obj.get("userInn"))
        _fiscalDocumentNumber = int(obj.get("fiscalDocumentNumber"))
        _dateTime = str(obj.get("dateTime"))
        _fiscalSign = int(obj.get("fiscalSign"))
        _shiftNumber = int(obj.get("shiftNumber"))
        _requestNumber = int(obj.get("requestNumber"))
        _operationType = int(obj.get("operationType"))
        _totalSum = int(obj.get("totalSum"))
        _operator = str(obj.get("operator"))
        _items = [Item.from_dict(y) for y in obj.get("items")]
        _ndsNo = int(obj.get("ndsNo"))
        _user = str(obj.get("user"))
        _retailPlaceAddress = str(obj.get("retailPlaceAddress"))
        _retailPlace = str(obj.get("retailPlace"))
        _appliedTaxationType = int(obj.get("appliedTaxationType"))
        _fnsUrl = str(obj.get("fnsUrl"))
        _cashTotalSum = int(obj.get("cashTotalSum"))
        _ecashTotalSum = int(obj.get("ecashTotalSum"))
        _prepaidSum = int(obj.get("prepaidSum"))
        _creditSum = int(obj.get("creditSum"))
        _provisionSum = int(obj.get("provisionSum"))
        _region = str(obj.get("region"))
        _numberKkt = str(obj.get("numberKkt"))
        _redefine_mask = int(obj.get("redefine_mask"))
        _metadata = Metadata.from_dict(obj.get("metadata"))
        return Json(_messageFiscalSign, _code, _fiscalDocumentFormatVer, _fiscalDriveNumber, _kktRegId, _userInn, _fiscalDocumentNumber, _dateTime, _fiscalSign, _shiftNumber, _requestNumber, _operationType, _totalSum, _operator, _items, _ndsNo, _user, _retailPlaceAddress, _retailPlace, _appliedTaxationType, _fnsUrl, _cashTotalSum, _ecashTotalSum, _prepaidSum, _creditSum, _provisionSum, _region, _numberKkt, _redefine_mask, _metadata)

@dataclass
class Manual:
    fn: str
    fd: str
    fp: str
    check_time: str
    type: str
    sum: str

    @staticmethod
    def from_dict(obj: Any) -> 'Manual':
        _fn = str(obj.get("fn"))
        _fd = str(obj.get("fd"))
        _fp = str(obj.get("fp"))
        _check_time = str(obj.get("check_time"))
        _type = str(obj.get("type"))
        _sum = str(obj.get("sum"))
        return Manual(_fn, _fd, _fp, _check_time, _type, _sum)

@dataclass
class Metadata:
    id: float
    ofdId: str
    receiveDate: str
    subtype: str
    address: str

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        _id = float(obj.get("id"))
        _ofdId = str(obj.get("ofdId"))
        _receiveDate = str(obj.get("receiveDate"))
        _subtype = str(obj.get("subtype"))
        _address = str(obj.get("address"))
        return Metadata(_id, _ofdId, _receiveDate, _subtype, _address)

@dataclass
class Request:
    qrurl: str
    qrfile: str
    qrraw: str
    manual: Manual

    @staticmethod
    def from_dict(obj: Any) -> 'Request':
        _qrurl = str(obj.get("qrurl"))
        _qrfile = str(obj.get("qrfile"))
        _qrraw = str(obj.get("qrraw"))
        _manual = Manual.from_dict(obj.get("manual"))
        return Request(_qrurl, _qrfile, _qrraw, _manual)

@dataclass
class Root:
    code: int
    first: int
    data: Data
    request: Request

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _code = int(obj.get("code"))
        _first = int(obj.get("first"))
        _data = Data.from_dict(obj.get("data"))
        _request = Request.from_dict(obj.get("request"))
        return Root(_code, _first, _data, _request)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
