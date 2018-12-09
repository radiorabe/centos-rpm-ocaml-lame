Name:     ocaml-lame
Version:  0.3.3
Release:  3%{?dist}
Summary:  OCaml bindings for the liblame

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/savonet/ocaml-lame
Source0:  https://github.com/savonet/ocaml-lame/releases/download/0.3.3/ocaml-lame-0.3.3.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-camlidl
BuildRequires: ocaml-findlib
BuildRequires: lame-devel
Requires:      lame
Provides:      ocaml(Lame_dynlink)


%description
OCAML bindings for the liblame


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}

%build
./configure \
   --prefix=%{_prefix} \
   --disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
%doc README
%license COPYING
%{_libdir}/ocaml/%{libname}
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so.owner
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license COPYING
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Sun Dec  9 2018 Lucas Bickel <hairmare@rabe.ch> - 0.3.3-3
- Cleanup and add separate -devel subpackage

* Fri Nov 23 2018 Lucas Bickel <hairmare@rabe.ch> - 0.3.3-2
- Require missing ocaml-findlibs
- Start cleaning up files section
- Stomp a Tumbleweed bug

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch> - 0.3.3-1
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-lame.spec
