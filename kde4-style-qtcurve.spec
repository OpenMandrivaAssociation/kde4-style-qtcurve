%define shortname QtCurve
%define libname %{_lib}%{name}

Name: kde4-style-qtcurve
Summary: QtCurve Theme for KDE4
Version: 1.8.4
Release: %mkrel 1
Source0: http://craigd.wikispaces.com/file/view/%{shortname}-KDE4-%{version}.tar.bz2
URL: http://www.kde-look.org/content/show.php?content=40492
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2 
BuildRequires: kdelibs4-devel
BuildRequires: kdebase4-workspace-devel
Requires: %{_lib}%{name} = %{version}
Suggests: qtcurve-gtk2
#added for test purpose by bedi
Suggests: oxygen-gtk
Suggests: systemsettings-qt-gtk
Conflicts: kde-style-QtCurve < 0.59
Obsoletes: kde4-style-QtCurve < 0.59.3

%description
QtCurve theme for KDE 4


%package -n %{libname}
Summary: libraries for %{name}
Group: System/Libraries
Provides: lib%{name} = %{version}-%{release}
Conflicts: %{name} < 0.69.2-2

%description -n %{libname}
The libraries for %{name}.

%prep 
%setup -q -n %{shortname}-KDE4-%version

%build 
%cmake_kde4 
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build
%find_lang qtcurve

%clean 
rm -rf %{buildroot} 

%files -f qtcurve.lang
%defattr(-,root,root)
%doc README ChangeLog TODO
%{_kde_appsdir}/QtCurve
%{_kde_appsdir}/color-schemes/
%{_kde_appsdir}/kstyle/
%{_kde_appsdir}/kwin/

%files -n %{libname}
%{_kde_libdir}/kde4/kstyle_qtcurve_config.so
%{_kde_libdir}/kde4/kwin3_qtcurve.so
%{_kde_libdir}/kde4/kwin_qtcurve_config.so
%{_kde_libdir}/kde4/plugins/styles/qtcurve.so
