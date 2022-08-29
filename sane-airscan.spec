Name: sane-airscan
Version: 0.99.27
Release: 1
Source0: https://github.com/alexpevzner/sane-airscan/archive/%{version}/%{name}-%{version}.tar.gz
Summary: AirScan (eSCL and WSD) scanner support for SANE
URL: https://github.com/alexpevzner/sane-airscan
License: GPL
Group: Hardware
BuildRequires: meson ninja
BuildRequires: pkgconfig(avahi-client)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(sane-backends)
Recommends: ipp-usb
Supplements: sane-backends

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
