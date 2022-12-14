# This file is part of Xpra.
# Copyright (C) 2014-2021 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.


from xpra.net.digest import get_salt, choose_digest
from xpra.util import typedict


class Authenticator:
    def __init__(self, **kwargs):
        self.challenge_sent = False
        self.prompt = kwargs.pop("prompt", "password")
        self.passed = False

    def requires_challenge(self) -> bool:
        return True

    def get_challenge(self, digests):
        self.challenge_sent = True
        return get_salt(), choose_digest(digests)

    def choose_salt_digest(self, digest_modes):
        return choose_digest(digest_modes)

    def get_uid(self):
        return -1

    def get_gid(self):
        return -1

    def get_passwords(self):
        return ()

    def get_password(self):
        return None

    def authenticate(self, caps : typedict) -> bool:  #pylint: disable=unused-argument
        return False

    def get_sessions(self):
        return None

    def __repr__(self):
        return "reject"
