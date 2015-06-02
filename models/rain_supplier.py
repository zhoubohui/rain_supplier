# -*- coding: utf-8 -*-
from openerp import models, api, _, fields
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import  string
class rain_supplier(models.Model):
    _inherit="res.partner"
    zhengjian = fields.Boolean('zhengjian')
    shuiwu = fields.Boolean('shuiwu')
    jgdm = fields.Boolean('jgdm')
    quyang = fields.Boolean('quyang')
    quyang_text=fields.Text('quyang_text')
    category2=fields.Many2one('supplier.category',domain=['|',('id','child_of',122),('idopenerp-','child_of',123)])
    instructor=fields.Text('dsd')
    attachment_count=fields.Many2one('ir.attachment','attachment_count')
    #@api.one
    #def name_get(self):
    #    name=self.category2.name
    #    parent=self.category2
    #    while True:
    #        if parent.parent_id:
    #            name = parent.name +"/"+name
    #            parent=parent.parent_id
    #        else:
    #            name = self.name
    #        return (name,)
    #supplier_type = fields.Selection((('a',u'正式供应商'),('b',u'备选供应商'),('c',u'资源供应商')),'supplier_type',required=True)
    #_defaults = {
    #    'supplier_type':'c'
    #}
    @api.onchange('category2')
    def on_change_category2_type(self):
       # if self.supplier_type == 'b':
       #     if self.zhengjian == False or self.shuiwu == False or self.jgdm == False:
       #         warning={}
       #         warning={
       #             'title':'提示',
       #             'message':'营业执照、税务登记、组织机构代码必须同时勾选并上传相应附件!'
       #         }
       #         self.supplier_type = 'c'
       #         return {'warning':warning}
       self.category=self.category2
       name=self.category2.name_get()
       try:
           if str(name[0]).find('\u5907\u7528')!=-1:
               if self.zhengjian == False or self.shuiwu == False or self.jgdm == False:
                   warning={}
                   warning={
                        'title':'提示',
                        'message':'营业执照、税务登记、组织机构代码必须同时勾选并上传相应附件!'
                    }
                   return {'warning':warning}
       except:
           return


    @api.onchange('category')
    def on_change_category_type(self):
        self.category2=self.category
    @api.onchange('attachment_count')
    def _attachment_count(self):
        AnalyticAccount = self.pool('ir.attachment')
        return {
            partner_id: {
                'attachment_count': AnalyticAccount.search_count([('partner_id', '=', partner_id)])
            }
            for partner_id in ids
        }
class rain_supplier_category(models.Model):
    _inherit="supplier.category"
    #category = fields.Many2one('supplier.category','category')

