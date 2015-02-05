from sap import Collection, DataManager


if __name__ == '__main__':
    DSRecord = DataManager.NewDataRecord(1)
    DSRecord.SetField(u'POST_ID_IN', unicode('0'))
    Collection.AddRecord(DSRecord)
    # import triggers program automatically
    import fb_page
