%define		qtver	5.9.0
Summary:	Browser aiming to recreate classic Opera (12.x) UI using Qt5
Summary(pl.UTF-8):	Przeglądarka, której celem jest odtworzenie klasycznego interfejsu Opery (12.x) przy użyciu Qt5
Name:		otter-browser
Version:	1.0.01
Release:	2
License:	GPL v3
Group:		X11/Applications/Networking
Source0:	https://github.com/OtterBrowser/otter-browser/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	99601d0b230956dc542a04f0df912626
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
BuildRequires:	Qt5XmlPatterns-devel >= %{qtver}
BuildRequires:	cmake >= 2.6.2
BuildRequires:	hunspell-devel
BuildRequires:	kf5-sonnet-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-qmake >= 4.7.0
BuildRequires:	rpmbuild(find_lang) >= 1.37
BuildRequires:	tar >= 1:1.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Otter Browser aims to recreate the best aspects of the classic Opera
(12.x) UI using Qt5.

%description -l pl.UTF-8
Otter Browser to przeglądarka, której celem jest odtworzenie
najlepszych aspektów klasycznego interfejsu użytkownika Opery (12.x)
przy użyciu Qt5.

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
