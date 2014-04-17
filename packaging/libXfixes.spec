%bcond_with x

Name:           libXfixes
Version:        5.0.1
Release:        2
License:        MIT
Summary:        X Fixes library
Url:            http://www.x.org
Group:          Graphics/X Window System
Source:         %{name}-%{version}.tar.bz2
Source1001: 	libXfixes.manifest

BuildRequires:  pkgconfig(fixesproto)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%if !%{with x}
ExclusiveArch:
%endif

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
cp %{SOURCE1001} .

%build
%autogen --disable-static
make %{?_smp_mflags}

%install
%make_install
%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libXfixes.so.3
%{_libdir}/libXfixes.so.3.1.0

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/Xfixes.h
%{_libdir}/libXfixes.so
%{_libdir}/pkgconfig/xfixes.pc
