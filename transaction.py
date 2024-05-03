from redis import Redis

redis = Redis(host="172.17.0.2", decode_responses=True)

with redis.pipeline() as pipe:
    keys = redis.keys("test")
    pipe.watch("test")
    pipe.multi()
    for k in keys:
        pipe.hdel("test", k)
    pipe.execute()
