import pusher

pusher_client = pusher.Pusher(
  app_id=u'APP_ID',
  key=u'APP_KEY',
  secret=u'SECRET_KEY',
  cluster=u'CLUSTER'
)

pusher_client.trigger(u'my-channel', u'my-event', {u'message': u'Test message'})
