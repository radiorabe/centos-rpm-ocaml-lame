Name:     ocaml-lame
Version:  0.3.4
Release:  0.1%{?dist}
Summary:  OCaml bindings for the liblame

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/savonet/ocaml-lame
Source0:  https://github.com/savonet/ocaml-lame/archive/v%{version}.tar.gz?#/%{name}-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-dune-devel
BuildRequires: lame-devel
Requires:      lame-libs
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
dune build

%install
dune install \
  --prefix %{buildroot} \
  --libdir %{buildroot}$(ocamlfind printconf destdir)
rm -rf %{buildroot}/doc


%files
%doc README.md CHANGES
%license COPYING
%{_libdir}/ocaml/%{libname}
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so
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
* Fri Dec 4 2020 Lucas Bickel <hairmare@rabe.ch> - 0.3.4-0.1
- Bump to 0.3.4

* Sun Dec  9 2018 Lucas Bickel <hairmare@rabe.ch> - 0.3.3-3
- Cleanup and add separate -devel subpackage

* Fri Nov 23 2018 Lucas Bickel <hairmare@rabe.ch> - 0.3.3-2
- Require missing ocaml-findlibs
- Start cleaning up files section
- Stomp a Tumbleweed bug

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch> - 0.3.3-1
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-lame.spec
