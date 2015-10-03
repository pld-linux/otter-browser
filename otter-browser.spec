%define		qtver	5.2.0
Summary:	Browser aiming to recreate classic Opera (12.x) UI using Qt5
Name:		otter-browser
Version:	0.9.07
Release:	1
License:	GPL v3
Group:		X11/Applications/Networking
Source0:	https://github.com/OtterBrowser/otter-browser/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	82198cedb0d817932d556b80c2676040
URL:		http://otter-browser.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Multimedia-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtver}
BuildRequires:	Qt5Script-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5WebKit-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 2.6.2
BuildRequires:	libstdc++-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-qmake >= 4.7.0
BuildRequires:	rpmbuild(find_lang) >= 1.37
BuildRequires:	tar >= 1:1.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Otter Browser aims to recreate the best aspects of the classic Opera
(12.x) UI using Qt5.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/otter-browser
%{_mandir}/man1/otter-browser.1*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
