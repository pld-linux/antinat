Summary:	A SOCKS server for SOCKS4 and SOCKS5
Summary(pl):	Serwer SOCKS dla SOCKS4 SOCKS5
Name:		antinat
Version:	0.64
Release:	0.1
License:	GPL
Group:		Daemons
Source0:	http://yallara.cs.rmit.edu.au/%7Emalsmith/C0A00201/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	08250f314de6203fb1ee1b542fcbb02f
Patch0:		%{name}-makefile.patch
URL:		http://yallara.cs.rmit.edu.au/~malsmith/products/antinat/
BuildRequires:	libds-devel >= 1.2.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A SOCKS server for SOCKS4 and SOCKS5

%description -l pl
Serwer SOCKS dla SOCKS4 SOCKS5

%package socks4
Group:		Daemons
Requires:	antinat = %{version}
Summary:	Support for SOCKS4 in antinat

%description socks4
Support for older style SOCKS4 connections in antinat. SOCKS4 is
limited to anonymous only connections, and if authentication is
required, do not install this package.

%package logging
Group:		Daemons
Requires:	antinat = %{version}
Summary:	Support for logging in antinat

%description logging
Support for connection and summary logging in antinat.

%package filtering
Group:		Daemons
Requires:	antinat = %{version}
Summary:	Support for filtering in antinat

%description filtering
Support for allowing and disallowing connections on the basis of some
criteria in antinat. Included are filters for IPv4 source and
destination addresses, as well as ports.

%package anonymous
Group:		Daemons
Requires:	antinat = %{version}
Summary:	Support for anonymous SOCKS5 connections in antinat

%description anonymous
Support for anonymous (non-authenticated) connections in antinat. If
this package is not installed, clients must give the username and
password credentials of a user on the server to proceed. Note that
socks4 will also provide anonymous connections, in effect.

%package ipv6
Group:		Daemons
Requires:	antinat = %{version}
Summary:	Support for IPv6 connections in antinat

%description ipv6
Support for IPv6 connections, to allow the server to connect to v6
hosts and be connected to from v6 hosts.

%package udp
Group:		Daemons
Requires:	antinat = %{version}
Summary:	Support for UDP Association in antinat

%description udp
Support for UDP association over SOCKSv5. This allows hosts to send
and receive UDP packets through the SOCKS server.

%prep
%setup -q
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}

%configure \
	--datadir=%{_libdir} \
	--with-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	datadir=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -fR $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README TODO
%config(noreplace) %{_sysconfdir}/antinat.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*
%{_libdir}/%{name}/address/libipv4.so
%{_libdir}/%{name}/version5/authenticators/libunpw.so
%{_libdir}/%{name}/version5/authenticators/unpwsources
%{_libdir}/%{name}/version5/commands/libconn.so
%{_libdir}/%{name}/version5/commands/libbind.so
%{_libdir}/%{name}/version5/commands/libident.so
%{_libdir}/%{name}/resolvers/libipv4.so
%{_libdir}/%{name}/resolvers/libname.so
%{_libdir}/%{name}/revres/libipv4.so
%{_libdir}/%{name}/versions/libv5.so

%files socks4
%defattr(644,root,root,755)
%{_libdir}/%{name}/version4/*
%{_libdir}/%{name}/versions/libv4.so

%files logging
%defattr(644,root,root,755)
%{_libdir}/%{name}/loggers/*
%{_localstatedir}

%files filtering
%defattr(644,root,root,755)
%{_libdir}/%{name}/filters/*

%files anonymous
%defattr(644,root,root,755)
%{_libdir}/%{name}/version5/authenticators/libanon.so

%files ipv6
%defattr(644,root,root,755)
%{_libdir}/%{name}/address/libipv6.so
%{_libdir}/%{name}/resolvers/libipv6.so
%{_libdir}/%{name}/revres/libipv6.so

%files udp
%defattr(644,root,root,755)
%{_libdir}/%{name}/version5/commands/libudp.so
