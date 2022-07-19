# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
import pdb,logging

from openerp.tools.translate import _
import json
import requests
#, msal, base64

#import werkzeug.urls
#import urlparse
#import urllib2
#import simplejson


logger = logging.getLogger(__name__)


class res_users(models.Model):
    _name = "res.users"
    _inherit = "res.users"

    # @api.model
    # def auth_oauth(self,provider,params=None):
    #     res=super(res_users, self).auth_oauth(provider,params)
    #     return res

    @api.model
    def _auth_oauth_rpc(self, endpoint, access_token):
        #Microsoft works with a get request with Bearer authetication
        #this is a lazy trick to detecht wether the oauth provider is microsoft
        # if the endpoint is not microsoft, this little hack wil not work
        if "microsoft" in endpoint:
            response= requests.get( endpoint, headers={'Authorization': 'Bearer ' + access_token}, )
            try:
                response=response.json()
            except:
                response={}    
#            pdb.set_trace()
        else:    
#            pdb.set_trace()
            response=super(res_users, self)._auth_oauth_rpc(endpoint, access_token)

        return response