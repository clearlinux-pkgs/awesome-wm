#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x22E428EBCB8FCB06 (psychon@znc.in)
#
Name     : awesome-wm
Version  : 4.3
Release  : 8
URL      : https://github.com/awesomeWM/awesome/releases/download/v4.3/awesome-4.3.tar.xz
Source0  : https://github.com/awesomeWM/awesome/releases/download/v4.3/awesome-4.3.tar.xz
Source99 : https://github.com/awesomeWM/awesome/releases/download/v4.3/awesome-4.3.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: awesome-wm-bin = %{version}-%{release}
Requires: awesome-wm-data = %{version}-%{release}
Requires: awesome-wm-license = %{version}-%{release}
Requires: cairo-lib
Requires: dbus-lib
Requires: expat-lib
Requires: fontconfig-lib
Requires: freetype-lib
Requires: gdk-pixbuf-lib
Requires: glib-lib
Requires: graphite-lib
Requires: harfbuzz-lib
Requires: libX11-lib
Requires: libXau-lib
Requires: libXdamage-lib
Requires: libXdmcp-lib
Requires: libXext-lib
Requires: libXfixes-lib
Requires: libXxf86vm-lib
Requires: libdrm-lib
Requires: libffi-lib
Requires: libgcrypt-lib
Requires: libgpg-error-lib
Requires: libpng-lib
Requires: libxcb-lib
Requires: libxdg-basedir
Requires: libxkbcommon-lib
Requires: libxshmfence-lib
Requires: lualgi
Requires: mesa-lib
Requires: pcre-lib
Requires: pixman-lib
Requires: startup-notification-lib
Requires: systemd-lib
Requires: util-linux-lib
Requires: wayland-lib
Requires: xcb-util-cursor-lib
Requires: xcb-util-image-lib
Requires: xcb-util-keysyms-lib
Requires: xcb-util-lib
Requires: xcb-util-renderutil-lib
Requires: xcb-util-wm-lib
Requires: xcb-util-xrm
Requires: xz-lib
Requires: zlib-lib
BuildRequires : ImageMagick
BuildRequires : buildreq-cmake
BuildRequires : gdk-pixbuf-dev
BuildRequires : glib-dev
BuildRequires : lua-dev
BuildRequires : lualgi-lib
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-xcb)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(libxdg-basedir)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-cursor)
BuildRequires : pkgconfig(xcb-xrm)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xkbcommon-x11)
BuildRequires : startup-notification-dev
Patch1: install-awesome.desktop-into-gnome-sessions.patch

%description
Background images:
Mikael Eriksson <mikael_eriksson@miffe.org>
Licensed under CC-BY-SA-3.0

%package bin
Summary: bin components for the awesome-wm package.
Group: Binaries
Requires: awesome-wm-data = %{version}-%{release}
Requires: awesome-wm-license = %{version}-%{release}

%description bin
bin components for the awesome-wm package.


%package data
Summary: data components for the awesome-wm package.
Group: Data

%description data
data components for the awesome-wm package.


%package doc
Summary: doc components for the awesome-wm package.
Group: Documentation

%description doc
doc components for the awesome-wm package.


%package license
Summary: license components for the awesome-wm package.
Group: Default

%description license
license components for the awesome-wm package.


%prep
%setup -q -n awesome-4.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548690186
mkdir -p clr-build
pushd clr-build
%cmake .. -DSYSCONFDIR=/usr/share
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1548690186
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/awesome-wm
cp LICENSE %{buildroot}/usr/share/package-licenses/awesome-wm/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/awesome
/usr/bin/awesome-client

%files data
%defattr(-,root,root,-)
/usr/share/awesome/icons/awesome16.png
/usr/share/awesome/icons/awesome32.png
/usr/share/awesome/icons/awesome48.png
/usr/share/awesome/icons/awesome64.png
/usr/share/awesome/lib/awful/autofocus.lua
/usr/share/awesome/lib/awful/button.lua
/usr/share/awesome/lib/awful/client.lua
/usr/share/awesome/lib/awful/client/focus.lua
/usr/share/awesome/lib/awful/client/shape.lua
/usr/share/awesome/lib/awful/client/urgent.lua
/usr/share/awesome/lib/awful/completion.lua
/usr/share/awesome/lib/awful/dbus.lua
/usr/share/awesome/lib/awful/ewmh.lua
/usr/share/awesome/lib/awful/hotkeys_popup/init.lua
/usr/share/awesome/lib/awful/hotkeys_popup/keys/firefox.lua
/usr/share/awesome/lib/awful/hotkeys_popup/keys/init.lua
/usr/share/awesome/lib/awful/hotkeys_popup/keys/qutebrowser.lua
/usr/share/awesome/lib/awful/hotkeys_popup/keys/termite.lua
/usr/share/awesome/lib/awful/hotkeys_popup/keys/tmux.lua
/usr/share/awesome/lib/awful/hotkeys_popup/keys/vim.lua
/usr/share/awesome/lib/awful/hotkeys_popup/widget.lua
/usr/share/awesome/lib/awful/init.lua
/usr/share/awesome/lib/awful/key.lua
/usr/share/awesome/lib/awful/keygrabber.lua
/usr/share/awesome/lib/awful/layout/init.lua
/usr/share/awesome/lib/awful/layout/suit/corner.lua
/usr/share/awesome/lib/awful/layout/suit/fair.lua
/usr/share/awesome/lib/awful/layout/suit/floating.lua
/usr/share/awesome/lib/awful/layout/suit/init.lua
/usr/share/awesome/lib/awful/layout/suit/magnifier.lua
/usr/share/awesome/lib/awful/layout/suit/max.lua
/usr/share/awesome/lib/awful/layout/suit/spiral.lua
/usr/share/awesome/lib/awful/layout/suit/tile.lua
/usr/share/awesome/lib/awful/menu.lua
/usr/share/awesome/lib/awful/mouse/drag_to_tag.lua
/usr/share/awesome/lib/awful/mouse/init.lua
/usr/share/awesome/lib/awful/mouse/resize.lua
/usr/share/awesome/lib/awful/mouse/snap.lua
/usr/share/awesome/lib/awful/placement.lua
/usr/share/awesome/lib/awful/popup.lua
/usr/share/awesome/lib/awful/prompt.lua
/usr/share/awesome/lib/awful/remote.lua
/usr/share/awesome/lib/awful/rules.lua
/usr/share/awesome/lib/awful/screen.lua
/usr/share/awesome/lib/awful/spawn.lua
/usr/share/awesome/lib/awful/startup_notification.lua
/usr/share/awesome/lib/awful/tag.lua
/usr/share/awesome/lib/awful/titlebar.lua
/usr/share/awesome/lib/awful/tooltip.lua
/usr/share/awesome/lib/awful/util.lua
/usr/share/awesome/lib/awful/wibar.lua
/usr/share/awesome/lib/awful/wibox.lua
/usr/share/awesome/lib/awful/widget/button.lua
/usr/share/awesome/lib/awful/widget/calendar_popup.lua
/usr/share/awesome/lib/awful/widget/clienticon.lua
/usr/share/awesome/lib/awful/widget/common.lua
/usr/share/awesome/lib/awful/widget/graph.lua
/usr/share/awesome/lib/awful/widget/init.lua
/usr/share/awesome/lib/awful/widget/keyboardlayout.lua
/usr/share/awesome/lib/awful/widget/launcher.lua
/usr/share/awesome/lib/awful/widget/layoutbox.lua
/usr/share/awesome/lib/awful/widget/layoutlist.lua
/usr/share/awesome/lib/awful/widget/only_on_screen.lua
/usr/share/awesome/lib/awful/widget/progressbar.lua
/usr/share/awesome/lib/awful/widget/prompt.lua
/usr/share/awesome/lib/awful/widget/taglist.lua
/usr/share/awesome/lib/awful/widget/tasklist.lua
/usr/share/awesome/lib/awful/widget/textclock.lua
/usr/share/awesome/lib/awful/widget/watch.lua
/usr/share/awesome/lib/beautiful.lua
/usr/share/awesome/lib/beautiful/gtk.lua
/usr/share/awesome/lib/beautiful/init.lua
/usr/share/awesome/lib/beautiful/theme_assets.lua
/usr/share/awesome/lib/beautiful/xresources.lua
/usr/share/awesome/lib/gears/cache.lua
/usr/share/awesome/lib/gears/color.lua
/usr/share/awesome/lib/gears/debug.lua
/usr/share/awesome/lib/gears/filesystem.lua
/usr/share/awesome/lib/gears/geometry.lua
/usr/share/awesome/lib/gears/init.lua
/usr/share/awesome/lib/gears/math.lua
/usr/share/awesome/lib/gears/matrix.lua
/usr/share/awesome/lib/gears/object.lua
/usr/share/awesome/lib/gears/object/properties.lua
/usr/share/awesome/lib/gears/protected_call.lua
/usr/share/awesome/lib/gears/shape.lua
/usr/share/awesome/lib/gears/sort/init.lua
/usr/share/awesome/lib/gears/sort/topological.lua
/usr/share/awesome/lib/gears/string.lua
/usr/share/awesome/lib/gears/surface.lua
/usr/share/awesome/lib/gears/table.lua
/usr/share/awesome/lib/gears/timer.lua
/usr/share/awesome/lib/gears/wallpaper.lua
/usr/share/awesome/lib/menubar/icon_theme.lua
/usr/share/awesome/lib/menubar/index_theme.lua
/usr/share/awesome/lib/menubar/init.lua
/usr/share/awesome/lib/menubar/menu_gen.lua
/usr/share/awesome/lib/menubar/utils.lua
/usr/share/awesome/lib/naughty.lua
/usr/share/awesome/lib/naughty/core.lua
/usr/share/awesome/lib/naughty/dbus.lua
/usr/share/awesome/lib/naughty/init.lua
/usr/share/awesome/lib/wibox/container/arcchart.lua
/usr/share/awesome/lib/wibox/container/background.lua
/usr/share/awesome/lib/wibox/container/constraint.lua
/usr/share/awesome/lib/wibox/container/init.lua
/usr/share/awesome/lib/wibox/container/margin.lua
/usr/share/awesome/lib/wibox/container/mirror.lua
/usr/share/awesome/lib/wibox/container/place.lua
/usr/share/awesome/lib/wibox/container/radialprogressbar.lua
/usr/share/awesome/lib/wibox/container/rotate.lua
/usr/share/awesome/lib/wibox/container/scroll.lua
/usr/share/awesome/lib/wibox/drawable.lua
/usr/share/awesome/lib/wibox/hierarchy.lua
/usr/share/awesome/lib/wibox/init.lua
/usr/share/awesome/lib/wibox/layout/align.lua
/usr/share/awesome/lib/wibox/layout/constraint.lua
/usr/share/awesome/lib/wibox/layout/fixed.lua
/usr/share/awesome/lib/wibox/layout/flex.lua
/usr/share/awesome/lib/wibox/layout/grid.lua
/usr/share/awesome/lib/wibox/layout/init.lua
/usr/share/awesome/lib/wibox/layout/manual.lua
/usr/share/awesome/lib/wibox/layout/margin.lua
/usr/share/awesome/lib/wibox/layout/mirror.lua
/usr/share/awesome/lib/wibox/layout/ratio.lua
/usr/share/awesome/lib/wibox/layout/rotate.lua
/usr/share/awesome/lib/wibox/layout/scroll.lua
/usr/share/awesome/lib/wibox/layout/stack.lua
/usr/share/awesome/lib/wibox/widget/background.lua
/usr/share/awesome/lib/wibox/widget/base.lua
/usr/share/awesome/lib/wibox/widget/calendar.lua
/usr/share/awesome/lib/wibox/widget/checkbox.lua
/usr/share/awesome/lib/wibox/widget/graph.lua
/usr/share/awesome/lib/wibox/widget/imagebox.lua
/usr/share/awesome/lib/wibox/widget/init.lua
/usr/share/awesome/lib/wibox/widget/piechart.lua
/usr/share/awesome/lib/wibox/widget/progressbar.lua
/usr/share/awesome/lib/wibox/widget/separator.lua
/usr/share/awesome/lib/wibox/widget/slider.lua
/usr/share/awesome/lib/wibox/widget/systray.lua
/usr/share/awesome/lib/wibox/widget/textbox.lua
/usr/share/awesome/lib/wibox/widget/textclock.lua
/usr/share/awesome/themes/default/README
/usr/share/awesome/themes/default/background.png
/usr/share/awesome/themes/default/background_white.png
/usr/share/awesome/themes/default/layouts/cornerne.png
/usr/share/awesome/themes/default/layouts/cornernew.png
/usr/share/awesome/themes/default/layouts/cornernw.png
/usr/share/awesome/themes/default/layouts/cornernww.png
/usr/share/awesome/themes/default/layouts/cornerse.png
/usr/share/awesome/themes/default/layouts/cornersew.png
/usr/share/awesome/themes/default/layouts/cornersw.png
/usr/share/awesome/themes/default/layouts/cornersww.png
/usr/share/awesome/themes/default/layouts/dwindle.png
/usr/share/awesome/themes/default/layouts/dwindlew.png
/usr/share/awesome/themes/default/layouts/fairh.png
/usr/share/awesome/themes/default/layouts/fairhw.png
/usr/share/awesome/themes/default/layouts/fairv.png
/usr/share/awesome/themes/default/layouts/fairvw.png
/usr/share/awesome/themes/default/layouts/floating.png
/usr/share/awesome/themes/default/layouts/floatingw.png
/usr/share/awesome/themes/default/layouts/fullscreen.png
/usr/share/awesome/themes/default/layouts/fullscreenw.png
/usr/share/awesome/themes/default/layouts/magnifier.png
/usr/share/awesome/themes/default/layouts/magnifierw.png
/usr/share/awesome/themes/default/layouts/max.png
/usr/share/awesome/themes/default/layouts/maxw.png
/usr/share/awesome/themes/default/layouts/spiral.png
/usr/share/awesome/themes/default/layouts/spiralw.png
/usr/share/awesome/themes/default/layouts/tile.png
/usr/share/awesome/themes/default/layouts/tilebottom.png
/usr/share/awesome/themes/default/layouts/tilebottomw.png
/usr/share/awesome/themes/default/layouts/tileleft.png
/usr/share/awesome/themes/default/layouts/tileleftw.png
/usr/share/awesome/themes/default/layouts/tiletop.png
/usr/share/awesome/themes/default/layouts/tiletopw.png
/usr/share/awesome/themes/default/layouts/tilew.png
/usr/share/awesome/themes/default/submenu.png
/usr/share/awesome/themes/default/taglist/squarefw.png
/usr/share/awesome/themes/default/taglist/squarew.png
/usr/share/awesome/themes/default/theme.lua
/usr/share/awesome/themes/default/titlebar/close_focus.png
/usr/share/awesome/themes/default/titlebar/close_normal.png
/usr/share/awesome/themes/default/titlebar/floating_focus_active.png
/usr/share/awesome/themes/default/titlebar/floating_focus_inactive.png
/usr/share/awesome/themes/default/titlebar/floating_normal_active.png
/usr/share/awesome/themes/default/titlebar/floating_normal_inactive.png
/usr/share/awesome/themes/default/titlebar/maximized_focus_active.png
/usr/share/awesome/themes/default/titlebar/maximized_focus_inactive.png
/usr/share/awesome/themes/default/titlebar/maximized_normal_active.png
/usr/share/awesome/themes/default/titlebar/maximized_normal_inactive.png
/usr/share/awesome/themes/default/titlebar/minimize_focus.png
/usr/share/awesome/themes/default/titlebar/minimize_normal.png
/usr/share/awesome/themes/default/titlebar/ontop_focus_active.png
/usr/share/awesome/themes/default/titlebar/ontop_focus_inactive.png
/usr/share/awesome/themes/default/titlebar/ontop_normal_active.png
/usr/share/awesome/themes/default/titlebar/ontop_normal_inactive.png
/usr/share/awesome/themes/default/titlebar/sticky_focus_active.png
/usr/share/awesome/themes/default/titlebar/sticky_focus_inactive.png
/usr/share/awesome/themes/default/titlebar/sticky_normal_active.png
/usr/share/awesome/themes/default/titlebar/sticky_normal_inactive.png
/usr/share/awesome/themes/gtk/theme.lua
/usr/share/awesome/themes/sky/awesome-icon.png
/usr/share/awesome/themes/sky/layouts/cornerne.png
/usr/share/awesome/themes/sky/layouts/cornernw.png
/usr/share/awesome/themes/sky/layouts/cornerse.png
/usr/share/awesome/themes/sky/layouts/cornersw.png
/usr/share/awesome/themes/sky/layouts/dwindle.png
/usr/share/awesome/themes/sky/layouts/fairh.png
/usr/share/awesome/themes/sky/layouts/fairv.png
/usr/share/awesome/themes/sky/layouts/floating.png
/usr/share/awesome/themes/sky/layouts/fullscreen.png
/usr/share/awesome/themes/sky/layouts/magnifier.png
/usr/share/awesome/themes/sky/layouts/max.png
/usr/share/awesome/themes/sky/layouts/spiral.png
/usr/share/awesome/themes/sky/layouts/tile.png
/usr/share/awesome/themes/sky/layouts/tilebottom.png
/usr/share/awesome/themes/sky/layouts/tileleft.png
/usr/share/awesome/themes/sky/layouts/tiletop.png
/usr/share/awesome/themes/sky/sky-background.png
/usr/share/awesome/themes/sky/theme.lua
/usr/share/awesome/themes/xresources/assets.lua
/usr/share/awesome/themes/xresources/theme.lua
/usr/share/awesome/themes/zenburn/awesome-icon.png
/usr/share/awesome/themes/zenburn/layouts/cornerne.png
/usr/share/awesome/themes/zenburn/layouts/cornernw.png
/usr/share/awesome/themes/zenburn/layouts/cornerse.png
/usr/share/awesome/themes/zenburn/layouts/cornersw.png
/usr/share/awesome/themes/zenburn/layouts/dwindle.png
/usr/share/awesome/themes/zenburn/layouts/fairh.png
/usr/share/awesome/themes/zenburn/layouts/fairv.png
/usr/share/awesome/themes/zenburn/layouts/floating.png
/usr/share/awesome/themes/zenburn/layouts/fullscreen.png
/usr/share/awesome/themes/zenburn/layouts/magnifier.png
/usr/share/awesome/themes/zenburn/layouts/max.png
/usr/share/awesome/themes/zenburn/layouts/spiral.png
/usr/share/awesome/themes/zenburn/layouts/tile.png
/usr/share/awesome/themes/zenburn/layouts/tilebottom.png
/usr/share/awesome/themes/zenburn/layouts/tileleft.png
/usr/share/awesome/themes/zenburn/layouts/tiletop.png
/usr/share/awesome/themes/zenburn/taglist/squarefz.png
/usr/share/awesome/themes/zenburn/taglist/squarez.png
/usr/share/awesome/themes/zenburn/theme.lua
/usr/share/awesome/themes/zenburn/titlebar/close_focus.png
/usr/share/awesome/themes/zenburn/titlebar/close_normal.png
/usr/share/awesome/themes/zenburn/titlebar/floating_focus_active.png
/usr/share/awesome/themes/zenburn/titlebar/floating_focus_inactive.png
/usr/share/awesome/themes/zenburn/titlebar/floating_normal_active.png
/usr/share/awesome/themes/zenburn/titlebar/floating_normal_inactive.png
/usr/share/awesome/themes/zenburn/titlebar/maximized_focus_active.png
/usr/share/awesome/themes/zenburn/titlebar/maximized_focus_inactive.png
/usr/share/awesome/themes/zenburn/titlebar/maximized_normal_active.png
/usr/share/awesome/themes/zenburn/titlebar/maximized_normal_inactive.png
/usr/share/awesome/themes/zenburn/titlebar/ontop_focus_active.png
/usr/share/awesome/themes/zenburn/titlebar/ontop_focus_inactive.png
/usr/share/awesome/themes/zenburn/titlebar/ontop_normal_active.png
/usr/share/awesome/themes/zenburn/titlebar/ontop_normal_inactive.png
/usr/share/awesome/themes/zenburn/titlebar/sticky_focus_active.png
/usr/share/awesome/themes/zenburn/titlebar/sticky_focus_inactive.png
/usr/share/awesome/themes/zenburn/titlebar/sticky_normal_active.png
/usr/share/awesome/themes/zenburn/titlebar/sticky_normal_inactive.png
/usr/share/awesome/themes/zenburn/zenburn-background.png
/usr/share/gnome-session/sessions/awesome.desktop
/usr/share/xdg/awesome/rc.lua
/usr/share/xsessions/awesome.desktop

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/awesome/00-authors.md
/usr/share/doc/awesome/01-readme.md
/usr/share/doc/awesome/02-contributing.md
/usr/share/doc/awesome/LICENSE

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/awesome-wm/LICENSE
