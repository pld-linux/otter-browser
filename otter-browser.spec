%define	orgname	otter
Summary:	Qt5WebKit browser
Name:		otter-browser
Version:	0.9.01
Release:	1
License:	GPL v3
Group:		X11/Applications/Networking
Source0:	http://github.com/Emdek/otter/archive/v%{version}.tar.gz
# Source0-md5:	081b62825ee2d3d1ed3eec9075c1eaad
URL:		http://otter-browser.org/
BuildRequires:	Qt5Script-devel >= 5.2.0
BuildRequires:	Qt5WebKit-devel >= 5.2.0
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.2
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qmake >= 4.7.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Project aiming to recreate classic Opera (12.x) UI using Qt5.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/otter-browser
%{_desktopdir}/otter-browser.desktop
%{_iconsdir}/hicolor/*/apps/otter-browser.png
