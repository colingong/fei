from share.config_redis import redis_rate_limit

KEY = 'ratelimit_counter'
RATE_LIMIT = 3

# redis_rate_limit.set(KEY, RATE_LIMIT)
for i in range(RATE_LIMIT):
    redis_rate_limit.lpush(KEY, 1)

