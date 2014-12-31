%define	orgname	otter
Summary:	Qt5WebKit browser
Name:		otter-browser
Version:	0.9.03
Release:	1
License:	GPL v3
Group:		X11/Applications/Networking
Source0:	http://github.com/Emdek/otter/archive/v%{version}.tar.gz
# Source0-md5:	d13b34ad5a15d70590cb04e594b752f4
URL:		http://otter-browser.org/
BuildRequires:	Qt5Concurrent-devel >= 5.2.0
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5Gui-devel >= 5.2.0
BuildRequires:	Qt5Network-devel >= 5.2.0
BuildRequires:	Qt5PrintSupport-devel >= 5.2.0
BuildRequires:	Qt5Script-devel >= 5.2.0
BuildRequires:	Qt5Sql-devel >= 5.2.0
BuildRequires:	Qt5WebKit-devel >= 5.2.0
BuildRequires:	Qt5Widgets-devel >= 5.2.0
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
%dir %{_datadir}/otter-browser
%dir %{_datadir}/otter-browser/locale
%lang(cs) %{_datadir}/otter-browser/locale/otter-browser_cs_CZ.qm
%lang(de) %{_datadir}/otter-browser/locale/otter-browser_de_DE.qm
%lang(en_GB) %{_datadir}/otter-browser/locale/otter-browser_en_GB.qm
%lang(en_US) %{_datadir}/otter-browser/locale/otter-browser_en_US.qm
%lang(es) %{_datadir}/otter-browser/locale/otter-browser_es_ES.qm
%lang(et) %{_datadir}/otter-browser/locale/otter-browser_et.qm
%lang(fi) %{_datadir}/otter-browser/locale/otter-browser_fi.qm
%lang(fr) %{_datadir}/otter-browser/locale/otter-browser_fr_FR.qm
%lang(hu) %{_datadir}/otter-browser/locale/otter-browser_hu.qm
%lang(id) %{_datadir}/otter-browser/locale/otter-browser_id_ID.qm
%lang(it) %{_datadir}/otter-browser/locale/otter-browser_it_IT.qm
%lang(ka) %{_datadir}/otter-browser/locale/otter-browser_ka_GE.qm
%lang(lt) %{_datadir}/otter-browser/locale/otter-browser_lt.qm
%lang(no) %{_datadir}/otter-browser/locale/otter-browser_nb_NO.qm
%lang(nl) %{_datadir}/otter-browser/locale/otter-browser_nl.qm
%lang(pl) %{_datadir}/otter-browser/locale/otter-browser_pl_PL.qm
%lang(pt_BR) %{_datadir}/otter-browser/locale/otter-browser_pt_BR.qm
%lang(pt_PT) %{_datadir}/otter-browser/locale/otter-browser_pt_PT.qm
%lang(ro) %{_datadir}/otter-browser/locale/otter-browser_ro.qm
%lang(ru) %{_datadir}/otter-browser/locale/otter-browser_ru_RU.qm
%lang(sk) %{_datadir}/otter-browser/locale/otter-browser_sk.qm
%lang(sr) %{_datadir}/otter-browser/locale/otter-browser_sr.qm
#%lang(sr) %{_datadir}/otter-browser/locale/otter-browser_sr@Ijekavian.qm
#%lang(sr) %{_datadir}/otter-browser/locale/otter-browser_sr@ijekavianlatin.qm
#%lang(sr) %{_datadir}/otter-browser/locale/otter-browser_sr@latin.qm
%lang(tr) %{_datadir}/otter-browser/locale/otter-browser_tr_TR.qm
%lang(uk) %{_datadir}/otter-browser/locale/otter-browser_uk_UA.qm
%lang(zh_CN) %{_datadir}/otter-browser/locale/otter-browser_zh_CN.qm
%lang(zh_TW) %{_datadir}/otter-browser/locale/otter-browser_zh_TW.qm
