from odoo import api, models, fields, _


class QualityVerification(models.Model):
    _inherit = 'quality.check'

    quality_state = fields.Selection([
        ('none', 'To do'),
        ('pass', 'Passed'),
        ('fail', 'Failed'),
        ('verified', 'Verified')], string='Status', tracking=True,
        default='none', copy=False)

    def action_verified(self):
        self.quality_state = 'verified'
        return True


