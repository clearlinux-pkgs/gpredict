#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gpredict
Version  : 2.0
Release  : 3
URL      : https://github.com/csete/gpredict/releases/download/v2.0/gpredict-2.0.tar.bz2
Source0  : https://github.com/csete/gpredict/releases/download/v2.0/gpredict-2.0.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gpredict-bin
Requires: gpredict-data
Requires: gpredict-locales
Requires: gpredict-doc
BuildRequires : curl-dev
BuildRequires : gettext
BuildRequires : glib-dev
BuildRequires : goocanvas-dev
BuildRequires : gtk3-dev
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : perl(XML::Parser)

%description
Gpredict is a real time satellite tracking and orbit prediction program
for the Linux desktop. It uses the SGP4/SDP4 propagation algorithms together
with NORAD two-line element sets (TLE).

%package bin
Summary: bin components for the gpredict package.
Group: Binaries
Requires: gpredict-data

%description bin
bin components for the gpredict package.


%package data
Summary: data components for the gpredict package.
Group: Data

%description data
data components for the gpredict package.


%package doc
Summary: doc components for the gpredict package.
Group: Documentation

%description doc
doc components for the gpredict package.


%package locales
Summary: locales components for the gpredict package.
Group: Default

%description locales
locales components for the gpredict package.


%prep
%setup -q -n gpredict-2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513002932
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1513002932
rm -rf %{buildroot}
%make_install
%find_lang gpredict

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gpredict

%files data
%defattr(-,root,root,-)
/usr/share/applications/gpredict.desktop
/usr/share/gpredict/AUTHORS
/usr/share/gpredict/COPYING
/usr/share/gpredict/NEWS
/usr/share/gpredict/README
/usr/share/gpredict/data/Amateur.mod
/usr/share/gpredict/data/locations.dat
/usr/share/gpredict/data/sample.qth
/usr/share/gpredict/data/satdata/amateur.cat
/usr/share/gpredict/data/satdata/cubesat.cat
/usr/share/gpredict/data/satdata/galileo.cat
/usr/share/gpredict/data/satdata/glo-ops.cat
/usr/share/gpredict/data/satdata/gps-ops.cat
/usr/share/gpredict/data/satdata/iridium-NEXT.cat
/usr/share/gpredict/data/satdata/iridium.cat
/usr/share/gpredict/data/satdata/molniya.cat
/usr/share/gpredict/data/satdata/noaa.cat
/usr/share/gpredict/data/satdata/satellites.dat
/usr/share/gpredict/data/satdata/science.cat
/usr/share/gpredict/data/satdata/visual.cat
/usr/share/gpredict/data/satdata/weather.cat
/usr/share/pixmaps/gpredict-icon.png
/usr/share/pixmaps/gpredict/icons/gpredict-antenna-small.png
/usr/share/pixmaps/gpredict/icons/gpredict-antenna.png
/usr/share/pixmaps/gpredict/icons/gpredict-azel-small.png
/usr/share/pixmaps/gpredict/icons/gpredict-calendar.png
/usr/share/pixmaps/gpredict/icons/gpredict-clock-small.png
/usr/share/pixmaps/gpredict/icons/gpredict-clock.png
/usr/share/pixmaps/gpredict/icons/gpredict-crash.png
/usr/share/pixmaps/gpredict/icons/gpredict-icon.png
/usr/share/pixmaps/gpredict/icons/gpredict-layout-00.png
/usr/share/pixmaps/gpredict/icons/gpredict-layout-01.png
/usr/share/pixmaps/gpredict/icons/gpredict-layout-02.png
/usr/share/pixmaps/gpredict/icons/gpredict-layout-03.png
/usr/share/pixmaps/gpredict/icons/gpredict-layout-04.png
/usr/share/pixmaps/gpredict/icons/gpredict-layout-05.png
/usr/share/pixmaps/gpredict/icons/gpredict-layout-06.png
/usr/share/pixmaps/gpredict/icons/gpredict-layout-07.png
/usr/share/pixmaps/gpredict/icons/gpredict-layout-08.png
/usr/share/pixmaps/gpredict/icons/gpredict-layout-99.png
/usr/share/pixmaps/gpredict/icons/gpredict-leds.png
/usr/share/pixmaps/gpredict/icons/gpredict-mod-attach.png
/usr/share/pixmaps/gpredict/icons/gpredict-mod-close.png
/usr/share/pixmaps/gpredict/icons/gpredict-mod-config.png
/usr/share/pixmaps/gpredict/icons/gpredict-mod-detach.png
/usr/share/pixmaps/gpredict/icons/gpredict-mod-popup.png
/usr/share/pixmaps/gpredict/icons/gpredict-notebook.png
/usr/share/pixmaps/gpredict/icons/gpredict-oscilloscope-small.png
/usr/share/pixmaps/gpredict/icons/gpredict-oscilloscope.png
/usr/share/pixmaps/gpredict/icons/gpredict-planner-small.png
/usr/share/pixmaps/gpredict/icons/gpredict-planner.png
/usr/share/pixmaps/gpredict/icons/gpredict-polar-small.png
/usr/share/pixmaps/gpredict/icons/gpredict-sat-list.png
/usr/share/pixmaps/gpredict/icons/gpredict-sat-pref.png
/usr/share/pixmaps/gpredict/icons/gpredict-shuttle-small.png
/usr/share/pixmaps/gpredict/icons/gpredict-shuttle.png
/usr/share/pixmaps/gpredict/logos/gpredict_horizontal_color.png
/usr/share/pixmaps/gpredict/logos/gpredict_horizontal_color.svg
/usr/share/pixmaps/gpredict/logos/gpredict_horizontal_white.png
/usr/share/pixmaps/gpredict/logos/gpredict_horizontal_white.svg
/usr/share/pixmaps/gpredict/logos/gpredict_icon_color.png
/usr/share/pixmaps/gpredict/logos/gpredict_icon_color.svg
/usr/share/pixmaps/gpredict/logos/gpredict_icon_white.png
/usr/share/pixmaps/gpredict/logos/gpredict_icon_white.svg
/usr/share/pixmaps/gpredict/logos/gpredict_vertical_color.png
/usr/share/pixmaps/gpredict/logos/gpredict_vertical_color.svg
/usr/share/pixmaps/gpredict/logos/gpredict_vertical_white.png
/usr/share/pixmaps/gpredict/logos/gpredict_vertical_white.svg
/usr/share/pixmaps/gpredict/maps/earth_800.png
/usr/share/pixmaps/gpredict/maps/nasa-bmng-01_1024.jpg
/usr/share/pixmaps/gpredict/maps/nasa-bmng-01_2048.jpg
/usr/share/pixmaps/gpredict/maps/nasa-bmng-03_1024.jpg
/usr/share/pixmaps/gpredict/maps/nasa-bmng-03_2048.jpg
/usr/share/pixmaps/gpredict/maps/nasa-bmng-05_1024.jpg
/usr/share/pixmaps/gpredict/maps/nasa-bmng-05_2048.jpg
/usr/share/pixmaps/gpredict/maps/nasa-bmng-07_1024.jpg
/usr/share/pixmaps/gpredict/maps/nasa-bmng-07_2048.jpg
/usr/share/pixmaps/gpredict/maps/nasa-bmng-08_1024.jpg
/usr/share/pixmaps/gpredict/maps/nasa-bmng-08_2048.jpg
/usr/share/pixmaps/gpredict/maps/nasa-topo_1024.jpg
/usr/share/pixmaps/gpredict/maps/nasa-topo_1600.jpg
/usr/share/pixmaps/gpredict/maps/nasa-topo_2048.jpg
/usr/share/pixmaps/gpredict/maps/nasa-topo_800.png

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files locales -f gpredict.lang
%defattr(-,root,root,-)

