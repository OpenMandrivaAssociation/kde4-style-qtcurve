%define shortname QtCurve

Name: kde4-style-%{shortname} 
Summary: QtCurve Theme for KDE4
Version: 0.59.2
Release: %mkrel 1
Source0: %{shortname}-KDE4-%{version}.tar.bz2
URL: http://www.kde-look.org
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL 
BuildRequires: kdelibs4-devel
BuildRequires: kdebase4-workspace-devel
Conflicts: kde-style-QtCurve < 0.59

%description
QtCurve theme for KDE 4

%prep 
%setup -q -n %shortname-KDE4-%version

%build 
%cmake_kde4 
%make

%install
rm -rf $RPM_BUILD_ROOT
pushd build
%makeinstall_std
popd

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%{_kde_libdir}/kde4/kstyle_qtcurve_config.so
%{_kde_libdir}/kde4/kwin3_qtcurve.so
%{_kde_libdir}/kde4/kwin_qtcurve_config.so
%{_kde_libdir}/kde4/plugins/styles/qtcurve.so
%{_kde_appsdir}/QtCurve
%{_kde_appsdir}/color-schemes/
%{_kde_appsdir}/kstyle/
%{_kde_appsdir}/kwin/


