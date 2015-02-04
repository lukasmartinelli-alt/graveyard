import ConfigParser

print 'Loading history data...'

collectionSize = Collection.Size()
searchTermRec = DataManager.NewDataRecord()
ids_map = {}

# Get highest ID of Tweets in Table (latest Tweet of all read)
maxTweet = 0
for recNum in range(collectionSize, 0, -1):
  Collection.GetRecord(searchTermRec, recNum)
  tweet_id = searchTermRec.GetField(u'TWEET_ID_IN')
  try:
    if int(tweet_id) > maxTweet:
      maxTweet = int(tweet_id)
  except:
     pass 
  Collection.DeleteRecord(searchTermRec)

DataManager.DeleteDataRecord(searchTermRec)

print 'Loaded %d history data rows...' % collectionSize

DSRecord = DataManager.NewDataRecord(1)
DSRecord.SetField(u'TWEET_ID', unicode(maxTweet))
Collection.AddRecord(DSRecord)
del DSRecord