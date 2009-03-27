%define		orgname	kdeplasma-addons
%define		_state	stable
%define		_qtver	4.5.0

Summary:	KDE4 Plasmoids
Summary(pl.UTF-8):	Plazmoidy dla KDE4
Name:		kde4-kdeplasma-addons
Version:	4.2.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	809887da8ee9f7674761e0f46fa966a2
Patch100:	%{name}-branch.diff
Patch0:		%{name}-pastebinpld.patch
URL:		http://www.kde.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	QtCore-devel >= %{_qtver}
BuildRequires:	QtNetwork-devel >= %{_qtver}
BuildRequires:	QtOpenGL-devel >= %{_qtver}
BuildRequires:	QtScript-devel >= %{_qtver}
BuildRequires:	QtSvg-devel >= %{_qtver}
BuildRequires:	QtWebKit-devel >= %{_qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.6.2
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	phonon-devel >= 4.3.1
BuildRequires:	qt4-build >= %{_qtver}
BuildRequires:	qt4-qmake >= %{_qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	strigi-devel >= 0.6.3
BuildRequires:	xorg-lib-libXtst-devel
Obsoletes:	kde4-kdeplasmoids
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE4 plasmoids.

%description -l pl.UTF-8
Plazmoidy dla KDE4.

%package lancelot
Summary:	Lancelot Desktop Theme
Summary(pl.UTF-8):	Motyw pulpitu Lancelot
Group:		X11/Applications
Requires:	kde4-kdebase-workspace >= %{version}

%description lancelot
Lancelot Desktop Theme.

%description lancelot -l pl.UTF-8
Motyw pulpitu Lancelot.

%prep
%setup -q -n %{orgname}-%{version}
#%patch100 -p0
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" != "lib"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	lancelot	-p /sbin/ldconfig
%postun	lancelot	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/krunner_*.so
%attr(755,root,root) %{_libdir}/kde4/kcm_krunner_*.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_*.so
%attr(755,root,root) %{_libdir}/kde4/plasma_comic_*.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_*.so
%attr(755,root,root) %{_libdir}/kde4/plasma_packagestructure_comic.so
%attr(755,root,root) %ghost %{_libdir}/libplasmacomicprovidercore.so.?
%attr(755,root,root) %{_libdir}/libplasmacomicprovidercore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplasmaconverter.so.?
%attr(755,root,root) %{_libdir}/libplasmaconverter.so.*.*.*
%{_datadir}/apps/desktoptheme/Aya
%{_datadir}/apps/desktoptheme/Elegance
%{_datadir}/apps/desktoptheme/Silicon
%dir %{_datadir}/apps/desktoptheme/default/stylesheets
%{_datadir}/apps/desktoptheme/default/stylesheets/*
%dir %{_datadir}/apps/desktoptheme/default/weatherstation
%{_datadir}/apps/desktoptheme/default/weatherstation/*
%{_datadir}/apps/desktoptheme/default/widgets/*
%{_datadir}/apps/desktoptheme/heron
%{_datadir}/apps/desktoptheme/slim-glow
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/servicetypes/plasma_comicprovider.desktop
#%{_iconsdir}/hicolor/scalable/apps/fifteenpuzzle.svgz
%{_datadir}/config/comic.knsrc
%dir %{_datadir}/apps/desktoptheme/default/rssnow
%{_datadir}/apps/desktoptheme/default/rssnow/background.svgz
%{_datadir}/apps/desktoptheme/default/rssnow/left.svgz
%{_datadir}/apps/desktoptheme/default/rssnow/right.svgz
%{_datadir}/apps/desktoptheme/default/rssnow/rssnow.svgz
%dir %{_datadir}/apps/rssnow
%{_datadir}/apps/rssnow/feeds
%{_iconsdir}/*/*x*/apps/previewer.png
#%{_iconsdir}/oxygen/scalable/apps/bball.svgz
%{_datadir}/kde4/services/ServiceMenus/preview.desktop
%dir %{_datadir}/apps/bball
%{_datadir}/apps/bball/bball.svgz
%{_datadir}/apps/bball/bounce.ogg
%{_datadir}/apps/bball/football.svgz
%{_datadir}/apps/plasma-bluemarble
%{_datadir}/apps/plasma/services/tweet.operations

%files lancelot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lancelot
%attr(755,root,root) %ghost %{_libdir}/liblancelot.so.?
%attr(755,root,root) %{_libdir}/liblancelot.so.*.*.*
%{_datadir}/apps/desktoptheme/default/lancelot
%{_datadir}/dbus-1/services/org.kde.lancelot.service
%{_datadir}/mime/packages/lancelotpart-mime.xml
%{_iconsdir}/hicolor/*x*/apps/lancelot.png
%{_iconsdir}/hicolor/*x*/apps/lancelot-part.png
