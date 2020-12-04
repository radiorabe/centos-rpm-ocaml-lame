#!/bin/bash
#
# RPM build wrapper for ocaml-lame, runs inside the build container on travis-ci

set -xe

curl -o /etc/yum.repos.d/ocaml.repo "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap:/ocaml/CentOS_8/home:radiorabe:liquidsoap:ocaml.repo"

dnf config-manager --set-disabled epel
dnf -y install lame-devel --enablerepo=PowerTools

chown root:root ocaml-lame.spec

USER=nobody build-rpm-package.sh ocaml-lame.spec
