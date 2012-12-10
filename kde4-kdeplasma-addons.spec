#
%bcond_without	marble	# don't build marble plasma support

%define		orgname	    kdeplasma-addons
%define		_state	    stable
%define		qtver	    4.8.1

Summary:	KDE4 Plasmoids
Summary(pl.UTF-8):	Plazmoidy dla KDE4
Name:		kde4-kdeplasma-addons
Version:	4.9.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	630c2db7f869591e80e8f5493890ef58
Patch100:	%{name}-branch.diff
Patch0:		webslice_fix_zoom_on_reload.patch
URL:		http://www.kde.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	attica-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	eigen >= 1:2.0.12-3
BuildRequires:	glibc-misc
BuildRequires:	ibus-devel
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	kde4-kdebase-workspace-kwin >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	kde4-libkexiv2-devel >= %{version}
%{?with_marble:BuildRequires:	kde4-marble-devel >= %{version}}
BuildRequires:	libdbusmenu-qt-devel
BuildRequires:	libqalculate-devel
BuildRequires:	phonon-devel >= 4.4.1
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	qoauth-devel
BuildRequires:	qca-devel >= 2.0.2
BuildRequires:	qimageblitz-devel >= 0.0.6
BuildRequires:	qjson-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	qwt-devel
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	scim-devel
BuildRequires:	shared-desktop-ontologies-devel >= 0.5
BuildRequires:	shared-mime-info
BuildRequires:	soprano-devel >= 2.4.64
BuildRequires:	strigi-devel >= 0.7.2
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
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

%package devel
Summary:	Development files for KDE4 Plasmoids
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek plazmoidów dla KDE4
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdebase-workspace-devel >= %{version}
Requires:	kde4-kdelibs-devel >= %{version}
Requires:	kde4-kdepimlibs-devel >= %{version}

%description devel
This package contains header files needed if you wish to build
applications based on KDE4 Plasmoids.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe potrzebne do budowy aplikacji
opartych na plazmoidach dla KDE4.

%prep
%setup -q -n %{orgname}-%{version}
#%patch100 -p0
%patch0 -p1

%build
install -d build
cd build
%cmake \
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
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_bball.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_binaryclock.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_blackboard.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_bookmarks.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_bubblemon.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_calculator.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_charselect.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_comic.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_dict.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_eyes.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_fifteenPuzzle.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_fileWatcher.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_frame.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_fuzzy_clock.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_incomingmsg.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_kdeobservatory.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_knowledgebase.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_kolourpicker.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_leavenote.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_life.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_luna.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_magnifique.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_mediaplayer.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_microblog.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_news.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_notes.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_opendesktop.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_opendesktop_activities.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_paste.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_pastebin.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_plasmaboard.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_previewer.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_qalculate.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_rssnow.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_rtm.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_showdashboard.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_showdesktop.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_spellcheck.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_timer.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_unitconverter.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_weather.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_weatherstation.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_webslice.so
%attr(755,root,root) %{_libdir}/kde4/plasma_comic_*.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_*.so
%attr(755,root,root) %{_libdir}/kde4/plasma_packagestructure_comic.so
%attr(755,root,root) %ghost %{_libdir}/libplasmacomicprovidercore.so.?
%attr(755,root,root) %{_libdir}/libplasmacomicprovidercore.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/plasma-applet_systemloadviewer.so
%attr(755,root,root) %{_libdir}/kde4/plasma_potd_apodprovider.so
%attr(755,root,root) %{_libdir}/kde4/plasma_potd_epodprovider.so
%attr(755,root,root) %{_libdir}/kde4/plasma_potd_flickrprovider.so
%attr(755,root,root) %{_libdir}/kde4/plasma_potd_oseiprovider.so
%attr(755,root,root) %{_libdir}/kde4/plasma_potd_wcpotdprovider.so
%attr(755,root,root) %{_libdir}/kde4/plasma_runner_datetime.so
%attr(755,root,root) %{_libdir}/kde4/plasma_wallpaper_mandelbrot.so
%attr(755,root,root) %{_libdir}/kde4/kcm_plasma_runner_events.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_icontasks.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_kimpanel.so
%attr(755,root,root) %{_libdir}/kde4/plasma_wallpaper_potd.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_griddesktop.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_groupingdesktop.so
%attr(755,root,root) %{_libdir}/kde4/plasma_containment_groupingpanel.so
%attr(755,root,root) %{_libdir}/kde4/plasma_runner_events.so
%if %{with marble}
%attr(755,root,root) %{_libdir}/kde4/plasma_wallpaper_marble.so
%endif
%attr(755,root,root) %{_libdir}/kde4/plasma_wallpaper_pattern.so
%attr(755,root,root) %{_libdir}/kde4/plasma_wallpaper_virus.so
%attr(755,root,root) %{_libdir}/kde4/plasma_wallpaper_weather.so
%attr(755,root,root) %{_libdir}/libplasmacomicprovidercore.so
%attr(755,root,root) %ghost %{_libdir}/libplasmapotdprovidercore.so.?
%attr(755,root,root) %{_libdir}/libplasmapotdprovidercore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplasmaweather.so.?
%attr(755,root,root) %{_libdir}/libplasmaweather.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librtm.so.?
%attr(755,root,root) %{_libdir}/librtm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplasma_groupingcontainment.so.?
%attr(755,root,root) %{_libdir}/libplasma_groupingcontainment.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/libexec/kimpanel-ibus-panel
%attr(755,root,root) %{_libdir}/kde4/libexec/kimpanel-scim-panel
%{_datadir}/apps/desktoptheme/Aya
%{_datadir}/apps/desktoptheme/Androbit
#%{_datadir}/apps/desktoptheme/Elegance
%{_datadir}/apps/desktoptheme/Produkt
#%{_datadir}/apps/desktoptheme/Silicon
%{_datadir}/apps/desktoptheme/Tibanna
%dir %{_datadir}/apps/desktoptheme/default/stylesheets
%{_datadir}/apps/desktoptheme/default/stylesheets/*
%dir %{_datadir}/apps/desktoptheme/default/weatherstation
%{_datadir}/apps/desktoptheme/default/weatherstation/*
%dir %{_datadir}/apps/desktoptheme/default/weather/
%{_datadir}/apps/desktoptheme/default/weather/wind-arrows.svgz
%{_datadir}/apps/desktoptheme/default/widgets/*
#%{_datadir}/apps/desktoptheme/heron
%{_datadir}/apps/desktoptheme/slim-glow
%{_datadir}/apps/kdeplasma-addons
%{_datadir}/kde4/services/CharRunner_config.desktop
%{_datadir}/kde4/services/CharacterRunner.desktop
%{_datadir}/kde4/services/apodprovider.desktop
%{_datadir}/kde4/services/browserhistory.desktop
%{_datadir}/kde4/services/epodprovider.desktop
%{_datadir}/kde4/services/flickrprovider.desktop
%{_datadir}/kde4/services/katesessions.desktop
%{_datadir}/kde4/services/konquerorsessions.desktop
%{_datadir}/kde4/services/konsolesessions.desktop
%{_datadir}/kde4/services/oseiprovider.desktop
%{_datadir}/kde4/services/plasma-applet-bball.desktop
%{_datadir}/kde4/services/plasma-applet-binaryclock.desktop
%{_datadir}/kde4/services/plasma-applet-blackboard.desktop
%{_datadir}/kde4/services/plasma-applet-bookmarks.desktop
%{_datadir}/kde4/services/plasma-applet-bubblemon.desktop
%{_datadir}/kde4/services/plasma-applet-calculator.desktop
%{_datadir}/kde4/services/plasma-applet-charselect.desktop
%{_datadir}/kde4/services/plasma-applet-eyes.desktop
%{_datadir}/kde4/services/plasma-applet-fifteenPuzzle.desktop
%{_datadir}/kde4/services/plasma-applet-incomingmsg.desktop
%{_datadir}/kde4/services/plasma-applet-kdeobservatory.desktop
%{_datadir}/kde4/services/plasma-applet-knowledgebase.desktop
%{_datadir}/kde4/services/plasma-applet-konqprofiles.desktop
%{_datadir}/kde4/services/plasma-applet-konsoleprofiles.desktop
%{_datadir}/kde4/services/plasma-applet-leavenote.desktop
%{_datadir}/kde4/services/plasma-applet-life.desktop
%{_datadir}/kde4/services/plasma-applet-luna.desktop
%{_datadir}/kde4/services/plasma-applet-magnifique.desktop
%{_datadir}/kde4/services/plasma-applet-mediaplayer.desktop
%{_datadir}/kde4/services/plasma-applet-microblog.desktop
%{_datadir}/kde4/services/plasma-applet-news.desktop
%{_datadir}/kde4/services/plasma-applet-nowplaying.desktop
%{_datadir}/kde4/services/plasma-applet-opendesktop-activities.desktop
%{_datadir}/kde4/services/plasma-applet-opendesktop.desktop
%{_datadir}/kde4/services/plasma-applet-paste.desktop
%{_datadir}/kde4/services/plasma-applet-pastebin.desktop
%{_datadir}/kde4/services/plasma-applet-previewer.desktop
#%{_datadir}/kde4/services/plasma-applet-qalculate.desktop
%{_datadir}/kde4/services/plasma-applet-rememberthemilk.desktop
%{_datadir}/kde4/services/plasma-applet-rssnow.desktop
%{_datadir}/kde4/services/plasma-applet-showdashboard.desktop
%{_datadir}/kde4/services/plasma-applet-showdesktop.desktop
%{_datadir}/kde4/services/plasma-applet-spellcheck.desktop
%{_datadir}/kde4/services/plasma-applet-systemloadviewer.desktop
%{_datadir}/kde4/services/plasma-applet-timer.desktop
%{_datadir}/kde4/services/plasma-applet-unitconverter.desktop
%{_datadir}/kde4/services/plasma-applet-weather.desktop
%{_datadir}/kde4/services/plasma-applet-weatherstation.desktop
%{_datadir}/kde4/services/plasma-applet-webslice.desktop
%{_datadir}/kde4/services/plasma-clock-fuzzy.desktop
%{_datadir}/kde4/services/plasma-comic-default.desktop
%{_datadir}/kde4/services/plasma-dataengine-comic.desktop
%{_datadir}/kde4/services/plasma-dataengine-ocs.desktop
%{_datadir}/kde4/services/plasma-dataengine-potd.desktop
%{_datadir}/kde4/services/plasma-dataengine-konqprofiles.desktop
%{_datadir}/kde4/services/plasma-dataengine-konsoleprofiles.desktop
%{_datadir}/kde4/services/plasma-dataengine-microblog.desktop
%{_datadir}/kde4/services/plasma-runner-youtube.desktop
%{_datadir}/kde4/services/plasma-dict-default.desktop
%{_datadir}/kde4/services/plasma-engine-kdeobservatory.desktop
%{_datadir}/kde4/services/plasma-engine-rtm.desktop
%{_datadir}/kde4/services/plasma-fileWatcher-default.desktop
%{_datadir}/kde4/services/plasma-frame-default.desktop
%{_datadir}/kde4/services/plasma-kolourpicker-default.desktop
%{_datadir}/kde4/services/plasma-notes-default.desktop
%{_datadir}/kde4/services/plasma-packagestructure-comic.desktop
%{_datadir}/kde4/services/plasma-runner-audioplayercontrol.desktop
%{_datadir}/kde4/services/plasma-runner-audioplayercontrol_config.desktop
%{_datadir}/kde4/services/plasma-runner-contacts.desktop
%{_datadir}/kde4/services/plasma-runner-converter.desktop
%{_datadir}/kde4/services/plasma-runner-datetime.desktop
%{_datadir}/kde4/services/plasma-runner-kopete.desktop
%{_datadir}/kde4/services/plasma-runner-spellchecker.desktop
%{_datadir}/kde4/services/plasma-runner-spellchecker_config.desktop
%{_datadir}/kde4/services/plasma-runner-techbase.desktop
%{_datadir}/kde4/services/plasma-runner-wikipedia.desktop
%{_datadir}/kde4/services/plasma-runner-wikitravel.desktop
%{_datadir}/kde4/services/plasma-wallpaper-mandelbrot.desktop
%if %{with marble}
%{_datadir}/kde4/services/plasma-wallpaper-marble.desktop
%endif
%{_datadir}/kde4/services/plasma-wallpaper-pattern.desktop
%{_datadir}/kde4/services/plasma-wallpaper-virus.desktop
%{_datadir}/kde4/services/plasma-wallpaper-weather.desktop
%{_datadir}/kde4/services/plasma_applet_plasmaboard.desktop
%{_datadir}/kde4/services/wcpotdprovider.desktop
%{_datadir}/kde4/servicetypes/plasma_comicprovider.desktop
%{_datadir}/kde4/servicetypes/plasma_potdprovider.desktop
%{_datadir}/config/comic.knsrc
%{_datadir}/config/pastebin.knsrc
%{_datadir}/config/plasmaweather.knsrc
%{_datadir}/config/virus_wallpaper.knsrc
%{_datadir}/config.kcfg/kimpanelconfig.kcfg
%{_datadir}/apps/desktoptheme/default/bubblemon
%{_datadir}/apps/desktoptheme/default/fifteenPuzzle
%{_datadir}/apps/desktoptheme/default/icontasks
%{_datadir}/apps/desktoptheme/default/rssnow
%{_iconsdir}/hicolor/scalable/actions/youtube.svgz
%{_iconsdir}/hicolor/scalable/apps/accessories-dictionary.svgz
%{_iconsdir}/hicolor/scalable/apps/bball.svgz
%{_iconsdir}/hicolor/scalable/apps/eyes.svgz
%{_iconsdir}/hicolor/scalable/apps/fifteenpuzzle.svgz
%{_iconsdir}/hicolor/scalable/apps/kdeobservatory.svgz
%{_iconsdir}/hicolor/scalable/apps/lifegame.svgz
%{_iconsdir}/hicolor/*x*/apps/qalculate-applet.png
%{_iconsdir}/hicolor/*x*/apps/plasmaapplet-shelf.png
%{_iconsdir}/hicolor/*x*/apps/eyes.png
%{_iconsdir}/hicolor/*x*/apps/kdeobservatory.png
%{_iconsdir}/hicolor/*x*/apps/lifegame.png
%{_iconsdir}/hicolor/*x*/apps/luna.png
%{_iconsdir}/hicolor/*x*/actions/youtube.png
%dir %{_datadir}/apps/rssnow
%{_datadir}/apps/rssnow/feeds
%{_iconsdir}/*/*x*/apps/previewer.png
%{_datadir}/kde4/services/ServiceMenus/preview.desktop
%dir %{_datadir}/apps/bball
%{_datadir}/apps/bball/bball.svgz
%{_iconsdir}/*/*x*/apps/bball.png
%{_datadir}/apps/bball/bounce.ogg
%{_datadir}/apps/bball/football.svgz
%{_datadir}/apps/plasma
%{_datadir}/apps/plasmaboard
%{_datadir}/apps/plasma-applet-opendesktop
%{_datadir}/apps/plasma-applet-opendesktop-activities
%{_datadir}/apps/plasma-applet-frame
%{_datadir}/apps/plasma_pastebin
%{_datadir}/apps/plasma_wallpaper_pattern
%{_datadir}/kde4/services/lancelot.desktop
%{_datadir}/kde4/services/plasma-containment-griddesktop.desktop
%{_datadir}/kde4/services/plasma-containment-groupingdesktop.desktop
%{_datadir}/kde4/services/plasma-containment-groupingpanel.desktop
%{_datadir}/kde4/services/plasma-runner-events.desktop
%{_datadir}/kde4/services/plasma-runner-events_config.desktop
%{_datadir}/kde4/services/plasma-applet-icontasks.desktop
%{_datadir}/kde4/services/plasma-applet-kimpanel.desktop
%{_datadir}/kde4/services/plasma-applet-qalculate.desktop
%{_datadir}/kde4/services/plasma-dataengine-kimpanel.desktop
%{_datadir}/kde4/services/plasma-wallpaper-potd.desktop

%files lancelot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lancelot
%attr(755,root,root) %ghost %{_libdir}/liblancelot.so.?
%attr(755,root,root) %{_libdir}/liblancelot.so.*.*.*
%attr(755,root,root) %{_libdir}/liblancelot.so
%attr(755,root,root) %{_libdir}/liblancelot-datamodels.so.?
%attr(755,root,root) %{_libdir}/liblancelot-datamodels.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_lancelot_launcher.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_lancelot_part.so
%{_datadir}/apps/desktoptheme/default/lancelot
%{_datadir}/apps/desktoptheme/oxygen/lancelot
%{_datadir}/kde4/services/plasma-applet-lancelot-launcher.desktop
%{_datadir}/kde4/services/plasma-applet-lancelot-part.desktop
#%{_datadir}/dbus-1/services/org.kde.lancelot.service
%{_datadir}/mime/packages/lancelotpart-mime.xml
%{_datadir}/apps/lancelot
%{_iconsdir}/hicolor/*x*/apps/lancelot.png
%{_iconsdir}/hicolor/*x*/apps/lancelot-start.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%exclude %{_libdir}/libplasmacomicprovidercore.so
%exclude %{_libdir}/liblancelot.so
%{_includedir}/KDE/Lancelot
%{_includedir}/lancelot-datamodels
%{_includedir}/lancelot
%{_datadir}/apps/cmake/modules/*.cmake
