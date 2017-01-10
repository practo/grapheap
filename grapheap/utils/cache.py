import pylibmc
import string
import random
import ConfigParser
from os.path import expanduser

# Get cache configuration from ~/grapheap_configs/cache.conf
Config = ConfigParser.ConfigParser()
Config.read(expanduser("~")+'/grapheap_configs/cache.conf')
cache_server = Config.get("Memcache", "cache_server")

"""
Cache class

"""
class Cache:

	# Global memcache client for this class
	cache = pylibmc.Client(
		[cache_server],
		binary=True,
		behaviors={"tcp_nodelay": True, "ketama": True})


	@staticmethod
	def get_random_key(size=6, chars=string.ascii_uppercase + string.digits):
		"""
		Get random key

		:param size: int
		:param chars: string

		:return string
		"""

		return ''.join(random.choice(chars) for _ in range(size))


	@staticmethod
	def set(key, value, ttl=None):
		"""
		Set key-value pair in cache

		:param key: string
		:param value: any data type
		:param ttl: int

		:return string
		"""

		if ttl is None:
			Cache.cache.set(key, value)

		elif ttl > 0:
			Cache.cache.set(key, value, ttl)

		return key


	@staticmethod
	def get(key, silent=False):
		"""
		Get value by key from cache

		:param key: string
		:param silent: bool

		:return any data type
		"""

		try:
			value = Cache.cache[key]

		except Exception:
			if silent:
				return None
			raise Exception("Cache Exception: " + key + " is not found")

		return value


	@staticmethod
	def remove(key):
		"""
		Remove key-value pair from cache

		:param key: string
		"""

		try:
			Cache.get(key)
			del Cache.cache[key]

		except Exception:
			pass

