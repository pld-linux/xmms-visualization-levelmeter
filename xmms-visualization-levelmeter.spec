Summary:	Plugin which draws simple level meter
Summary(pl):	Plugin wizualizacji graficznej prostego miernika poziomu
Name:		xmms-visualization-levelmeter
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.gadaud.org/fabrice/xmms-levelmeter.tgz
URL:		http://membres.lycos.fr/gadaud/fabrice/xmms/
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Plugin which draw simple level meter.

%description -l pl
Wtyczka rysuj±ca prosty wska¼nik poziomu sygna³u.

%prep
%setup -q -n SLevel
%build
%{__make} \
	COMMON_CFLAGS="%{rpmcflags} -ffast-math `glib-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/`%{_bindir}/xmms-config --visualization-plugin-dir`/
install simplelevel.so \
	$RPM_BUILD_ROOT/`%{_bindir}/xmms-config	--visualization-plugin-dir`/simplelevel.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_libdir}/xmms/*/*.so
