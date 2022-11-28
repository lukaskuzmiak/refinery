#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .. import TestUnitBase
from . import KADATH1, KADATH2


class TEstLZG(TestUnitBase):

    def test_text_01(self):
        data = bytes.fromhex(
            '4C5A47000003E70000033F75F40FA3010102030454687265652074696D65732052616E646F6C70682043617274657220647265616D6564206F662074'
            '6865206D617276656C6C6F757320636974792C2003270311020838776173200320736E61746368033061776179207768696C030C74696C6C03557061'
            '757303136F6E02034B6869676820746572726163652061626F76652069742E20410324676F6C64656E02035C6C03106C79031220626C617A03366903'
            'F673756E7365742C20776974682077616C6C732C2074656D706C650301636F6C6F6E6E61640344037D617202038C627269646765730202CC7665696E'
            '030A6D6172626C652C2073696C7665722D626173038F666F756E7461696E03A3707269736D6174696320737072617902027962726F61642073717561'
            '72657302035A706572667502222867617264656E0205707769640202F772656574730202646368696E67206265747765656E2064656C696361746520'
            '035903FF626C6F73736F6D2D6C61033D2075726E03CF69766F72792073746174750321696E20676C65616D020244726F77733B0225606F6E031B6565'
            '70206E6F7274687761726420736C6F70032A636C696D62656420746965720203CC720305726F6F660204576F6C0202B9616B0203B7626C0329686172'
            '626F757202025A6C6974746C65206C616E02243267726173737920636F6203622E2049740223F461206665766572024628676F64733B034D616E6661'
            '7265034F73757065726E616C207472756D7002220A02239320636C6173680319696D6D6F7274031863796D62616C732E204D7973746572792068756E'
            '6702421A7574024200610202C86F75640338038B02025D6275024393756E76697369740222D10225BA3B02045D730246CF73746F6F02420165617468'
            '6C657302047C657870656374616E7402449361742062616C75737472616465642070617261706574031165726520737765707420757020746F206869'
            '6D034E20706F69676E616E637902034673757370656E730203EC616C6D6F73742D76616E697302427A6D656D6F72792C03EE61696E035C6C031A0309'
            '696E6702452E0264686464656E030C206E650330746F20706C02632067036E7702029C6F6E0308686164032C20617765736F6D031703376D03016E74'
            '02220703AB2E00'
        )
        self.assertEqual(data | self.load() | str, KADATH1)

    def test_text_02(self):
        data = bytes.fromhex(
            '4C5A470000033E000002CDF295EDAF01010203044865206B6E6577207468617420666F722068696D20697473206D65616E696E67206D757374206F6E'
            '63652068617665206265656E2073757072656D653B032E6F75676820696E207703786379636C6520033D696E6361726E6174696F6E2068037264206B'
            '6E6F776E2069742C0358776865746865036020647265616D03EC2077616B696E672C036B636F756C64206E6F742074656C6C2E2056616775656C7903'
            '392063616C6C656420757020676C696D70736573206F662061206661722C0202BB676F7474656E20666972737420796F7574682C0202696E20776F6E'
            '64657220616E6420706C656173757265206C6179020272616C6C20746865206D797374657279020249646179732C03A5646177031A034175736B0323'
            '696B65207374726F646502026774682070726F7068657469636B20746F020340656167657220736F75032E6F66206C7574657303BB736F6E673B2075'
            '6E636C6F73022257666102026767610358746F776172642066757202231503A7757270726903A26D617276656C732E204275742065616368206E6967'
            '687420617302222873746F6F64206F6E0224C16803120369626C6520746572726163652077697468020394637572696F75732075726E02048C630202'
            '526E207261696C03886C6F6F6B650202B066206F76657202054B757368030D73756E7365742063697402231D626561750302036E756E656172746802'
            '229C6D6D616E656E63650223C266656C74020370626F6E64616765036F0223ED277320747972616E6E020285676F64733B024379696E206E6F207769'
            '730226FD03336C650242740203806C6F6674792073706F02444264657363656E64020359776964650202EE6D6F7265616C20666C0222187304E1756E'
            '6720031D6C6573736C792064024281746F02420C7202024D6F730223C7656503246F6620656C02421D776974630318790243196F7574737072656164'
            '0203E16265636B6F0262142E00'
        )
        self.assertEqual(data | self.load() | str, KADATH2)

    def test_text_03(self):
        data = bytes.fromhex(
            '4C5A4700002712000000A6B05F0BA801000102034646031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F'
            '031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F'
            '031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F031F030C'
            '5555'
        )
        goal = B'F' * 10_000 + B'UU'
        self.assertEqual(data | self.load() | bytes, goal)

    def test_real_world_example_01(self):
        data = self.download_sample('84bde29f4828a71d189e473ac2e5ead9fc5f5416db73fb22135b04e67c33b1bb')
        out = data | self.ldu('vsnip', slice(0x01008040)) | self.load() | bytearray
        self.assertIn(b'WNetCancelConnection2W', out)
        self.assertIn(b'SetFilePointerEx', out)
        self.assertIn(b'WaitForMultipleObjects', out)
        self.assertIn(b'FindNextFileW', out)
        self.assertIn(b'NtQueryVirtualMemory', out)
