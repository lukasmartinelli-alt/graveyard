"""Fake implementation of the SAP Python BODS runtime"""


class FIDataCollection:
    records = []

    def AddRecord(self, record):
        """
        Add a new record(returned by DataManager.NewDataRecord()) to the
        collection.
        For every NewDataRecord(), you can call AddRecord() only once.
        After you call AddRecord(), do not call DeleteDataRecord().
        """
        self.records.append(record)

    def DeleteRecord(self, record):
        """Removes the specified record from collection."""
        self.records.remove(record)

    def GetRecord(self, record, index):
        """Get a record at a given index from the collection."""
        if index < 1:
            raise ValueError("Indizes in SAP BODS start at 1 and not 0!")
        for key, value in self.records[index-1].values.iteritems():
            record.SetField(key, value)

    def Size(self):
        """
        Counts the number of records in the collection.
        Returns number of records in a collection.
        """
        return len(self.records)

    def Truncate(self):
        """Removes all the records from collection."""
        self.records = []


class FIDataManager:
    def NewDataRecord(self, ownership=1):
        """
        Creates a new record object. Do not use this method in a loop,
        otherwise the Python expression may experience a
        memory leak. Depending on the expression, you'll probably want to
        place this method at the beginning of the expression.
        Returns a new object of type FlDataRecord.
        """
        return FIDataRecord()

    def DeleteDataRecord(self, record):
        """
        Deletes the memory allocated to the record object.
        Do not call DeleteDataRecord() after calling AddRecord().
        """
        del record


class FIProperties:
    values = {}

    def GetProperty(self, property_name):
        """Returns the value of given property."""
        return self.values[property_name]


class FIDataRecord:
    values = {}

    def SetField(self, field_name, value):
        """Stores a value in the specified field."""
        if not isinstance(value, unicode):
            raise ValueError("You should use unicode for exporting values "
                             "from Python to the schema output!")
        self.values[field_name] = value

    def GetField(self, field_name):
        """Get a field from record."""
        return self.values[field_name]


Collection = FIDataCollection()
DataManager = FIDataManager()
Properties = FIProperties()
