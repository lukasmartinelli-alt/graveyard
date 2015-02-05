import ConfigParser

print 'Loading history data...'

collectionSize = Collection.Size()
searchTermRec = DataManager.NewDataRecord()
ids_map = {}

# Get highest ID of Tweets in Table (latest Tweet of all read)
maxPostID = 0
for recNum in range(collectionSize, 0, -1):
  Collection.GetRecord(searchTermRec, recNum)
  post_id = searchTermRec.GetField(u'POST_ID_IN')
  try:
    if int(post_id) > maxPostID:
      maxPostID = int(post_id)
  except:
     pass 
  Collection.DeleteRecord(searchTermRec)

DataManager.DeleteDataRecord(searchTermRec)

print 'Loaded %d history data rows...' % collectionSize

DSRecord = DataManager.NewDataRecord(1)
DSRecord.SetField(u'POST_ID', unicode(maxPostID))
Collection.AddRecord(DSRecord)
del DSRecord