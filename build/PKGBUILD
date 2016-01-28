# Maintainer: Romanos Skiadas <rom.skiad@gmail.com>
# Contributor: Flaviu Tamas <tamas.flaviu@gmail.com>
# Contributor: Guangyu Zhang <zguangyu123@gmail.com>
pkgname=testu01-parallel
_pkgname=TestU01-parallel
pkgrel=1
pkgdesc="A version of the TestU01 library that implements parallel Crush tests"
arch=('i686' 'x86_64')
url='https://github.com/rski/testu01-parallel'
license=('custom')
depends=('glibc python')
source="git+https://github.com/rski/testu01-parallel.git"
sha256sums=('SKIP')
conflicts=('testu01')

pkgver() {
  cd "$pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd "$srcdir/$pkgname"
  ./configure --prefix=/usr
  make
}

package() {
  cd "$srcdir/$pkgname"
  make DESTDIR="$pkgdir/" install
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
