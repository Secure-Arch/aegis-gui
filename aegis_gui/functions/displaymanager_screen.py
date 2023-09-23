# displaymanager_screen.py

#
# Copyright 2023 user

#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from gi.repository import Gtk, Adw
from aegis_gui.classes.aegis_screen import AegisScreen


@Gtk.Template(resource_path="/org/athenaos/aegisgui/pages/displaymanager_screen.ui")
class DisplayManagerScreen(AegisScreen, Adw.Bin):
    __gtype_name__ = "DisplayManagerScreen"

    list_displaymanagers = Gtk.Template.Child()

    chosen_displaymanager = ""
    move_to_summary = False

    def __init__(self, window, application, **kwargs):
        super().__init__(**kwargs)
        self.window = window

        self.list_displaymanagers.connect("row-selected", self.selected_displaymanager)

    def selected_displaymanager(self, widget, row):
        if row is not None:
            print(row.get_title())
            self.chosen_displaymanager = row.get_title()
            row.select_button.set_active(True)

            self.set_valid(True)
        else:
            print("row is none!!")
