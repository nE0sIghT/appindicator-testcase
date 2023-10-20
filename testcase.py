#!/usr/bin/python3

import gi
from pathlib import Path
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

ROOT = Path( __file__ ).parent.absolute()

try:
    gi.require_version('AyatanaAppIndicator3', '0.1')
    from gi.repository import AyatanaAppIndicator3 as AppIndicator
except (ImportError, ValueError):
    gi.require_version('AppIndicator3', '0.1')
    from gi.repository import AppIndicator3 as AppIndicator


class App:
    def __init__(self) -> None:
        self.indicator = AppIndicator.Indicator.new(
            "testcase",
            str(ROOT / "emblem-web.svg"),
            AppIndicator.IndicatorCategory.APPLICATION_STATUS
        )

        self.indicator.set_attention_icon_full(
            str(ROOT / "unread.png"),
            "test"
        )
        self.indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
        self.indicator.set_title("test")

        self.menu = Gtk.Menu()

        for i in range(3):
            buf = "Test-undermenu - %d" % i
            menu_items = Gtk.MenuItem(label=buf)
            self.menu.append(menu_items)

        menu_items.show()

        self.indicator.set_menu(self.menu)

        self.i = 1
        GLib.timeout_add_seconds(5, self.tick, None)

    def tick(self, any):
        print(self.i)
        if self.i % 2:
            self.indicator.set_label(str(self.i), "99")
            self.indicator.set_status(AppIndicator.IndicatorStatus.ATTENTION)
        else:
            self.indicator.set_label("", "99")
            self.indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)

        self.i = min(99, self.i + 1)

        return True

    def main(self):
        Gtk.main()
        print("Quit")


if __name__ == '__main__':
    App().main()
