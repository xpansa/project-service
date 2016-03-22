# coding: utf-8
# © 2016 Veronika Kotovich @ Xpansa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class ProjectIssue(models.Model):
    _inherit = 'project.issue'

    gantt_date_start = fields.Datetime('Starting Date', select=True, copy=False)
    gantt_date_end = fields.Datetime('Ending Date', select=True, copy=False)
    