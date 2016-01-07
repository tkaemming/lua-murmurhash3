MurmurHash3 in Lua
==================

This repository contains an implementation of the [MurmurHash3 hashing
algorithm](https://en.wikipedia.org/wiki/MurmurHash) in Lua, intended to work
with a minimal set of commonly available dependencies.

Specifically, this is intended to work with the dependencies available to the
[Redis Lua interpreter](http://redis.io/commands/EVAL) to enable writing
scripts that require access to a hashing function with a good distribution that
can also be represented as an 32-bit integer (since Lua 5.1's number type is a
double floating point number with a maximum precise integer representation of 2
^ 53 - 1) such as many algorithms applied to probabilistic data structures.

Dependencies
------------

* [LuaBitOp](https://luarocks.org/modules/luarocks/luabitop)
* [struct](https://luarocks.org/modules/luarocks/struct)

Testing
-------

A test script is available (`test.py`) that reads lines from `/dev/stdin` and
compares the hash values of the Lua implementation with those returned by a
Python reference version, [`mmh3`](https://pypi.python.org/pypi/mmh3/2.0).
