Name:     ocaml-lame

Version:  0.3.3
Release:  2
Summary:  OCaml bindings for the liblame
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-lame
Source0:  https://github.com/savonet/ocaml-lame/releases/download/0.3.3/ocaml-lame-0.3.3.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-camlidl
BuildRequires: lame-devel
Requires:      lame
Provides:      ocaml(Lame_dynlink)

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
%{_libdir}/ocaml/lame/
%{_libdir}/ocaml/lame/META
%{_libdir}/ocaml/lame/lame.a
%{_libdir}/ocaml/lame/lame.cma
%{_libdir}/ocaml/lame/lame.cmi
%{_libdir}/ocaml/lame/lame.cmx
%{_libdir}/ocaml/lame/lame.cmxa
%{_libdir}/ocaml/lame/lame.mli
%{_libdir}/ocaml/lame/lame.cmxs
%{_libdir}/ocaml/lame/lame_dynlink.mli
%{_libdir}/ocaml/lame/lame_loader.cma
%{_libdir}/ocaml/lame/lame_loader.cmi
%{_libdir}/ocaml/lame/lame_loader.cmx
%{_libdir}/ocaml/lame/lame_loader.cmxs
%{_libdir}/ocaml/lame/liblame_stubs.a
%{_libdir}/ocaml/stublibs/dlllame_stubs.so
%{_libdir}/ocaml/stublibs/dlllame_stubs.so.owner

%description
OCAML bindings for the liblame


%changelog
* Fri Nov 23 2018 Lucas Bickel <hairmare@rabe.ch> - 0.3.3-2
- Require missing ocaml-findlibs
- Start cleaning up files section
- Stomp a Tumbleweed bug

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-lame.spec
