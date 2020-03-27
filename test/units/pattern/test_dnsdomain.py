#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .. import TestUnitBase


class TestDNSDomainCarver(TestUnitBase):

    def test_url_defang(self):
        unit = self.load()
        data = bytes.fromhex(
            '4A0100000100000000000009616D6F6E676F6C696103636F6D0000010001708FC05D73110A'
            '0059000000590000000A00273BD1A5AC1F6B0DDB8408004500004B7BAB0000791104D30808'
            '0808C0A8F06B0035C18D00375F39A64A8180000100010000000009616D6F6E676F6C696103'
            '636F6D0000010001C00C000100010000003B0004B97642FE708FC05D64610A004200000042'
            '00000000005E0001010A00273BD1A50800450000340164400080064BD7C0A8F06BB97642FE'
        )
        self.assertIn(B'amongolia', unit(data))
