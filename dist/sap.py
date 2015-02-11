"""Mock out SAP classes"""


class FIDataCollection:
    records = []

    def AddRecord(self, record):
        """
        Add a new record(returned by DataManager.NewDataRecord()) to the
        collection.
        """
        self.records.append(record)

    def DeleteRecord(self, record):
        """Removes the specified record from collection."""
        pass
        # self.records.remove(record)

    def GetRecord(self, record, index=1):
        """Get a record at a given index from the collection."""
        for key, value in self.records[0].values.iteritems():
            record.SetField(key, value)

    def Size(self):
        """Returns number of records in a collection."""
        return len(self.records)

    def Truncate(self):
        """Removes all the records from collection."""
        pass


class FIDataManager:
    def NewDataRecord(self, ownership=1):
        """
        Creates a new record object.
        Returns a new object of type FlDataRecord.
        """
        return FIDataRecord()

    def DeleteDataRecord(self, record):
        """Deletes the memory allocated to the record object."""
        pass


class FIProperties:
    def GetProperty(self, property_name):
        """Returns the value of given property."""
        pass


class FIDataRecord:
    values = {}

    def SetField(self, field_name, value):
        """Stores a value in the specified field."""
        self.values[field_name] = value

    def GetField(self, field_name):
        """Get a field from record."""
        return self.values[field_name]


Collection = FIDataCollection()
DataManager = FIDataManager()
Properties = FIProperties()
