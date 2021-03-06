%define		kdeplasmaver	5.21.2
%define		qtver		5.9.0
%define		kpname		kscreen
Summary:	KDE's screen management software
Name:		kp5-%{kpname}
Version:	5.21.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	f97326e82343b238a53dd4569868720d
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
BuildRequires:	ninja
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
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kscreen-console
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/kscreen.so
%{_datadir}/kservices5/kcm_kscreen.desktop
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
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_kscreen.so
%{_datadir}/kpackage/kcms/kcm_kscreen
%{_datadir}/qlogging-categories5/kscreen.categories
