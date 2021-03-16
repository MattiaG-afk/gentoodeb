# Copyright 2021 Gentoo Authors
# Distributed under the terms of the GNU General Public License v2

EAPI=7

DESCRIPTION="An easy to use installer for .deb packet on gentoo"
HOMEPAGE="https://github.com/MattiaG-afk/gentoodeb"
SRC_URI="https://github.com/MattiaG-afk/gentoodeb.git"

LICENSE="GNU"
SLOT="0"
KEYWORDS="~amd64 ~x86"

S="${WORKDIR}"

DEPEND=""
RDEPEND="${DEPEND}"
BDEPEND=""

src_install() {
	cd gentoodeb
	make DESTDIR=${D} install
}
