%define		kdeplasmaver	5.14.5
%define		qtver		5.9.0
%define		kpname		kscreen
Summary:	KDE's screen management software
Name:		kp5-%{kpname}
Version:	5.14.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	a3107c10a6622bf7386a0e4470707ac9
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE's screen management software.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kscreen-console
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kscreen.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/kscreen.so
%{_iconsdir}/hicolor/48x48/actions/kdocumentinfo.png
%{_iconsdir}/hicolor/scalable/actions/kdocumentinfo.svgz
%{_datadir}/kcm_kscreen
%{_datadir}/kservices5/kcm_kscreen.desktop
#%%{_datadir}/kservices5/kded/kscreen.desktop
/etc/xdg/kscreen.categories
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_kscreen.so
%dir %{_datadir}/kded_kscreen
%dir %{_datadir}/kded_kscreen/qml
%{_datadir}/kded_kscreen/qml/Osd.qml
%{_datadir}/kded_kscreen/qml/OsdItem.qml
%{_datadir}/kded_kscreen/qml/OsdSelector.qml
%{_datadir}/kded_kscreen/qml/OutputIdentifier.qml
%{_datadir}/kservices5/plasma-applet-org.kde.kscreen.desktop
%{_datadir}/metainfo/org.kde.kscreen.appdata.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.kscreen
%dir %{_datadir}/plasma/plasmoids/org.kde.kscreen/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.kscreen/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.kscreen/contents/ui/PresentationModeItem.qml
%{_datadir}/plasma/plasmoids/org.kde.kscreen/contents/ui/ScreenLayoutSelection.qml
%{_datadir}/plasma/plasmoids/org.kde.kscreen/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.kscreen/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.kscreen/metadata.json
