import argparse


def make_ddhresult(code):
    return (1 << 31) | (0x876 << 16) | code


ERROR_CODES = {0x800401F0: 'DDERR_NOTINITIALIZED', 0x80004005: 'DDERR_GENERIC', 0x8007000E: 'DDERR_OUTOFMEMORY',
               0x80004001: 'DDERR_UNSUPPORTED', 0x80070057: 'DDERR_INVALIDPARAMS',
               make_ddhresult(5): 'DDERR_ALREADYINITIALIZED', make_ddhresult(10): 'DDERR_CANNOTATTACHSURFACE',
               make_ddhresult(20): 'DDERR_CANNOTDETACHSURFACE', make_ddhresult(40): 'DDERR_CURRENTLYNOTAVAIL',
               make_ddhresult(55): 'DDERR_EXCEPTION', make_ddhresult(90): 'DDERR_HEIGHTALIGN',
               make_ddhresult(95): 'DDERR_INCOMPATIBLEPRIMARY', make_ddhresult(100): 'DDERR_INVALIDCAPS',
               make_ddhresult(110): 'DDERR_INVALIDCLIPLIST', make_ddhresult(120): 'DDERR_INVALIDMODE',
               make_ddhresult(130): 'DDERR_INVALIDOBJECT', make_ddhresult(145): 'DDERR_INVALIDPIXELFORMAT',
               make_ddhresult(150): 'DDERR_INVALIDRECT', make_ddhresult(160): 'DDERR_LOCKEDSURFACES',
               make_ddhresult(170): 'DDERR_NO3D', make_ddhresult(180): 'DDERR_NOALPHAHW',
               make_ddhresult(181): 'DDERR_NOSTEREOHARDWARE', make_ddhresult(182): 'DDERR_NOSURFACELEFT',
               make_ddhresult(205): 'DDERR_NOCLIPLIST', make_ddhresult(210): 'DDERR_NOCOLORCONVHW',
               make_ddhresult(212): 'DDERR_NOCOOPERATIVELEVELSET', make_ddhresult(215): 'DDERR_NOCOLORKEY',
               make_ddhresult(220): 'DDERR_NOCOLORKEYHW', make_ddhresult(222): 'DDERR_NODIRECTDRAWSUPPORT',
               make_ddhresult(225): 'DDERR_NOEXCLUSIVEMODE', make_ddhresult(230): 'DDERR_NOFLIPHW',
               make_ddhresult(240): 'DDERR_NOGDI', make_ddhresult(250): 'DDERR_NOMIRRORHW',
               make_ddhresult(255): 'DDERR_NOTFOUND', make_ddhresult(260): 'DDERR_NOOVERLAYHW',
               make_ddhresult(270): 'DDERR_OVERLAPPINGRECTS', make_ddhresult(280): 'DDERR_NORASTEROPHW',
               make_ddhresult(290): 'DDERR_NOROTATIONHW', make_ddhresult(310): 'DDERR_NOSTRETCHHW',
               make_ddhresult(316): 'DDERR_NOT4BITCOLOR', make_ddhresult(317): 'DDERR_NOT4BITCOLORINDEX',
               make_ddhresult(320): 'DDERR_NOT8BITCOLOR', make_ddhresult(330): 'DDERR_NOTEXTUREHW',
               make_ddhresult(335): 'DDERR_NOVSYNCHW', make_ddhresult(340): 'DDERR_NOZBUFFERHW',
               make_ddhresult(350): 'DDERR_NOZOVERLAYHW', make_ddhresult(360): 'DDERR_OUTOFCAPS',
               make_ddhresult(380): 'DDERR_OUTOFVIDEOMEMORY', make_ddhresult(382): 'DDERR_OVERLAYCANTCLIP',
               make_ddhresult(384): 'DDERR_OVERLAYCOLORKEYONLYONEACTIVE', make_ddhresult(387): 'DDERR_PALETTEBUSY',
               make_ddhresult(400): 'DDERR_COLORKEYNOTSET', make_ddhresult(410): 'DDERR_SURFACEALREADYATTACHED',
               make_ddhresult(420): 'DDERR_SURFACEALREADYDEPENDENT', make_ddhresult(430): 'DDERR_SURFACEBUSY',
               make_ddhresult(435): 'DDERR_CANTLOCKSURFACE', make_ddhresult(440): 'DDERR_SURFACEISOBSCURED',
               make_ddhresult(450): 'DDERR_SURFACELOST', make_ddhresult(460): 'DDERR_SURFACENOTATTACHED',
               make_ddhresult(470): 'DDERR_TOOBIGHEIGHT', make_ddhresult(480): 'DDERR_TOOBIGSIZE',
               make_ddhresult(490): 'DDERR_TOOBIGWIDTH', make_ddhresult(510): 'DDERR_UNSUPPORTEDFORMAT',
               make_ddhresult(520): 'DDERR_UNSUPPORTEDMASK', make_ddhresult(521): 'DDERR_INVALIDSTREAM',
               make_ddhresult(537): 'DDERR_VERTICALBLANKINPROGRESS', make_ddhresult(540): 'DDERR_WASSTILLDRAWING',
               make_ddhresult(542): 'DDERR_DDSCAPSCOMPLEXREQUIRED', make_ddhresult(560): 'DDERR_XALIGN',
               make_ddhresult(561): 'DDERR_INVALIDDIRECTDRAWGUID',
               make_ddhresult(562): 'DDERR_DIRECTDRAWALREADYCREATED', make_ddhresult(563): 'DDERR_NODIRECTDRAWHW',
               make_ddhresult(564): 'DDERR_PRIMARYSURFACEALREADYEXISTS', make_ddhresult(565): 'DDERR_NOEMULATION',
               make_ddhresult(566): 'DDERR_REGIONTOOSMALL', make_ddhresult(567): 'DDERR_CLIPPERISUSINGHWND',
               make_ddhresult(568): 'DDERR_NOCLIPPERATTACHED', make_ddhresult(569): 'DDERR_NOHWND',
               make_ddhresult(570): 'DDERR_HWNDSUBCLASSED', make_ddhresult(571): 'DDERR_HWNDALREADYSET',
               make_ddhresult(572): 'DDERR_NOPALETTEATTACHED', make_ddhresult(573): 'DDERR_NOPALETTEHW',
               make_ddhresult(574): 'DDERR_BLTFASTCANTCLIP', make_ddhresult(575): 'DDERR_NOBLTHW',
               make_ddhresult(576): 'DDERR_NODDROPSHW', make_ddhresult(577): 'DDERR_OVERLAYNOTVISIBLE',
               make_ddhresult(578): 'DDERR_NOOVERLAYDEST', make_ddhresult(579): 'DDERR_INVALIDPOSITION',
               make_ddhresult(580): 'DDERR_NOTAOVERLAYSURFACE', make_ddhresult(581): 'DDERR_EXCLUSIVEMODEALREADYSET',
               make_ddhresult(582): 'DDERR_NOTFLIPPABLE', make_ddhresult(583): 'DDERR_CANTDUPLICATE',
               make_ddhresult(584): 'DDERR_NOTLOCKED', make_ddhresult(585): 'DDERR_CANTCREATEDC',
               make_ddhresult(586): 'DDERR_NODC', make_ddhresult(587): 'DDERR_WRONGMODE',
               make_ddhresult(588): 'DDERR_IMPLICITLYCREATED', make_ddhresult(589): 'DDERR_NOTPALETTIZED',
               make_ddhresult(590): 'DDERR_UNSUPPORTEDMODE', make_ddhresult(591): 'DDERR_NOMIPMAPHW',
               make_ddhresult(592): 'DDERR_INVALIDSURFACETYPE', make_ddhresult(600): 'DDERR_NOOPTIMIZEHW',
               make_ddhresult(601): 'DDERR_NOTLOADED', make_ddhresult(602): 'DDERR_NOFOCUSWINDOW',
               make_ddhresult(603): 'DDERR_NOTONMIPMAPSUBLEVEL', make_ddhresult(620): 'DDERR_DCALREADYCREATED',
               make_ddhresult(630): 'DDERR_NONONLOCALVIDMEM', make_ddhresult(640): 'DDERR_CANTPAGELOCK',
               make_ddhresult(660): 'DDERR_CANTPAGEUNLOCK', make_ddhresult(680): 'DDERR_NOTPAGELOCKED',
               make_ddhresult(690): 'DDERR_MOREDATA', make_ddhresult(691): 'DDERR_EXPIRED',
               make_ddhresult(692): 'DDERR_TESTFINISHED', make_ddhresult(693): 'DDERR_NEWMODE',
               make_ddhresult(694): 'DDERR_D3DNOTINITIALIZED', make_ddhresult(695): 'DDERR_VIDEONOTACTIVE',
               make_ddhresult(696): 'DDERR_NOMONITORINFORMATION', make_ddhresult(697): 'DDERR_NODRIVERSUPPORT',
               make_ddhresult(699): 'DDERR_DEVICEDOESNTOWNSURFACE', }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("error_code", help="DirectDraw error code (hex or decimal)")
    args = parser.parse_args()

    error_code = int(args.error_code, 0)
    if error_code in ERROR_CODES:
        print "%s = 0x%x (%d)" % (ERROR_CODES[error_code], error_code, error_code)
    else:
        print "Error code not found"


if '__main__' == __name__:
    main()
