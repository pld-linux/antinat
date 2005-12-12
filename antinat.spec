Summary:	A SOCKS server for SOCKS4 and SOCKS5
Summary(pl):	Serwer SOCKS dla SOCKS4 i SOCKS5
Name:		antinat
Version:	0.71
Release:	0.1
License:	GPL
Group:		Daemons
Source0:	http://dl.sourceforge.net/antinat/%{name}-%{version}.tar.bz2
# Source0-md5:	842899a5fa705df1b0b8d8edee372fa2
# doesn't exist in SOURCES but probably needed to do s/%{name}-%{version}/%{name}/ and add DESTDIR
#Patch0:		%{name}-makefile.patch
URL:		http://yallara.cs.rmit.edu.au/~malsmith/products/antinat/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libds-devel >= 1.2.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# *.so are installed there
%define		_datadir	%{_libdir}
%define		_localstatedir	/var/lib

%description
A SOCKS server for SOCKS4 and SOCKS5.

%description -l pl
Serwer SOCKS dla SOCKS4 i SOCKS5.

%package socks4
Summary:	Support for SOCKS4 in antinat
Summary(pl):	Wsparcie w antinacie dla SOCKS4
Group:		Daemons
Requires:	%{name} = %{version}

%description socks4
Support for older style SOCKS4 connections in antinat. SOCKS4 is
limited to anonymous only connections, and if authentication is
required, do not install this package.

%description socks4 -l pl
Wsparcie w antinacie dla starego typu po³±czeñ SOCKS4. SOCKS4 jest
ograniczone do po³±czeñ anonimowych, wiêc je¶li wymagana jest
autoryzacja, nie nale¿y instalowaæ tego pakietu.

%package logging
Summary:	Support for logging in antinat
Summary(pl):	Wsparcie dla logowania przez antinata
Group:		Daemons
Requires:	%{name} = %{version}

%description logging
Support for connection and summary logging in antinat.

%description logging -l pl
Wsparcie dla logowania po³±czeñ i podsumowañ przez antinata.

%package filtering
Summary:	Support for filtering in antinat
Summary(pl):	Wsparcie dla filtrowania przez antinata
Group:		Daemons
Requires:	%{name} = %{version}

%description filtering
Support for allowing and disallowing connections on the basis of some
criteria in antinat. Included are filters for IPv4 source and
destination addresses, as well as ports.

%description filtering -l pl
Wsparcie dla umo¿liwiania i blokowania przez antinata po³±czeñ w
oparciu o pewne kryteria. Zawiera filtry dzia³aj±ce w oparciu o adresy
¼ród³owe i docelowe, jak te¿ w oparciu o porty.

%package anonymous
Summary:	Support for anonymous SOCKS5 connections in antinat
Summary(pl):	Wsparcie w antinacie dla anonimowych po³±czeñ SOCKS5
Group:		Daemons
Requires:	%{name} = %{version}

%description anonymous
Support for anonymous (non-authenticated) connections in antinat. If
this package is not installed, clients must give the username and
password credentials of a user on the server to proceed. Note that
antinat-socks4 package will also provide anonymous connections, in
effect.

%description anonymous -l pl
Wsparcie w antinacie dla po³±czeñ anonimowych (nie autoryzowanych).
Gdy ten pakiet nie jest zainstalowany, konieczne jest podanie przez
klienta nazwy i has³a u¿ytkownika na serwerze. Nale¿y zauwa¿yæ, ¿e
pakiet antinat-socks4 równie¿ w zasadzie umo¿liwia po³±czenia
anonimowe.

%package ipv6
Summary:	Support for IPv6 connections in antinat
Summary(pl):	Wsparcie w antinacie dla po³±czeñ IPv6
Group:		Daemons
Requires:	%{name} = %{version}

%description ipv6
Support for IPv6 connections, to allow the server to connect to v6
hosts and be connected to from v6 hosts.

%description ipv6 -l pl
Wsparcie dla po³±czeñ IPv6 umo¿liwiaj±ce serwerowi ³±czenie sie z i do
hostów IPv6.

%package udp
Summary:	Support for UDP association in antinat
Summary(pl):	Wsparcie w antinacie dla kojarzenia UDP
Group:		Daemons
Requires:	%{name} = %{version}

%description udp
Support for UDP association over SOCKSv5. This allows hosts to send
and receive UDP packets through the SOCKS server.

%description udp -l pl
Wsparcie dla kojarzenia UDP poprzez SOCKSv5. Umo¿liwia to wysy³anie i
odbiór pakietów za po¶rednictwem serwera SOCKS.

%prep
%setup -q
#%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-ipv6
#	--datadir=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_libdir} \
	localstatedir=$RPM_BUILD_ROOT%{_localstatedir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}
#	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -fR $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/antinat.conf
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/address
%attr(755,root,root) %{_libdir}/%{name}/address/libipv4.so
%dir %{_libdir}/%{name}/version5
%dir %{_libdir}/%{name}/version5/authenticators
%attr(755,root,root) %{_libdir}/%{name}/version5/authenticators/libunpw.so
%attr(755,root,root) %{_libdir}/%{name}/version5/authenticators/unpwsources
%dir %{_libdir}/%{name}/version5/commands
%attr(755,root,root) %{_libdir}/%{name}/version5/commands/libconn.so
%attr(755,root,root) %{_libdir}/%{name}/version5/commands/libbind.so
%attr(755,root,root) %{_libdir}/%{name}/version5/commands/libident.so
%dir %{_libdir}/%{name}/resolvers
%attr(755,root,root) %{_libdir}/%{name}/resolvers/libipv4.so
%attr(755,root,root) %{_libdir}/%{name}/resolvers/libname.so
%dir %{_libdir}/%{name}/revres
%attr(755,root,root) %{_libdir}/%{name}/revres/libipv4.so
%dir %{_libdir}/%{name}/versions
%attr(755,root,root) %{_libdir}/%{name}/versions/libv5.so
%{_mandir}/man[15]/*

%files socks4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/version4
%attr(755,root,root) %{_libdir}/%{name}/versions/libv4.so

%files logging
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/loggers
%{_localstatedir}/%{name}

%files filtering
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/filters

%files anonymous
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/version5/authenticators/libanon.so

%files ipv6
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/address/libipv6.so
%attr(755,root,root) %{_libdir}/%{name}/resolvers/libipv6.so
%attr(755,root,root) %{_libdir}/%{name}/revres/libipv6.so

%files udp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/version5/commands/libudp.so
