from __future__ import annotations

import abc
import collections
import threading


class SingletonMeta(abc.ABCMeta):
    _instances = {}
    _locks = collections.defaultdict(threading.Lock)

    def _get_instance_id(cls, args, kwargs):
        return cls

    def __call__(cls, *args, **kwargs):
        with cls._locks[cls]:
            instance_id = cls._get_instance_id(args, kwargs)
            if instance_id not in cls._instances:
                cls._instances[instance_id] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls._instances[instance_id]


class ThreadLocalSingletonMeta(SingletonMeta):
    def _get_instance_id(cls, args, kwargs):
        return cls, threading.current_thread()
