%define shortname QtCurve
%define libname %{_lib}%{name}

Name:		kde4-style-qtcurve
Summary:	QtCurve Theme for KDE4
Version:	1.8.14
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://www.kde-look.org/content/show.php?content=40492
Source0:	http://craigd.wikispaces.com/file/view/%{shortname}-KDE4-%{version}.tar.bz2
Patch0:		QtCurve-KDE4-1.8.11-l10n-ru.patch

BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
Requires:	%{_lib}%{name} = %{version}
Suggests:	qtcurve-gtk2
#added for test purpose by bedi
Suggests:	oxygen-gtk
Suggests:	systemsettings-qt-gtk

%description
QtCurve theme for KDE 4.

%package -n %{libname}
Summary:	libraries for %{name}
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
The libraries for %{name}.

%prep
%setup -qn %{shortname}-KDE4-%{version}
%autopatch -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang qtcurve

%files -f qtcurve.lang
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

