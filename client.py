import pusher

pusher_client = pusher.Pusher(
  app_id=u'1806190',
  key=u'b466625a5dad96340d2a',
  secret=u'36bbb1cd7506c37d7e69',
  cluster=u'eu'
)

pusher_client.trigger(u'my-channel', u'my-event', {u'message': u'Jelle'})