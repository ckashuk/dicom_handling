import json

from dcm.dicom_standard_validation.spec_reader.condition import Condition


class DefinitionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Condition):
            return obj.dict()
        return json.JSONEncoder.default(self, obj)
