%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kdesdk-thumbnailers
Summary:	kdesdk thumbnailers
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	b0b6887e7fd615b5117b198ce9e7979c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for the thumbnailing system.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/pothumbnail.so
%{_datadir}/config.kcfg/pocreatorsettings.kcfg
%{_datadir}/kservices5/pothumbnail.desktop
