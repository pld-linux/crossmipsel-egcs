Summary:	Cross-egcs for mipsel-linux on i386 systems
Summary(de):	Cross-egcs zur Erzeugung von little-Endian MIPS-Code auf i386
Summary(pl):	egcs kroskompiluj±cy na mipsel-linux
Name:		crossmipsel-egcs
Version:	1.0.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	ftp://alge.anart.no/pub/devel/egcs-%{version}.tar.gz
#Source0:	ftp://gcc.gnu.org/pub/gcc/releases/egcs-1.1.2/egcs-1.1.2.tar.bz2
Source1:	mipsel-cross-egcs.sh
Patch0:		egcs-1.0.2-libio.patch
Patch1:		egcs-1.0.2-hjl.patch
Patch2:		egcs-1.0.2-rth1.patch
Patch3:		egcs-1.0.2-rth2.patch
Patch4:		egcs-1.0.2-rth3.patch
Patch5:		egcs-1.0.2-rth4.patch
Patch6:		egcs-1.0.2-hjl2.patch
Patch7:		egcs-1.0.2-jim.patch
Patch8:		egcs-1.0.2-haifa.patch
Patch9:		egcs-1.0.1-objcbackend.patch
Patch10:	egcs-1.0.2-mips.patch
Requires:	crossmipsel-binutils >= 2.8.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/opt/mipsel
%define         _infodir        %{_prefix}/info

%description
This package contains a cross-egcs which allows the creation of
binaries to be run on little-endian Linux-MIPS (architecture
"mipsel-linux") on i386-machines. Currently this is only a first-stage
compiler, i.e. it can compile a Linux kernel, but not user space
applications.

%description -l de
Dieses Paket enthält einen Cross-egcs, der es erlaubt, auf einem
i386-Rechner Code für Linux-MIPS (auf little-Endian-Rechnern) zu
generieren. Derzeit existiert nur die erste Compiler-Stufe, d.h. der
Compiler ist in der Lage, einen Linux-Kernel zu kompilieren, jedoch
noch keine Anwendungsprogramme.

%description -l pl
Ten pakiet zawiera cross-egcs pozwalaj±cy na robienie binariów do
uruchamiania na little-endian MIPS (architektura "mipsel-linux") na
maszynach i386. Aktualnie jest to tylko kompilator pierszego etapu,
którym mo¿na skompilowaæ kernel, ale nie aplikacje.

%prep
%setup -q -n egcs-1.0.2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
%configure --with-newlib --target=mipsel-linux
cd gcc
%{__make} LANGUAGES="c"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/profile.d,%{_prefix}}

install %{SOURCE1}	$RPM_BUILD_ROOT/etc/profile.d/

cd gcc
%{__make} LANGUAGES="c" prefix=$RPM_BUILD_ROOT%{_prefix} exec_prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %config /etc/profile.d/*
%attr(755,root,root) %{_bindir}/mipsel-linux-gcc
%dir %{_libdir}/gcc-lib
%dir %{_libdir}/gcc-lib/mipsel-linux
%dir %{_libdir}/gcc-lib/mipsel-linux/egcs-2.90.27
%dir %{_libdir}/gcc-lib/mipsel-linux/egcs-2.90.27/include
%dir %{_libdir}/gcc-lib/mipsel-linux/egcs-2.90.27/eb
%{_libdir}/gcc-lib/mipsel-linux/egcs-2.90.27/eb/libgcc.a
%{_libdir}/gcc-lib/mipsel-linux/egcs-2.90.27/include/*
%attr(755,root,root) %{_libdir}/gcc-lib/mipsel-linux/egcs-2.90.27/cc1
%attr(755,root,root) %{_libdir}/gcc-lib/mipsel-linux/egcs-2.90.27/ld
%attr(755,root,root) %{_libdir}/gcc-lib/mipsel-linux/egcs-2.90.27/cpp
%{_libdir}/gcc-lib/mipsel-linux/egcs-2.90.27/specs
%{_libdir}/gcc-lib/mipsel-linux/egcs-2.90.27/*.[oa]
%{_mandir}/man*/*
%{_infodir}/*
