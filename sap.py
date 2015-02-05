"""Mock out SAP classes"""


class _Collection:
    records = []

    def AddRecord(self, record):
        self.records.append(record)

    def DeleteRecord(self, record):
        pass
        # self.records.remove(record)

    def GetRecord(self, record, num=1):
        for key, value in self.records[0].values.iteritems():
            record.SetField(key, value)

    def Size(self):
        return len(self.records)


class _DataManager:
    def NewDataRecord(self, num=1):
        return DSRecord()

    def DeleteDataRecord(self, num=1):
        pass


class DSRecord:
    values = {}

    def SetField(self, key, val):
        self.values[key] = val

    def GetField(self, key):
        return self.values[key]

Collection = _Collection()
DataManager = _DataManager()
