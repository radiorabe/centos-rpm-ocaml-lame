Name:     ocaml-lame

Version:  0.3.3
Release:  1
Summary:  OCaml bindings for the liblame
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-lame
Source0:  https://github.com/savonet/ocaml-lame/releases/download/0.3.3/ocaml-lame-0.3.3.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-camlidl
BuildRequires: lame-devel
Requires:      lame

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
/usr/lib64/ocaml/lame/META
/usr/lib64/ocaml/lame/lame.a
/usr/lib64/ocaml/lame/lame.cma
/usr/lib64/ocaml/lame/lame.cmi
/usr/lib64/ocaml/lame/lame.cmx
/usr/lib64/ocaml/lame/lame.cmxa
/usr/lib64/ocaml/lame/lame.mli
/usr/lib64/ocaml/lame/lame.cmxs
/usr/lib64/ocaml/lame/lame_dynlink.mli
/usr/lib64/ocaml/lame/lame_loader.cma
/usr/lib64/ocaml/lame/lame_loader.cmi
/usr/lib64/ocaml/lame/lame_loader.cmx
/usr/lib64/ocaml/lame/lame_loader.cmxs
/usr/lib64/ocaml/lame/liblame_stubs.a
/usr/lib64/ocaml/stublibs/dlllame_stubs.so
/usr/lib64/ocaml/stublibs/dlllame_stubs.so.owner

%description
OCAML bindings for the liblame


%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-lame.spec
