%define beta %{nil}
%define scmrev %{nil}

Name: fcitx-anthy
Version: 0.1.1
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 8
Source0: http://fcitx.googlecode.com/files/%{name}-%{version}.tar.xz
%else
Release: 0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source0: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: Anthy (Japanese IM) plugin for fcitx
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
Anthy (Japanese IM) plugin for fcitx

%prep
%if "%{scmrev}" == ""
%setup -q -n %{name}-%{version}%{beta}
%else
%setup -q -n %{name}
%endif

%build
%cmake
%make

%install
%makeinstall_std -C build
%find_lang %name

%files -f %name.lang
%_libdir/fcitx/fcitx-anthy.so
%_datadir/fcitx/addon/fcitx-anthy.conf
%_datadir/fcitx/configdesc/fcitx-anthy.desc
%_datadir/fcitx/anthy
%_datadir/fcitx/imicon/anthy.png
%_datadir/fcitx/inputmethod/anthy.conf
%_datadir/icons/hicolor/*/*/*
