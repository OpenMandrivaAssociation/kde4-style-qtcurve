%define shortname QtCurve
%define libname %{_lib}%{name}

Name:		kde4-style-qtcurve
Summary:	QtCurve Theme for KDE4
Version:	1.8.14
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde-look.org/content/show.php?content=40492
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
%setup -q -n %{shortname}-KDE4-%{version}
%patch0 -p 1

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


%changelog
* Mon Apr 11 2011 Funda Wang <fwang@mandriva.org> 1.8.7-1
+ Revision: 652659
- update to new version 1.8.7

* Thu Mar 31 2011 Sergio Rafael Lemke <sergio@mandriva.com> 1.8.6-1
+ Revision: 649495
- Update to version 1.8.6
  Drop mkrel

* Tue Jan 25 2011 Sergio Rafael Lemke <sergio@mandriva.com> 1.8.4-1
+ Revision: 632651
- New version - 1.8.4

* Mon Nov 22 2010 Funda Wang <fwang@mandriva.org> 1.7.2-1mdv2011.0
+ Revision: 599604
- update to new version 1.7.2

* Sat Oct 02 2010 Funda Wang <fwang@mandriva.org> 1.6.3-1mdv2011.0
+ Revision: 582414
- update to new version 1.6.3

* Tue Jul 20 2010 Funda Wang <fwang@mandriva.org> 1.5.2-1mdv2011.0
+ Revision: 555648
- update to new version 1.5.2

* Fri Apr 16 2010 Frederik Himpe <fhimpe@mandriva.org> 1.3.1-1mdv2010.1
+ Revision: 535583
- update to new version 1.3.1

* Sat Apr 10 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.2.0-1mdv2010.1
+ Revision: 533537
- new upstream release 1.2.0

* Sun Feb 28 2010 Frederik Himpe <fhimpe@mandriva.org> 1.1.1-1mdv2010.1
+ Revision: 512677
- update to new version 1.1.1

* Thu Feb 11 2010 Funda Wang <fwang@mandriva.org> 1.0.2-1mdv2010.1
+ Revision: 504365
- New version 1.0.2

* Tue Jan 19 2010 Frederik Himpe <fhimpe@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 493823
- update to new version 1.0.1

* Sun Nov 15 2009 Frederik Himpe <fhimpe@mandriva.org> 0.69.2-2mdv2010.1
+ Revision: 466386
- Move files in %%{_lib} to separate package, so that 32 and 64 bit
  theme engines can be installed together
- Make it suggest systemsettings-qt-gtk (for configuration of GTK+
  theme in KDE) and qtcurve-gtk2, in order to have consistent theming

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.69.2-1mdv2010.1
+ Revision: 462189
- Update to new version 0.69.2

* Thu Sep 10 2009 Stéphane Téletchéa <steletch@mandriva.org> 0.68.0-1mdv2010.0
+ Revision: 436904
- Update to new version 0.68

* Thu Aug 13 2009 Frederik Himpe <fhimpe@mandriva.org> 0.67.5-1mdv2010.0
+ Revision: 416098
- update to new version 0.67.5

* Sat Aug 08 2009 Frederik Himpe <fhimpe@mandriva.org> 0.67.4-1mdv2010.0
+ Revision: 411527
- Update to new 0.67.4
- Remove kwin patch: fixed upstream

* Fri Jul 24 2009 Frederik Himpe <fhimpe@mandriva.org> 0.67.0-1mdv2010.0
+ Revision: 399420
- Update to new version 0.67.0
- Package translations

* Mon Jul 06 2009 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 0.65.1-2mdv2010.0
+ Revision: 392967
- Added patch to fix a KWin crash

* Wed Jul 01 2009 Frederik Himpe <fhimpe@mandriva.org> 0.65.1-1mdv2010.0
+ Revision: 391343
- update to new version 0.65.1

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 0.62.9-1mdv2010.0
+ Revision: 370787
- New version 0.62.9

* Wed Mar 18 2009 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 0.62.4-2mdv2009.1
+ Revision: 357315
- Fixed defattr issue

* Tue Mar 17 2009 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 0.62.4-1mdv2009.1
+ Revision: 356610
- Update to new version 0.62

* Sun Jan 11 2009 Frederik Himpe <fhimpe@mandriva.org> 0.60.0-1mdv2009.1
+ Revision: 328323
- Update to new version 0.60

* Fri Aug 01 2008 Funda Wang <fwang@mandriva.org> 0.59.6-1mdv2009.0
+ Revision: 259126
- New version 0.59.6
- update URL

* Tue Jul 22 2008 Leonardo de Amaral Vidal <leonardoav@mandriva.com> 0.59.5-1mdv2009.0
+ Revision: 240216
- New upstream release
- Make the obsoletes versioned

* Sat Jul 05 2008 Funda Wang <fwang@mandriva.org> 0.59.4-1mdv2009.0
+ Revision: 231983
- New version 0.59.4

* Fri Jul 04 2008 Funda Wang <fwang@mandriva.org> 0.59.3-2mdv2009.0
+ Revision: 231507
- rebuild

* Sun Jun 22 2008 Funda Wang <fwang@mandriva.org> 0.59.3-1mdv2009.0
+ Revision: 227908
- New version 0.59.3

* Tue Jun 17 2008 Helio Chissini de Castro <helio@mandriva.com> 0.59.2-2mdv2009.0
+ Revision: 222784
- Lowercasing the name
- Lowercase to match all other styles

* Thu May 15 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 0.59.2-1mdv2009.0
+ Revision: 207583
- import kde4-style-QtCurve

