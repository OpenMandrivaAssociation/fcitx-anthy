Summary: Anthy (Japanese IM) plugin for fcitx
Name: fcitx-anthy
Version: 0.2.4
Release: 1
Source0: https://github.com/fcitx/fcitx-anthy/archive/refs/tags/%{version}.tar.gz
URL: http://fcitx.googlecode.com/
License: GPLv2
Group: System/Internationalization
BuildRequires: cmake
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(anthy)
BuildRequires: intltool
# https://github.com/OpenMandrivaAssociation/distribution/issues/2918
Requires: locales-extra-charsets

%description
Anthy (Japanese IM) plugin for fcitx.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %name

%files -f %name.lang
%{_libdir}/fcitx/fcitx-anthy.so
%{_datadir}/fcitx/addon/fcitx-anthy.conf
%{_datadir}/fcitx/configdesc/fcitx-anthy.desc
%{_datadir}/fcitx/anthy
%{_datadir}/fcitx/imicon/anthy.png
%{_datadir}/fcitx/inputmethod/anthy.conf
%{_datadir}/icons/hicolor/*/*/*
