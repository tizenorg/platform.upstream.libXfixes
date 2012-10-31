Name:           libXfixes
Version:        5.0
Release:        2
License:        MIT
Summary:        X Fixes library
Url:            http://www.x.org
Group:          System Environment/Libraries

Source:         %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig(fixesproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%description
X Fixes library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:       pkgconfig

%description devel
libXfixes development package

%prep
%setup -q

%build
%configure --disable-static \
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?_smp_mflags}

%install
%make_install
%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libXfixes.so.3
%{_libdir}/libXfixes.so.3.1.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/Xfixes.h
%{_libdir}/libXfixes.so
%{_libdir}/pkgconfig/xfixes.pc
#%{_mandir}/man3/Xfixes.3
