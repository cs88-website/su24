test = {
    'name': 'Extra Credit',
    'points': 1,
    'suites': [
        {
            'type': 'doctest',
            'setup': """
            >>> from lab03 import *
            >>> import hashlib
            """,
            'cases' : [
                {
                    'code': """
                    >>> email, code = lab03_practice_problems()
                    >>> def md5_hash(s):
                    ...     return hashlib.md5(str.encode('88' + s)).hexdigest()
                    >>> def lab_key(s):
                    ...     return md5_hash('cs88/lab{}/{}'.format('03', md5_hash(s)))
                    >>> code == lab_key(email)
                    True
                    """,
                },
            ]
        },
    ]
}
