%global optflags %{optflags} -Ofast

Name:		orion
Version:	1.6.7
Release:	1
Summary:	Desktop client for Twitch.
Group:		Video/Players
License:	GPLv3+
URL:		https://github.com/alamminsalo/orion
Source0:	https://github.com/alamminsalo/orion/archive/%{version}/%{name}-%{version}.tar.gz
#Patch0:   orion-1.6.6-fix-install-prefix-openmandriva.patch
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5QuickControls2)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	desktop-file-utils
BuildRequires:  qmake5
BuildRequires:  pkgconfig(gl)
#BuildRequires:  pkgconfig(mpv)
#BuildRequires:  glesv3-devel
#Requires: mpv
Requires:	hicolor-icon-theme
Requires:	qt5-qtquickcontrols

%description
Desktop client for Twitch based on QML/C++


%prep
%autosetup -p0 -n %{name}-%{version}

%build
mkdir build
cd build
# Is possible to build Orion with MPV (CONFIG+=mpv), QtAV (CONFIG+=qtav) or Qt5 Multimedia (CONFIG+=multimedia). (Penguin)
%{qmake_qt5} ../ "CONFIG+=multimedia"
%make_build

%install
cd build
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/orion
#{_datadir}/metainfo/Orion.appdata.xml
%{_datadir}/applications/Orion.desktop
%{_datadir}/icons/%{name}.svg
%license COPYING LICENSE.txt
