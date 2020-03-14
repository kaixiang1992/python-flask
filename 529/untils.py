from flask import g


def log_a():
    print('log a value is %s' % g.username)


def log_b():
    print('log b value is %s' % g.username)


def log_c():
    print('log c value is %s' % g.username)
