# Copyright (C) 2014 Daniele Simonetti
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import os
import sys
import dal
import dal.query
import models
from widgets.skills.choosemore import ChooseMoreSkill

from wizardpage import WizardPage
from PySide import QtCore, QtGui

class SkillsPage(WizardPage):
    def __init__(self, parent=None):
        super(SkillsPage, self).__init__(parent)

        w = ChooseMoreSkill(self)
        w.statusChanged.connect(self.nextAllowed)

        self._set_ui(w)

    def get_h1_text(self):
        return self.tr('''
<center>
<h1>Join your First School</h1>
<p style="color: #666">In this phase you're limited to base schools,
        however you can replace this rank with an alternate path
        on the next step</p>
</center>
        ''')
