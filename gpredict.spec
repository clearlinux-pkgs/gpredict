#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gpredict
Version  : 2.2.1
Release  : 10
URL      : https://github.com/csete/gpredict/releases/download/v2.2.1/gpredict-2.2.1.tar.bz2
Source0  : https://github.com/csete/gpredict/releases/download/v2.2.1/gpredict-2.2.1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gpredict-bin = %{version}-%{release}
Requires: gpredict-data = %{version}-%{release}
Requires: gpredict-license = %{version}-%{release}
Requires: gpredict-locales = %{version}-%{release}
Requires: gpredict-man = %{version}-%{release}
BuildRequires : curl-dev
BuildRequires : gettext
BuildRequires : glib-dev
BuildRequires : goocanvas-dev
BuildRequires : gtk3-dev
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : perl(XML::Parser)
Patch1: 0001-Add-typdef-to-qth_data_type.patch

%description
Gpredict is a real time satellite tracking and orbit prediction program
for the Linux desktop. It uses the SGP4/SDP4 propagation algorithms together
with NORAD two-line element sets (TLE).

%package bin
Summary: bin components for the gpredict package.
Group: Binaries
Requires: gpredict-data = %{version}-%{release}
Requires: gpredict-license = %{version}-%{release}

%description bin
bin components for the gpredict package.


%package data
Summary: data components for the gpredict package.
Group: Data

%description data
data components for the gpredict package.


%package license
Summary: license components for the gpredict package.
Group: Default

%description license
license components for the gpredict package.


%package locales
Summary: locales components for the gpredict package.
Group: Default

%description locales
locales components for the gpredict package.


%package man
Summary: man components for the gpredict package.
Group: Default

%description man
man components for the gpredict package.


%prep
%setup -q -n gpredict-2.2.1
cd %{_builddir}/gpredict-2.2.1
%patch1 -p1
pushd ..
cp -a gpredict-2.2.1 buildavx2
popd
pushd ..
cp -a gpredict-2.2.1 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603685629
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export FFLAGS="$FFLAGS -m64 -march=haswell"
export FCFLAGS="$FCFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=skylake-avx512 -mprefer-vector-width=512"
export CXXFLAGS="$CXXFLAGS -m64 -march=skylake-avx512 -mprefer-vector-width=512"
export FFLAGS="$FFLAGS -m64 -march=skylake-avx512 -mprefer-vector-width=512"
export FCFLAGS="$FCFLAGS -m64 -march=skylake-avx512 -mprefer-vector-width=512"
export LDFLAGS="$LDFLAGS -m64 -march=skylake-avx512"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :
cd ../buildavx512;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1603685629
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gpredict
cp %{_builddir}/gpredict-2.2.1/COPYING %{buildroot}/usr/share/package-licenses/gpredict/9a13113b89f7985efe22a28b8e4ad1ace7f2b5d1
pushd ../buildavx512/
%make_install_avx512
popd
pushd ../buildavx2/
%make_install_avx2
popd
%make_install
%find_lang gpredict

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gpredict
/usr/bin/haswell/avx512_1/gpredict
/usr/bin/haswell/gpredict

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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gpredict/9a13113b89f7985efe22a28b8e4ad1ace7f2b5d1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gpredict.1

%files locales -f gpredict.lang
%defattr(-,root,root,-)

