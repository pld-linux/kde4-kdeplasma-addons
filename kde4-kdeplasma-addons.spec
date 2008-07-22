%define		orgname	kdeplasma-addons
%define		_state	unstable
%define		_qtver	4.4.0

Summary:	KDE4 Plasmoids
Summary(pl.UTF-8):	Plazmoidy dla KDE4
Name:		kde4-kdeplasma-addons
Version:	4.0.98
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	26f22c591af158c4f4d716f0be904089
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	QtCore-devel >= %{_qtver}
BuildRequires:	QtOpenGL-devel >= %{_qtver}
BuildRequires:	automoc4 >= 0.9.83
BuildRequires:	cmake
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	phonon-devel >= 4.1.83
BuildRequires:	qt4-build >= %{_qtver}
BuildRequires:	qt4-qmake >= %{_qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
Obsoletes:	kde4-kdeplasmoids
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE4 plasmoids.

%description -l pl.UTF-8
Plazmoidy dla KDE4.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
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

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/krunner_*.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_*.so
%attr(755,root,root) %{_libdir}/kde4/plasma_comic_*.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_*.so
%attr(755,root,root) %ghost %{_libdir}/libplasmaappletdialog.so.?
%attr(755,root,root) %{_libdir}/libplasmaappletdialog.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplasmacomicprovidercore.so.?
%attr(755,root,root) %{_libdir}/libplasmacomicprovidercore.so.*.*.*
%{_datadir}/apps/desktoptheme/Aya
%{_datadir}/apps/desktoptheme/Elegance
%{_datadir}/apps/desktoptheme/Silicon
%{_datadir}/apps/desktoptheme/default/widgets/*
%{_datadir}/apps/desktoptheme/heron
%{_datadir}/apps/desktoptheme/slim-glow
%{_datadir}/apps/plasma-bluemarble
%{_datadir}/apps/plasma-comic
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/servicetypes/plasma_comicprovider.desktop
%{_iconsdir}/hicolor/scalable/apps/fifteenpuzzle.svgz
