Name:		sane-airscan
Version:	0.99.29
Release:	1
Source0:	https://github.com/alexpevzner/sane-airscan/archive/%{version}/%{name}-%{version}.tar.gz
# Patches from upstream git
Patch0:		0001-Added-Brother-DCP-J552DW.patch
Patch1:		0002-Update-README.md.patch
Patch2:		0003-Added-Brother-MFC-7360N.patch
Patch3:		0004-Adds-Canon-MF645Cx.patch
Patch4:		0005-Add-Brother-HL-L2380DW-series.patch
Patch5:		0006-Added-EPSON-ET-2710-Series-fixes-233.patch
Patch6:		0007-Added-EPSON-XP-5100-Series-fixes-232.patch
Patch7:		0008-Added-HP-Neverstop-Laser-MFP-1202nw-fixes-230.patch
Patch8:		0009-Added-EPSON-ET-4850-Series-fixes-229.patch
Patch9:		0010-Added-EPSON-ET-2850-Series-fixes-224.patch
Patch10:	0011-Added-Brother-MFC-8710DW-fixes-220.patch
Patch11:	0012-Added-HP-ENVY-5055-series-fixes-213.patch
Patch12:	0013-Added-Brother-MFC-J4410DW-fixes-208.patch
Patch13:	0014-Added-Xerox-C235-fixes-200.patch
Patch14:	0015-Added-EPSON-ET-2810-Series-fixes-190.patch
Patch15:	0016-Added-Canon-G600-series-fixes-189.patch
Patch16:	0017-Added-EPSON-ET-M2170-Series-fixes-188.patch
Patch17:	0018-Added-Lexmark-MC3326adwe-fixes-187.patch
Patch18:	0019-Added-Samsung-SCX-3400-Series.patch
Patch19:	0020-sane-airscan.5-updated-see-216.patch
Patch20:	0021-Man-pages-updated-see-216.patch
Patch21:	0022-Ignore-HTTP-I-O-error-if-headers-received-and-body-i.patch
Patch22:	0023-Added-Canon-TS-3400-fixes-202.patch
Patch23:	0024-Added-Kyocera-ECOSYS-M2035dn-fixes-234.patch
Patch24:	0025-Fixed-Kyocera-ECOSYS-M2035dn-description-see-234.patch
Patch25:	0026-Add-Canon-TS8230.patch
Patch26:	0027-Update-README.md.patch
Patch27:	0028-Added-Brother-MFC-J4620DW.patch
Patch28:	0029-Added-SHARP-MX-3060N.patch
Patch29:	0030-HP-Neverstop-Laser-MFP-1202nw-information-updated-fi.patch
Patch30:	0031-Added-Canon-TR8600-Scanner.patch
Patch31:	0032-Added-Brother-MFC-J1012DW.patch
Patch32:	0033-Added-THE-NEED-FOR-HELP-FROM-COMMUNITY-statement.patch
Patch33:	0034-Fixed-e-mail-addresses.patch
Patch34:	0035-Added-HP-LaserJet-Pro-M329-and-footnote-for-M329-M42.patch
Patch35:	0036-Removed-the-need-for-help-problem-solved.patch
Summary:	AirScan (eSCL and WSD) scanner support for SANE
URL:		https://github.com/alexpevzner/sane-airscan
License:	GPL
Group:		Hardware
BuildRequires:	meson ninja
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sane-backends)
Recommends:	ipp-usb
Supplements:	sane-backends

%description
Similar to how most modern network printers support "driverless" printing,
using the universal vendor-neutral printing protocol, many modern network
scanners and MFPs support "driverless" scanning.

Driverless scanning comes in two flavors:

Apple AirScan or AirPrint scanning (official protocol name is eSCL)
Microsoft WSD, or WS-Scan (term WSD means "Web Services for Devices)
This backend implements both protocols, choosing automatically between
them. It was successfully tested with many devices from Brother, Canon, Dell,
Kyocera, Lexmark, Epson, HP, OKI, Panasonic, Pantum, Ricoh, Samsung and Xerox
both in WSD and eSCL modes.

%prep
%autosetup -p1
%meson

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/airscan-discover
%{_libdir}/sane/libsane-airscan.so.1
%{_sysconfdir}/sane.d/airscan.conf
%{_sysconfdir}/sane.d/dll.d/airscan
%{_libdir}/sane/libsane-airscan.so
%{_mandir}/man1/airscan-discover.1*
%{_mandir}/man5/sane-airscan.5*
