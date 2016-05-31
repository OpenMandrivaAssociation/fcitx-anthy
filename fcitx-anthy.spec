Summary: Anthy (Japanese IM) plugin for fcitx
Name: fcitx-anthy
Version: 0.2.2
Release: 1
Source0: http://fcitx.googlecode.com/files/%{name}-%{version}.tar.xz
URL: http://fcitx.googlecode.com/
License: GPLv2
Group: System/Internationalization
BuildRequires: cmake
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(anthy)
BuildRequires: intltool

%track
prog %{name} = {
	url = http://code.google.com/p/fcitx/downloads/list
	regex = %name-(__VER__)\.tar\.xz
	version = %{version}
}

%description
Anthy (Japanese IM) plugin for fcitx.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build
%find_lang %name

%files -f %name.lang
%{_libdir}/fcitx/fcitx-anthy.so
%{_datadir}/fcitx/addon/fcitx-anthy.conf
%{_datadir}/fcitx/configdesc/fcitx-anthy.desc
%{_datadir}/fcitx/anthy
%{_datadir}/fcitx/imicon/anthy.png
%{_datadir}/fcitx/inputmethod/anthy.conf
%{_datadir}/icons/hicolor/*/*/*
