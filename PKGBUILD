# Script generated with Bloom
pkgdesc="ROS - Provides a portable set of time functions that are especially useful for porting other code or being wrapped by higher level c++ classes."
url='http://wiki.ros.org/ecl_time_lite'

pkgname='ros-lunar-ecl-time-lite'
pkgver='0.61.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-ecl-build'
'ros-lunar-ecl-config'
'ros-lunar-ecl-errors'
'ros-lunar-ecl-license'
)

depends=('ros-lunar-ecl-build'
'ros-lunar-ecl-config'
'ros-lunar-ecl-errors'
'ros-lunar-ecl-license'
)

conflicts=()
replaces=()

_dir=ecl_time_lite
source=()
md5sums=()

prepare() {
    cp -R $startdir/ecl_time_lite $srcdir/ecl_time_lite
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

